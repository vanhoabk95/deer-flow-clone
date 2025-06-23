"""Retrieval Graph - Chat with documents using RAG.

Simple graph to chat with indexed documents, 
using Gemini for chat and Ollama embeddings for retrieval.
"""

import asyncio
import hashlib
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Annotated, Any, Literal, Optional, TypedDict, cast

from langchain_core.documents import Document
from langchain_core.messages import AnyMessage, BaseMessage
from langchain_core.runnables import RunnableConfig, ensure_config
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaEmbeddings
from langgraph.graph import END, START, StateGraph, add_messages

try:
    from openevals.llm import create_async_llm_as_judge
    from openevals.prompts import RAG_RETRIEVAL_RELEVANCE_PROMPT
    OPENEVALS_AVAILABLE = True
except ImportError:
    OPENEVALS_AVAILABLE = False
    print("⚠️ openevals not available, relevance evaluation will be skipped")


# Document utilities
def _generate_uuid(page_content: str) -> str:
    """Generate UUID from content."""
    md5_hash = hashlib.md5(page_content.encode()).hexdigest()
    return str(uuid.UUID(md5_hash))


def reduce_docs(
    existing: Optional[list[Document]],
    new: list[Document] | str | Literal["delete"],
) -> list[Document]:
    """Reduce and process documents."""
    if new == "delete":
        return []
    
    existing_list = list(existing) if existing else []
    
    if isinstance(new, str):
        return existing_list + [Document(page_content=new)]
    
    if isinstance(new, list):
        return existing_list + new
    
    return existing_list


def format_docs(docs: Optional[list[Document]]) -> str:
    """Format documents to XML string."""
    if not docs:
        return "<documents></documents>"
    
    formatted = []
    for doc in docs:
        metadata = doc.metadata or {}
        meta = "".join(f" {k}={v!r}" for k, v in metadata.items())
        if meta:
            meta = f" {meta}"
        formatted.append(f"<document{meta}>\n{doc.page_content}\n</document>")
    
    return f"""<documents>
{chr(10).join(formatted)}
</documents>"""


# State management
@dataclass(kw_only=True)
class InputState:
    """Input state for retrieval graph."""
    messages: Annotated[list[AnyMessage], add_messages]


class Router(TypedDict):
    """Classify user query."""
    logic: str
    type: Literal["more-info", "langchain", "general"]


@dataclass(kw_only=True)
class RetrievalState(InputState):
    """State for retrieval graph."""
    router: Router = field(default_factory=lambda: Router(type="general", logic=""))
    documents: Annotated[list[Document], reduce_docs] = field(default_factory=list)
    original_query: str = ""
    generated_queries: list[str] = field(default_factory=list)
    relevance_scores: list[bool] = field(default_factory=list)


@dataclass(kw_only=True)
class RetrievalConfiguration:
    """Configuration for retrieval graph."""
    
    # Provider selection
    llm_provider: Literal["gemini", "ollama"] = field(
        default="ollama",
        metadata={"description": "LLM provider to use (gemini or ollama)"}
    )
    
    # Gemini model configuration
    gemini_model: str = field(
        default="gemini-2.0-flash",
        metadata={"description": "Gemini model name"}
    )
    
    # Ollama model configuration  
    ollama_model: str = field(
        default="gemma3:1b",
        metadata={"description": "Ollama model name"}
    )
    
    embedding_model: str = field(
        default="nomic-embed-text:latest",
        metadata={"description": "Ollama embedding model"}
    )
    
    lancedb_uri: str = field(
        default="./lancedb",
        metadata={"description": "LanceDB local path"}
    )
    
    table_name: str = field(
        default="documents",
        metadata={"description": "Table name in LanceDB"}
    )
    
    search_kwargs: dict[str, Any] = field(
        default_factory=lambda: {"k": 5},
        metadata={"description": "Search parameters for retriever"}
    )
    
    enable_relevance_filter: bool = field(
        default=True,
        metadata={"description": "Enable relevance evaluation and filtering"}
    )
    
    min_relevant_docs: int = field(
        default=1,
        metadata={"description": "Minimum number of relevant documents to keep (even if all scored 0)"}
    )
    
    num_generated_queries: int = field(
        default=3,
        metadata={"description": "Number of additional search queries to generate"}
    )
    
    max_docs_per_query: int = field(
        default=3,
        metadata={"description": "Maximum documents to retrieve per query"}
    )

    @classmethod
    def from_runnable_config(cls, config: Optional[RunnableConfig] = None):
        """Create configuration from RunnableConfig."""
        config = ensure_config(config)
        configurable = config.get("configurable") or {}
        return cls(**{k: v for k, v in configurable.items() if hasattr(cls, k)})


