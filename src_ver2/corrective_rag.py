import json
import asyncio
from datetime import datetime

from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, MessagesState, END, START
from langchain_core.tools import tool

from openevals.llm import create_async_llm_as_judge
from openevals.prompts import (
    RAG_RETRIEVAL_RELEVANCE_PROMPT,
    RAG_HELPFULNESS_PROMPT,
)

# model = ChatGoogleGenerativeAI(
#     model="gemini-2.0-flash",
#     temperature=0.2
# )

model = ChatOllama(model="qwen2.5:0.5b", temperature=0.2)


current_date = datetime.now().strftime("%A, %B %d, %Y")

MAX_SEARCH_RETRIES = 5


class GraphState(MessagesState):
    original_question: str
    attempted_search_queries: list[str]


relevance_evaluator = create_async_llm_as_judge(
    judge=model,
    prompt=RAG_RETRIEVAL_RELEVANCE_PROMPT + f"\n\nThe current date is {current_date}.",
    feedback_key="retrieval_relevance",
)

helpfulness_evaluator = create_async_llm_as_judge(
    judge=model,
    prompt=RAG_HELPFULNESS_PROMPT
    + f'\nReturn "true" if the answer is helpful, and "false" otherwise.\n\nThe current date is {current_date}.',
    feedback_key="helpfulness",
)


SYSTEM_PROMPT = """
Use the provided web search tool to find the latest information if you are not sure of what the user is asking for.
"""


# Simplify the Tavily search tool's input schema for a small local model
@tool
async def search_tool(query: str):
    """Search the web for information relevant to the query.
    
    """
    return await TavilySearch(max_results=5).ainvoke({"query": query})


model_with_tools = model.bind_tools([search_tool])


async def relevance_filter(state: GraphState):
    last_message = state["messages"][-1]
    if last_message.type == "tool" and last_message.name == search_tool.name:
        search_results = json.loads(last_message.content).get("results", [])
        filtered_results = []

        # Create a semaphore to limit concurrent tasks to 2
        semaphore = asyncio.Semaphore(2)

        async def evaluate_with_semaphore(result):
            async with semaphore:
                eval_result = await relevance_evaluator(
                    inputs=state["attempted_search_queries"][-1], context=result
                )
                return result, eval_result

        # Create tasks for all results
        tasks = [evaluate_with_semaphore(result) for result in search_results]

        # Process tasks as they complete
        for completed_task in asyncio.as_completed(tasks):
            result, eval_result = await completed_task
            if eval_result["score"]:
                filtered_results.append(result)

        last_message.content = json.dumps({"results": filtered_results})
        return {"messages": [last_message]}
    else:
        raise Exception(f"Relevance filter node must be called after web search")


async def should_continue(state: GraphState):
    if len(state["attempted_search_queries"]) > MAX_SEARCH_RETRIES:
        return END
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "web_search"
    return "reflect"


async def call_model(state: GraphState):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + state["messages"]
    response = await model_with_tools.ainvoke(messages)
    if response.tool_calls and response.tool_calls[0]["name"] == search_tool.name:
        search_query = response.tool_calls[0]["args"]["query"]
        return {
            "messages": [response],
            "attempted_search_queries": state["attempted_search_queries"]
            + [search_query],
        }
    return {"messages": [response]}


async def web_search(state: GraphState):
    last_message = state["messages"][-1]
    search_results = await search_tool.ainvoke(last_message.tool_calls[0])
    return {"messages": [search_results]}


async def reflect(state: GraphState):
    last_message = state["messages"][-1]
    helpfulness_eval_result = await helpfulness_evaluator(
        inputs=state["original_question"], outputs=last_message.content
    )
    if not helpfulness_eval_result["score"]:
        return {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
I originally asked you the following question:

<original_question>
{state["original_question"]}
</original_question>

Your answer was not helpful for the following reason:

<reason>
{helpfulness_eval_result['comment']}
</reason>

Please check the conversation history carefully and try again. You may choose to fetch more information if you think the answer
to the original question is not somewhere in the conversation, but carefully consider if the answer is already in the conversation.

You have already attempted to answer the original question using the following search queries,
so if you choose to search again, you must rephrase your search query to be different from the ones below to avoid fetching redundant information:

<attempted_search_queries>
{state['attempted_search_queries']}
</attempted_search_queries>

As a reminder, check the previous conversation history and fetched context carefully before searching again!
""",
                }
            ]
        }

    return {}


async def retry_or_end(state: GraphState):
    if state["messages"][-1].type == "human":
        return "agent"
    return END


workflow = StateGraph(GraphState, input=MessagesState, output=MessagesState)

workflow.add_node(
    "store_original_question",
    lambda state: {
        "original_question": state["messages"][-1].content,
        "attempted_search_queries": [],
    },
)
workflow.add_node("agent", call_model)
workflow.add_node("web_search", web_search)
workflow.add_node("relevance_filter", relevance_filter)
workflow.add_node("reflect", reflect)

workflow.add_edge(START, "store_original_question")
workflow.add_edge("store_original_question", "agent")
workflow.add_conditional_edges("agent", should_continue, ["web_search", "reflect", END])
workflow.add_edge("web_search", "relevance_filter")
workflow.add_edge("relevance_filter", "agent")
workflow.add_conditional_edges(
    "reflect",
    retry_or_end,
    ["agent", END],
)

agent = workflow.compile()