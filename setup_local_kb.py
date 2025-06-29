#!/usr/bin/env python3
"""
Setup script để chuẩn bị Local Knowledge Base với LanceDB
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))


def setup_environment():
    """Setup environment variables"""
    print("🔧 Setting up environment...")
    
    # Create .env file if not exists
    env_file = Path(".env")
    if not env_file.exists():
        env_content = """# RAG Provider - Use local knowledge base
RAG_PROVIDER=local_kb

# Local Knowledge Base Settings  
LOCAL_KB_MAX_RESULTS=10
EMBEDDING_MODEL=nomic-embed-text

# Search API
SEARCH_API=duckduckgo

# Add your LLM API keys here
# OPENAI_API_KEY=your_key_here
# ANTHROPIC_API_KEY=your_key_here
"""
        env_file.write_text(env_content)
        print("✅ Created .env file with default configuration")
    else:
        print("✅ .env file already exists")


def setup_knowledge_base_structure():
    """Create knowledge base directory structure"""
    print("📁 Setting up knowledge base structure...")
    
    appdata_dir = Path("appdata")
    kb_test_dir = appdata_dir / "knowledge_base_test"
    
    # Create directories
    for dir_path in [
        kb_test_dir,
        kb_test_dir / "documents", 
        kb_test_dir / "markdown",
        kb_test_dir / "lancedb"
    ]:
        dir_path.mkdir(parents=True, exist_ok=True)
    
    print(f"✅ Created directory structure at {appdata_dir}")
    
    # Create/update metadata
    metadata_file = kb_test_dir / "metadata.json"
    if not metadata_file.exists():
        metadata = {
            "id": "knowledge_base_test",
            "name": "Knowledge Base Test",
            "description": "Test knowledge base với các tài liệu mẫu cho demo",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "document_count": len(list((kb_test_dir / "documents").glob("*.pdf")))
        }
        
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print("✅ Created metadata.json")
    else:
        print("✅ metadata.json already exists")


def create_sample_knowledge_base():
    """Create a sample knowledge base for testing"""
    print("📚 Creating sample knowledge base...")
    
    from src.knowledge_base import LocalKnowledgeBaseProvider
    
    provider = LocalKnowledgeBaseProvider()
    
    # Create a sample KB if none exist
    kbs = provider.get_knowledge_bases()
    if not kbs:
        kb_id = provider.create_knowledge_base(
            "Demo Knowledge Base",
            "Demo knowledge base for testing DeerFlow local RAG"
        )
        print(f"✅ Created sample knowledge base: {kb_id}")
    else:
        print(f"✅ Found {len(kbs)} existing knowledge bases")


def check_dependencies():
    """Check required dependencies"""
    print("🔍 Checking dependencies...")
    
    missing_deps = []
    
    try:
        import lancedb
        print("✅ LanceDB installed")
    except ImportError:
        missing_deps.append("lancedb")
    
    try:
        from langchain_community.vectorstores import LanceDB
        print("✅ LangChain LanceDB integration available")
    except ImportError:
        missing_deps.append("langchain-community")
    
    try:
        from langchain_ollama import OllamaEmbeddings
        print("✅ Ollama embeddings available")
    except ImportError:
        missing_deps.append("langchain-ollama")
    
    if missing_deps:
        print(f"❌ Missing dependencies: {', '.join(missing_deps)}")
        print("Install with: uv add " + " ".join(missing_deps))
        return False
    
    return True


def check_ollama():
    """Check if Ollama is running and has required model"""
    print("🤖 Checking Ollama...")
    
    try:
        import requests
        
        # Check if Ollama is running
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get("models", [])
            model_names = [model["name"] for model in models]
            
            print(f"✅ Ollama is running with {len(models)} models")
            
            # Check for embedding model
            embedding_model = os.getenv("EMBEDDING_MODEL", "nomic-embed-text")
            if any(embedding_model in name for name in model_names):
                print(f"✅ Embedding model '{embedding_model}' is available")
            else:
                print(f"⚠️  Embedding model '{embedding_model}' not found")
                print(f"📥 Install with: ollama pull {embedding_model}")
                
        else:
            print("❌ Ollama is not responding")
            
    except Exception as e:
        print(f"❌ Cannot connect to Ollama: {e}")
        print("💡 Make sure Ollama is installed and running:")
        print("   curl -fsSL https://ollama.ai/install.sh | sh")
        print("   ollama serve")


def main():
    """Main setup function"""
    print("🚀 Setting up DeerFlow Local Knowledge Base")
    print("=" * 50)
    
    # Setup environment
    setup_environment()
    
    # Check dependencies
    if not check_dependencies():
        print("\n❌ Please install missing dependencies first")
        return
    
    # Check Ollama
    check_ollama()
    
    # Setup directory structure
    setup_knowledge_base_structure()
    
    # Create sample KB
    try:
        create_sample_knowledge_base()
    except Exception as e:
        print(f"⚠️  Could not create sample knowledge base: {e}")
    
    print("\n✅ Setup completed!")
    print("\n🎯 Next steps:")
    print("1. Start backend: uv run python server.py")
    print("2. Start frontend: cd web && pnpm dev")
    print("3. Test with: uv run python test_local_kb.py")
    print("4. Visit: http://localhost:3000/knowledge-base")
    
    print("\n💡 Configuration:")
    print(f"  - Knowledge bases location: {Path('appdata').absolute()}")
    print(f"  - RAG Provider: local_kb")
    print(f"  - Embedding model: {os.getenv('EMBEDDING_MODEL', 'nomic-embed-text')}")


if __name__ == "__main__":
    main() 