"""Index Graph - Create and store documents in vector database.

Simple graph to index documents using Ollama embeddings and local LanceDB.
"""

import json
import os
from dataclasses import dataclass, field
from typing import Annotated, Any, Literal, Optional, Type, TypeVar

from langchain_core.documents import Document
from langchain_core.runnables import RunnableConfig, ensure_config
from langchain_ollama import OllamaEmbeddings
from langgraph.graph import END, START, StateGraph


# State management
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


@dataclass(kw_only=True)
class IndexState:
    """State for document indexing."""
    docs: Annotated[list[Document], reduce_docs]


@dataclass(kw_only=True)
class IndexConfiguration:
    """Configuration for indexing."""
    
    embedding_model: str = field(
        default="nomic-embed-text:latest",
        metadata={"description": "Ollama embedding model name"}
    )
    
    lancedb_uri: str = field(
        default="./lancedb",  # Local LanceDB directory
        metadata={"description": "Local LanceDB directory path"}
    )
    
    table_name: str = field(
        default="documents",
        metadata={"description": "Table name in LanceDB"}
    )
    
    docs_file: str = field(
        default="src_rag_template/sample_docs.json",
        metadata={"description": "Path to JSON file containing documents"}
    )

    @classmethod
    def from_runnable_config(cls, config: Optional[RunnableConfig] = None):
        """Create configuration from RunnableConfig."""
        config = ensure_config(config)
        configurable = config.get("configurable") or {}
        return cls(**{k: v for k, v in configurable.items() if hasattr(cls, k)})


async def index_docs(
    state: IndexState, *, config: Optional[RunnableConfig] = None
) -> dict[str, str]:
    """Index documents into LanceDB."""
    if not config:
        raise ValueError("Configuration required!")

    configuration = IndexConfiguration.from_runnable_config(config)
    docs = state.docs
    
    # If no docs, load from file
    if not docs:
        try:
            with open(configuration.docs_file, 'r', encoding='utf-8') as f:
                serialized_docs = json.load(f)
                docs = [
                    Document(
                        page_content=doc.get("page_content", ""),
                        metadata=doc.get("metadata", {})
                    )
                    for doc in serialized_docs
                ]
        except FileNotFoundError:
            print(f"File {configuration.docs_file} does not exist")
            return {"docs": "delete"}
    
    if not docs:
        print("No documents to index")
        return {"docs": "delete"}
    
    try:
        # Initialize Ollama embeddings
        embeddings = OllamaEmbeddings(model=configuration.embedding_model)
        
        # Initialize LanceDB
        import lancedb
        from langchain_community.vectorstores import LanceDB
        
        # Connect to local LanceDB
        vectorstore = LanceDB(
            uri=configuration.lancedb_uri,
            embedding=embeddings,
            table_name=configuration.table_name
        )
        
        # Add documents to vector store
        await vectorstore.aadd_documents(docs)
        
        print(f"Successfully indexed {len(docs)} documents into LanceDB")
        
    except Exception as e:
        print(f"Error indexing documents: {e}")
        return {"docs": "delete"}
    
    return {"docs": "delete"}


# Create graph
builder = StateGraph(IndexState, config_schema=IndexConfiguration)
builder.add_node("index_docs", index_docs)
builder.add_edge(START, "index_docs")
builder.add_edge("index_docs", END)

# Compile graph
graph = builder.compile()
graph.name = "IndexGraph"

if __name__ == "__main__":
    print("Index Graph created successfully!")
    print("Use 'langgraph dev' to test graph")