# Prompts (from original prompts.py)
ROUTER_SYSTEM_PROMPT = """You are a LangChain Developer advocate. Your job is help people using LangChain answer any issues they are running into.

A user will come to you with an inquiry. Your first job is to classify what type of inquiry it is. The types of inquiries you should classify it as are:

## 'langchain'
Classify a user inquiry as this if it can be answered by looking up information related to LangChain open source package. The LangChain open source package \
is a python library for working with LLMs. It integrates with various LLMs, databases and APIs.

## 'general'
Classify a user inquiry as this if it is just a general question not related to LangChain.

You SHOULD NOT include any other text in the response

{
  "logic": "your logic reasoning here",
  "type": "langchain" or "general" or "more-info"
}
"""

GENERAL_SYSTEM_PROMPT = """You are a LangChain Developer advocate. Your job is help people using LangChain answer any issues they are running into.

Your boss has determined that the user is asking a general question, not one related to LangChain. This was their logic:

<logic>
{logic}
</logic>

Respond to the user. Politely decline to answer and tell them you can only answer questions about LangChain-related topics, and that if their question is about LangChain they should clarify how it is.\
Be nice to them though - they are still a user!"""

RESPONSE_SYSTEM_PROMPT = """\
You are an expert programmer and problem-solver, tasked with answering any question \
about LangChain.

Generate a comprehensive and informative answer for the \
given question based solely on the provided search results (URL and content). \
Do NOT ramble, and adjust your response length based on the question. If they ask \
a question that can be answered in one sentence, do that. If 5 paragraphs of detail is needed, \
do that. You must \
only use information from the provided search results. Use an unbiased and \
journalistic tone. Combine search results together into a coherent answer. Do not \
repeat text. Cite search results using [${{number}}] notation. Only cite the most \
relevant results that answer the question accurately. Place these citations at the end \
of the individual sentence or paragraph that reference them. \
Do not put them all at the end, but rather sprinkle them throughout. If \
different results refer to different entities within the same name, write separate \
answers for each entity.

You should use bullet points in your answer for readability. Put citations where they apply
rather than putting them all at the end. DO NOT PUT THEM ALL THAT END, PUT THEM IN THE BULLET POINTS.

If there is nothing in the context relevant to the question at hand, do NOT make up an answer. \
Rather, tell them why you're unsure and ask for any additional information that may help you answer better.

Sometimes, what a user is asking may NOT be possible. Do NOT tell them that things are possible if you don't \
see evidence for it in the context below. If you don't see based in the information below that something is possible, \
do NOT say that it is - instead say that you're not sure.

Anything between the following `context` html blocks is retrieved from a knowledge \
bank, not part of the conversation with the user.

<context>
    {context}
<context/>"""

QUERY_GENERATION_PROMPT = """You are an expert at generating search queries for document retrieval systems.

Given a user's question, generate {num_queries} different search queries that would help find relevant information to answer the question.

The queries should:
1. Use different keywords and phrasings
2. Focus on different aspects of the question
3. Be specific and targeted for document search
4. Cover the main concepts and related topics

Original question: {original_question}

Generate exactly {num_queries} search queries, one per line:"""


# Initialize relevance evaluator if openevals is available
current_date = datetime.now().strftime("%A, %B %d, %Y")

