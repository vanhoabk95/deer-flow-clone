# Copyright (c) 2025 Bytedance Ltd. and/or its affiliates
# SPDX-License-Identifier: MIT

import os
from urllib.parse import urlparse


def get_content_type(file_ext: str) -> str:
    """Get MIME type from file extension."""
    content_types = {
        '.pdf': 'application/pdf',
        '.doc': 'application/msword',
        '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        '.txt': 'text/plain',
        '.md': 'text/markdown',
        '.html': 'text/html',
        '.htm': 'text/html',
        '.csv': 'text/csv',
        '.json': 'application/json',
        '.xml': 'application/xml'
    }
    return content_types.get(file_ext, 'application/octet-stream')


def parse_kb_uri(uri: str) -> str | None:
    """Parse knowledge base URI to extract KB ID."""
    try:
        parsed = urlparse(uri)
        if parsed.scheme == "kb":
            return parsed.netloc or parsed.path.strip("/")
    except Exception:
        pass
    return None


def count_documents(kb_path: str) -> int:
    """Count documents in knowledge base."""
    docs_path = os.path.join(kb_path, "documents")
    if os.path.exists(docs_path):
        return len([
            f for f in os.listdir(docs_path) 
            if os.path.isfile(os.path.join(docs_path, f)) and not f.startswith('.')
        ])
    return 0


def setup_kb_directories(kb_path: str) -> None:
    """Create knowledge base directory structure."""
    directories = ["documents", "markdown", "lancedb"]
    for directory in directories:
        os.makedirs(os.path.join(kb_path, directory), exist_ok=True) 