from datetime import datetime

from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool

from openevals.llm import create_llm_as_judge
from openevals.prompts import RAG_RETRIEVAL_RELEVANCE_PROMPT

# llm = init_chat_model("ollama:qwen2.5:7b", temperature=0.2)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2
)

# Simplify the Tavily search tool's input schema for a small local model
@tool
async def search_tool(query: str):
    """Search the web for information relevant to the query."""
    return await TavilySearch(max_results=5).ainvoke({"query": query})


current_date = datetime.now().strftime("%A, %B %d, %Y")

relevance_evaluator = create_llm_as_judge(
    judge=llm,
    prompt=RAG_RETRIEVAL_RELEVANCE_PROMPT + f"\n\nThe current date is {current_date}.",
    feedback_key="retrieval_relevance",
)

agent = create_react_agent(
    llm,
    prompt=f"The current date is {current_date}.",
    tools=[search_tool],
)