def create_chat_model(configuration: RetrievalConfiguration, temperature: float = 0):
    """Create appropriate chat model based on provider configuration."""
    if configuration.llm_provider == "gemini":
        print(f"🤖 Sử dụng Gemini model: {configuration.gemini_model}")
        # return ChatGoogleGenerativeAI(
        #     model=configuration.gemini_model,
        #     temperature=temperature
        # )
        return ChatOpenAI(
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            model=configuration.gemini_model,
            api_key="AIzaSyB2ULrNJY75iGN_7waSjZjFRfYfe3T9A_o",
            temperature=temperature
        )

    elif configuration.llm_provider == "ollama":
        print(f"🦙 Sử dụng Ollama model: {configuration.ollama_model}")
        return ChatOllama(
            model=configuration.ollama_model,
            temperature=temperature
        )
    else:
        raise ValueError(f"❌ Provider không được hỗ trợ: {configuration.llm_provider}. Chỉ hỗ trợ 'gemini' hoặc 'ollama'")

def create_relevance_evaluator(model):
    """Create relevance evaluator if openevals is available."""
    if not OPENEVALS_AVAILABLE:
        return None
    
    return create_async_llm_as_judge(
        judge=model,
        prompt=RAG_RETRIEVAL_RELEVANCE_PROMPT + f"\n\nThe current date is {current_date}.",
        feedback_key="retrieval_relevance",
    )


# Graph nodes
async def analyze_and_route_query(
    state: RetrievalState, *, config: RunnableConfig
) -> dict[str, Router]:
    """Analyze and route user query."""
    configuration = RetrievalConfiguration.from_runnable_config(config)
    
    # Create chat model based on provider
    model = create_chat_model(configuration, temperature=0)
    
    messages = [
        {"role": "system", "content": ROUTER_SYSTEM_PROMPT}
    ] + [{"role": msg.type, "content": msg.content} for msg in state.messages]
    
    response = cast(
        Router, await model.with_structured_output(Router).ainvoke(messages)
    )
    return {"router": response}


def route_query(state: RetrievalState) -> Literal["generate_search_queries", "respond_general", "ask_for_more_info"]:
    """Determine next step based on classification."""
    _type = state.router["type"]
    if _type == "langchain":
        return "generate_search_queries"
    elif _type == "general":
        return "respond_general"
    elif _type == "more-info":
        return "ask_for_more_info"
    else:
        return "respond_general"


async def respond_general(
    state: RetrievalState, *, config: RunnableConfig
) -> dict[str, list[BaseMessage]]:
    """Respond to general queries."""
    configuration = RetrievalConfiguration.from_runnable_config(config)
    
    model = create_chat_model(configuration, temperature=0.3)
    
    system_prompt = GENERAL_SYSTEM_PROMPT.format(logic=state.router["logic"])
    messages = [
        {"role": "system", "content": system_prompt}
    ] + [{"role": msg.type, "content": msg.content} for msg in state.messages]
    
    response = await model.ainvoke(messages)
    return {"messages": [response]}


async def ask_for_more_info(
    state: RetrievalState, *, config: RunnableConfig
) -> dict[str, list[BaseMessage]]:
    """Ask for more information when needed."""
    configuration = RetrievalConfiguration.from_runnable_config(config)
    
    model = create_chat_model(configuration, temperature=0.3)
    
    # Using the same prompt logic as general for simplicity
    system_prompt = """You are a LangChain Developer advocate. Your job is help people using LangChain answer any issues they are running into.

Your boss has determined that more information is needed before doing any research on behalf of the user. This was their logic:

<logic>
{logic}
</logic>

Respond to the user and try to get any more relevant information. Do not overwhelm them! Be nice, and only ask them a single follow up question.""".format(logic=state.router["logic"])
    
    messages = [
        {"role": "system", "content": system_prompt}
    ] + [{"role": msg.type, "content": msg.content} for msg in state.messages]
    
    response = await model.ainvoke(messages)
    return {"messages": [response]}


