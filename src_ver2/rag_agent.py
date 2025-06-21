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

current_date = datetime.now().strftime("%A, %B %d, %Y")

model = ChatOllama(model="gemma3:1b", temperature=0.2)

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
Use the provided context to answer the user's question.
"""

def generate_query(state: GraphState):
    






