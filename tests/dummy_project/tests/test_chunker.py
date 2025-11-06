"""Tests for document chunker"""
import pytest
from docprep import DocumentChunker, ChunkStrategy


def test_sentence_chunking():
    """Test basic sentence-based chunking"""
    chunker = DocumentChunker(chunk_size=20, strategy=ChunkStrategy.SENTENCE)
    text = "This is sentence one. This is sentence two. This is sentence three."
    
    chunks = chunker.chunk_text(text)
    assert len(chunks) > 0
    assert all(isinstance(c, str) for c in chunks)


def test_paragraph_chunking():
    """Test paragraph-based chunking"""
    chunker = DocumentChunker(chunk_size=50, strategy=ChunkStrategy.PARAGRAPH)
    text = "Paragraph one.\n\nParagraph two.\n\nParagraph three."
    
    chunks = chunker.chunk_text(text)
    assert len(chunks) >= 1


def test_code_block_bug():
    """
    Test demonstrating the code block bug
    
    TODO: Fix chunker to preserve code block formatting
    """
    chunker = DocumentChunker(chunk_size=30, strategy=ChunkStrategy.SENTENCE)
    text = """Here is some code:

```python
def hello():
    print("world")
```

The code above demonstrates the bug."""
    
    chunks = chunker.chunk_text(text)
    # BUG: Code formatting is destroyed by sentence chunking
    # This test will fail after fix
    assert len(chunks) > 0


def test_semantic_chunking_not_implemented():
    """Semantic chunking should raise NotImplementedError"""
    chunker = DocumentChunker(strategy=ChunkStrategy.SEMANTIC)
    
    with pytest.raises(NotImplementedError):
        chunker.chunk_text("Some text")