async def generate_search_queries(
    state: RetrievalState, *, config: RunnableConfig
) -> dict[str, Any]:
    """Generate multiple search queries from user question."""
    configuration = RetrievalConfiguration.from_runnable_config(config)
    
    # Get original query from last message
    last_message = state.messages[-1]
    original_query = last_message.content if hasattr(last_message, 'content') else str(last_message)
    
    # Generate multiple queries using LLM
    model = create_chat_model(configuration, temperature=0.3)
    
    prompt = QUERY_GENERATION_PROMPT.format(
        num_queries=configuration.num_generated_queries,
        original_question=original_query
    )
    
    try:
        response = await model.ainvoke([{"role": "user", "content": prompt}])
        generated_text = response.content
        
        # Parse queries from response (one per line)
        queries = [line.strip() for line in generated_text.split('\n') if line.strip()]
        
        # Ensure we have the right number of queries
        queries = queries[:configuration.num_generated_queries]
        
        # Add original query to the list
        all_queries = [original_query] + queries
        
        print(f"🧠 Generated {len(queries)} additional search queries:")
        for i, query in enumerate(queries, 1):
            print(f"   {i}. {query}")
        
        return {
            "original_query": original_query,
            "generated_queries": all_queries
        }
        
    except Exception as e:
        print(f"⚠️ Error generating queries, using original: {e}")
        return {
            "original_query": original_query,
            "generated_queries": [original_query]
        }


async def search_documents(
    state: RetrievalState, *, config: RunnableConfig
) -> dict[str, Any]:
    """Search and retrieve documents using multiple queries."""
    configuration = RetrievalConfiguration.from_runnable_config(config)
    
    if not state.generated_queries:
        print("⚠️ No generated queries found, using original query")
        queries = [state.original_query] if state.original_query else [""]
    else:
        queries = state.generated_queries
    
    all_documents = []
    seen_content = set()  # For deduplication
    
    try:
        # Initialize embeddings and retriever
        embeddings = OllamaEmbeddings(model=configuration.embedding_model)
        
        import lancedb
        from langchain_community.vectorstores import LanceDB
        
        # Connect to LanceDB
        vectorstore = LanceDB(
            uri=configuration.lancedb_uri,
            embedding=embeddings,
            table_name=configuration.table_name
        )
        
        # Search with each query
        search_kwargs = {"k": configuration.max_docs_per_query}
        retriever = vectorstore.as_retriever(search_kwargs=search_kwargs)
        
        print(f"🔍 Searching with {len(queries)} queries...")
        
        for i, query in enumerate(queries, 1):
            try:
                print(f"   Query {i}: {query[:50]}{'...' if len(query) > 50 else ''}")
                documents = await retriever.ainvoke(query)
                
                # Deduplicate documents based on content
                for doc in documents:
                    content_hash = hashlib.md5(doc.page_content.encode()).hexdigest()
                    if content_hash not in seen_content:
                        seen_content.add(content_hash)
                        all_documents.append(doc)
                        
            except Exception as e:
                print(f"   ⚠️ Error with query {i}: {e}")
                continue
        
        print(f"📚 Total unique documents found: {len(all_documents)}")
        
    except Exception as e:
        print(f"❌ Error retrieving documents: {e}")
        all_documents = []
    
    return {"documents": all_documents}


async def evaluate_relevance(
    state: RetrievalState, *, config: RunnableConfig
) -> dict[str, Any]:
    """Evaluate relevance of retrieved documents using binary classification."""
    configuration = RetrievalConfiguration.from_runnable_config(config)
    
    if not configuration.enable_relevance_filter or not OPENEVALS_AVAILABLE:
        print("📝 Relevance evaluation skipped - using all documents")
        return {"relevance_scores": [True] * len(state.documents)}
    
    if not state.documents:
        return {"relevance_scores": []}
    
    # Create relevance evaluator
    model = create_chat_model(configuration, temperature=0)
    
    relevance_evaluator = create_relevance_evaluator(model)
    if not relevance_evaluator:
        return {"relevance_scores": [True] * len(state.documents)}
    
    print(f"🧠 Evaluating relevance of {len(state.documents)} documents...")
    
    # Create a semaphore to limit concurrent tasks to 2
    semaphore = asyncio.Semaphore(2)
    scores = []
    
    async def evaluate_with_semaphore(doc):
        async with semaphore:
            try:
                eval_result = await relevance_evaluator(
                    inputs=state.original_query, 
                    context=doc.page_content
                )
                # openevals returns binary classification (True/False or 1/0)
                score = eval_result.get("score", False)
                return bool(score)  # Ensure boolean result
            except Exception as e:
                print(f"⚠️ Error evaluating document relevance: {e}")
                return True  # Default to keeping document on error
    
    # Create tasks for all documents
    tasks = [evaluate_with_semaphore(doc) for doc in state.documents]
    
    # Process tasks as they complete
    for completed_task in asyncio.as_completed(tasks):
        score = await completed_task
        scores.append(score)
    
    relevant_count = sum(scores)
    print(f"📊 Relevance results: {relevant_count}/{len(scores)} documents marked as relevant")
    print(f"🔍 Binary scores: {['✓' if s else '✗' for s in scores]}")
    
    return {"relevance_scores": scores}


