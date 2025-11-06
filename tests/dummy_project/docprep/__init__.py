"""
DocPrep - Document preprocessing for RAG systems

Provides utilities for chunking, tokenizing, and preparing
documents for retrieval-augmented generation.
"""

__version__ = "0.3.0"

from .chunker import DocumentChunker, ChunkStrategy
from .tokens import TokenCounter
from .parser import DocumentParser
from .embeddings import EmbeddingGenerator
from .cache import EmbeddingCache

__all__ = [
    "DocumentChunker",
    "ChunkStrategy",
    "TokenCounter",
    "DocumentParser",
    "EmbeddingGenerator",
    "EmbeddingCache",
]

