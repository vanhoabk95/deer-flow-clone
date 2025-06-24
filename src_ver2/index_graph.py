"""Index Graph - Create and store PDF documents in vector database.

PDF-focused graph that converts PDFs to markdown, applies semantic chunking,
and stores embeddings with detailed metadata for retrieval.
"""

import json
import os
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Annotated, Any, Literal, Optional, Type, TypeVar

from langchain_core.documents import Document
from langchain_core.runnables import RunnableConfig, ensure_config
from langchain_ollama import OllamaEmbeddings
from langgraph.graph import END, START, StateGraph

# PDF processing imports
import pymupdf4llm
from langchain_experimental.text_splitter import SemanticChunker


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
    """State for PDF document indexing."""
    docs: Annotated[list[Document], reduce_docs] = field(default_factory=list)
    
    # Input PDF paths to be indexed (only .pdf files accepted)
    document_paths: list[str] = field(
        default_factory=list,
        metadata={"description": "List of PDF file paths to be indexed"}
    )
    
    # Knowledge base path where documents and lancedb will be stored
    knowledge_base: str = field(
        default="appdata/knowledge_base_test",
        metadata={"description": "Path to knowledge base folder"}
    )


@dataclass(kw_only=True)
class IndexConfiguration:
    """Configuration for PDF indexing."""
    
    embedding_model: str = field(
        default="nomic-embed-text:latest",
        metadata={"description": "Ollama embedding model name"}
    )
    
    # Base directory for all knowledge bases
    base_appdata_dir: str = field(
        default="appdata",
        metadata={"description": "Base directory for all knowledge bases"}
    )
    
    # Default knowledge base name
    default_knowledge_base: str = field(
        default="knowledge_base_test",
        metadata={"description": "Default knowledge base folder name"}
    )
    
    table_name: str = field(
        default="documents",
        metadata={"description": "Table name in LanceDB"}
    )
    
    # Semantic chunking configuration
    chunk_breakpoint_threshold_type: str = field(
        default="percentile",
        metadata={"description": "Semantic chunking breakpoint type"}
    )
    
    chunk_breakpoint_threshold_amount: int = field(
        default=95,
        metadata={"description": "Semantic chunking breakpoint threshold"}
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
    """Index PDF documents into knowledge base specific LanceDB."""
    if not config:
        raise ValueError("Configuration required!")

    configuration = IndexConfiguration.from_runnable_config(config)
    
    # Determine knowledge base path
    knowledge_base_path = state.knowledge_base
    if not knowledge_base_path or knowledge_base_path == "":
        knowledge_base_path = os.path.join(
            configuration.base_appdata_dir, 
            configuration.default_knowledge_base
        )
    
    # Create knowledge base directory structure
    kb_path = Path(knowledge_base_path)
    documents_dir = kb_path / "documents"
    markdown_dir = kb_path / "markdown"  # Store converted markdown files
    lancedb_dir = kb_path / "lancedb"
    
    # Create directories if they don't exist
    kb_path.mkdir(parents=True, exist_ok=True)
    documents_dir.mkdir(exist_ok=True)
    markdown_dir.mkdir(exist_ok=True)
    lancedb_dir.mkdir(exist_ok=True)
    
    print(f"📁 Knowledge base: {kb_path}")
    print(f"📄 PDF documents dir: {documents_dir}")
    print(f"📝 Markdown dir: {markdown_dir}")
    print(f"🗄️ LanceDB dir: {lancedb_dir}")
    
    docs = state.docs
    
    # Initialize Ollama embeddings for semantic chunking
    print(f"🤖 Initializing embeddings: {configuration.embedding_model}")
    embeddings = OllamaEmbeddings(model=configuration.embedding_model)
    
    # Initialize semantic chunker
    semantic_chunker = SemanticChunker(
        embeddings,
        breakpoint_threshold_type=configuration.chunk_breakpoint_threshold_type,
        breakpoint_threshold_amount=configuration.chunk_breakpoint_threshold_amount,
    )
    
    # Determine documents to process
    document_paths = state.document_paths
    
    # If no document paths provided, use default test PDF
    if not document_paths:
        default_test_pdf = "src_ver2/VH1_DMAIC_1_Introduce_Statistics_Define_Mesure_MBB.pdf"
        if os.path.exists(default_test_pdf):
            document_paths = [default_test_pdf]
            print(f"📋 No documents specified, using default test PDF: {default_test_pdf}")
        else:
            print(f"⚠️ Default test PDF not found: {default_test_pdf}")
            print("📭 No documents to process")
            return {"docs": "delete"}
    
    # Process PDF documents
    if document_paths:
        print(f"📥 Processing {len(document_paths)} PDF document(s)...")
        
        for i, document_path in enumerate(document_paths, 1):
            print(f"  📄 [{i}/{len(document_paths)}] Processing: {document_path}")
            
            if not os.path.exists(document_path):
                print(f"    ⚠️ File not found, skipping: {document_path}")
                continue
            
            # Check if file is PDF
            source_path = Path(document_path)
            if source_path.suffix.lower() != '.pdf':
                print(f"    ⚠️ Not a PDF file, skipping: {source_path.name}")
                continue
                
            try:
                # Copy PDF to knowledge base documents folder
                dest_pdf_path = documents_dir / source_path.name
                
                # Handle filename conflicts by adding suffix
                counter = 1
                original_dest = dest_pdf_path
                while dest_pdf_path.exists():
                    stem = original_dest.stem
                    suffix = original_dest.suffix
                    dest_pdf_path = documents_dir / f"{stem}_{counter}{suffix}"
                    counter += 1
                
                print(f"    📋 Copying PDF: {source_path.name} -> {dest_pdf_path.name}")
                shutil.copy2(source_path, dest_pdf_path)
                
                # Convert PDF to Markdown using pymupdf4llm
                print(f"    🔄 Converting PDF to Markdown...")
                try:
                    markdown_content = pymupdf4llm.to_markdown(str(dest_pdf_path))
                    
                    # Save markdown file
                    markdown_filename = dest_pdf_path.stem + ".md"
                    markdown_path = markdown_dir / markdown_filename
                    
                    with open(markdown_path, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)
                    
                    print(f"    ✅ Markdown saved: {markdown_filename}")
                    
                except Exception as e:
                    print(f"    ❌ PDF conversion failed: {e}")
                    continue
                
                # Create initial document for chunking
                initial_doc = Document(
                    page_content=markdown_content,
                    metadata={
                        "source_pdf": str(dest_pdf_path),
                        "source_markdown": str(markdown_path),
                        "original_path": str(source_path),
                        "knowledge_base": str(kb_path),
                        "file_index": i,
                        "file_type": "pdf",
                        "file_name": dest_pdf_path.name,
                        "markdown_name": markdown_filename
                    }
                )
                
                # Apply semantic chunking
                print(f"    🧩 Applying semantic chunking...")
                try:
                    chunks = semantic_chunker.split_documents([initial_doc])
                    
                    # Enhance each chunk with detailed metadata
                    enhanced_chunks = []
                    for chunk_idx, chunk in enumerate(chunks):
                        # Estimate page number based on content position
                        # This is approximate since pymupdf4llm doesn't preserve exact page info
                        estimated_page = chunk_idx + 1  # Simple estimation
                        
                        enhanced_metadata = {
                            **chunk.metadata,
                            "chunk_index": chunk_idx,
                            "total_chunks": len(chunks),
                            "estimated_page": estimated_page,
                            "chunk_length": len(chunk.page_content),
                            "chunk_start_chars": 0,  # Could be enhanced with actual positions
                        }
                        
                        enhanced_chunk = Document(
                            page_content=chunk.page_content,
                            metadata=enhanced_metadata
                        )
                        enhanced_chunks.append(enhanced_chunk)
                    
                    docs.extend(enhanced_chunks)
                    print(f"    ✅ Created {len(chunks)} semantic chunks")
                    
                except Exception as e:
                    print(f"    ❌ Semantic chunking failed: {e}")
                    # Fallback: use original document as single chunk
                    docs.append(initial_doc)
                    print(f"    ⚠️ Using original document as single chunk")
                        
            except Exception as e:
                print(f"    ❌ Error processing {document_path}: {e}")
                continue
    
    if not docs:
        print("📭 No documents to index")
        return {"docs": "delete"}
    
    try:
        # Initialize LanceDB in knowledge base specific directory
        import lancedb
        from langchain_community.vectorstores import LanceDB
        
        # Connect to knowledge base specific LanceDB with append mode
        vectorstore = LanceDB(
            uri=str(lancedb_dir),
            embedding=embeddings,
            table_name=configuration.table_name,
            mode="append"  # Quan trọng: append thay vì overwrite
        )
        
        # Add documents to vector store
        print(f"🔄 Indexing {len(docs)} document chunks...")
        await vectorstore.aadd_documents(docs)
        
        print(f"✅ Successfully indexed {len(docs)} chunks into {lancedb_dir}")
        print(f"🗂️ Knowledge base: {kb_path}")
        print(f"📊 Chunk statistics:")
        
        # Print some statistics
        total_chunks = len(docs)
        avg_chunk_length = sum(len(doc.page_content) for doc in docs) / total_chunks
        unique_files = len(set(doc.metadata.get('file_name', '') for doc in docs))
        
        print(f"   📄 Unique PDFs processed: {unique_files}")
        print(f"   🧩 Total chunks created: {total_chunks}")
        print(f"   📏 Average chunk length: {avg_chunk_length:.0f} characters")
        
    except Exception as e:
        print(f"❌ Error indexing documents: {e}")
        return {"docs": "delete"}
    
    return {"docs": "delete"}


# Create graph
builder = StateGraph(IndexState, config_schema=IndexConfiguration)
builder.add_node("index_docs", index_docs)
builder.add_edge(START, "index_docs")
builder.add_edge("index_docs", END)

# Compile graph
graph = builder.compile()
graph.name = "PDFIndexGraph"

if __name__ == "__main__":
    print("📊 PDF Index Graph created successfully!")
    print("📚 Features:")
    print("  - PDF-only document processing")
    print("  - pymupdf4llm PDF → Markdown conversion")
    print("  - Semantic chunking with LangChain")
    print("  - Enhanced metadata with page information")
    print("  - Knowledge base specific LanceDB storage")
    print("💡 Use 'langgraph dev' to test graph")