async def filter_documents(
    state: RetrievalState, *, config: RunnableConfig
) -> dict[str, list[Document]]:
    """Filter documents based on binary relevance classification."""
    configuration = RetrievalConfiguration.from_runnable_config(config)
    
    if not configuration.enable_relevance_filter or not state.relevance_scores:
        return {"documents": state.documents}
    
    # Filter documents by binary relevance scores
    filtered_docs = []
    
    for doc, is_relevant in zip(state.documents, state.relevance_scores):
        if is_relevant:
            filtered_docs.append(doc)
    
    # Ensure we have at least min_relevant_docs if available
    if len(filtered_docs) == 0 and len(state.documents) > 0:
        min_docs = min(configuration.min_relevant_docs, len(state.documents))
        filtered_docs = state.documents[:min_docs]
        print(f"⚠️ No documents marked as relevant, keeping top {min_docs} document(s)")
    
    print(f"🔧 Filtered {len(state.documents)} → {len(filtered_docs)} documents (binary relevance)")
    
    return {"documents": filtered_docs}


def should_continue_to_response(state: RetrievalState) -> Literal["evaluate_relevance", "generate_response"]:
    """Determine if we should evaluate relevance or go directly to response."""
    # Default to enabling relevance filter if openevals is available
    if OPENEVALS_AVAILABLE and state.documents:
        return "evaluate_relevance"
    else:
        return "generate_response"


async def generate_response(
    state: RetrievalState, *, config: RunnableConfig
) -> dict[str, list[BaseMessage]]:
    """Generate response with filtered documents as context."""
    configuration = RetrievalConfiguration.from_runnable_config(config)
    
    # Generate response with context
    model = create_chat_model(configuration, temperature=0.1)
    
    context = format_docs(state.documents)
    system_prompt = RESPONSE_SYSTEM_PROMPT.format(context=context)
    messages = [
        {"role": "system", "content": system_prompt}
    ] + [{"role": msg.type, "content": msg.content} for msg in state.messages]
    
    response = await model.ainvoke(messages)
    return {"messages": [response]}


# Create graph
builder = StateGraph(RetrievalState, input=InputState, config_schema=RetrievalConfiguration)
builder.add_node("analyze_and_route_query", analyze_and_route_query)
builder.add_node("respond_general", respond_general)
builder.add_node("ask_for_more_info", ask_for_more_info)
builder.add_node("generate_search_queries", generate_search_queries)
builder.add_node("search_documents", search_documents)
builder.add_node("evaluate_relevance", evaluate_relevance)
builder.add_node("filter_documents", filter_documents)
builder.add_node("generate_response", generate_response)

builder.add_edge(START, "analyze_and_route_query")
builder.add_conditional_edges("analyze_and_route_query", route_query)
builder.add_edge("respond_general", END)
builder.add_edge("ask_for_more_info", END)
builder.add_edge("generate_search_queries", "search_documents")
builder.add_conditional_edges("search_documents", should_continue_to_response)
builder.add_edge("evaluate_relevance", "filter_documents")
builder.add_edge("filter_documents", "generate_response")
builder.add_edge("generate_response", END)

# Compile graph
graph = builder.compile()
graph.name = "RetrievalGraph"

if __name__ == "__main__":
    print("🎉 Retrieval Graph đã được tạo thành công!")
    print("📚 Hỗ trợ cả Gemini và Ollama LLM providers")
    print("\n🚀 Cách sử dụng:")
    print("   langgraph dev --configurable llm_provider=gemini --configurable gemini_model=gemini-2.0-flash-exp")
    print("   langgraph dev --configurable llm_provider=ollama --configurable ollama_model=gemma2:2b")
    print("   langgraph dev  # (mặc định sử dụng Ollama)")
    print("\n📖 Xem config_example.py để biết thêm chi tiết")
