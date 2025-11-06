# DocPrep

**Document preprocessing for RAG systems** - chunk, embed, and prepare documents for retrieval-augmented generation.

## Purpose

This is a **realistic test project** for dotagent testing. It's a Python library that helps prepare documents for RAG (Retrieval-Augmented Generation) systems.

## Features

- 📄 **Smart Chunking** - Split documents by sentences, paragraphs, or semantic boundaries
- 🔢 **Token Counting** - Accurate token counts for different LLM models
- 🎯 **Metadata Extraction** - Extract titles, headers, and structure
- 💾 **Embedding Cache** - Cache embeddings to avoid recomputation
- 🔍 **Overlap Management** - Configurable chunk overlap for better retrieval

## Known Issues

1. **Chunking breaks on code blocks** - Bug in `docprep/chunker.py:45` - doesn't preserve code formatting
2. **Token counter inaccurate for GPT-4** - Wrong tokenizer in `docprep/tokens.py:28`
3. **Memory leak in embedding cache** - Cache never evicts old entries in `docprep/cache.py:56`
4. **Markdown headers not extracted** - Parser misses H2/H3 headers in `docprep/parser.py:89`

## TODOs

- [ ] Add support for PDF parsing (currently only text/markdown)
- [ ] Implement semantic chunking using embeddings
- [ ] Add async support for batch processing
- [ ] Support custom tokenizers
- [ ] Add chunk deduplication
- [ ] Implement sliding window with overlap
- [ ] Add support for structured data (JSON, CSV)

## Installation

```bash
pip install -e .
pip install -r requirements-dev.txt  # for development
```

## Quick Start

```python
from docprep import DocumentChunker, TokenCounter

# Chunk a document
chunker = DocumentChunker(chunk_size=512, overlap=50)
chunks = chunker.chunk_text(document_text)

# Count tokens
counter = TokenCounter(model="gpt-3.5-turbo")
tokens = counter.count(text)
```

## Project Structure

```
docprep/
├── chunker.py          # Document chunking (has code block bug)
├── tokens.py           # Token counting (wrong tokenizer)
├── parser.py           # Metadata extraction (missing headers)
├── cache.py            # Embedding cache (memory leak)
├── embeddings.py       # Embedding generation
└── utils.py            # Helper functions
```

## Testing Dotagent

This project provides realistic AI/ML scenarios:

1. **/issues_report** - Report code block chunking bug
2. **/tasks_add** - Add PDF parsing TODO
3. **/issues_log_gap** - Log missing semantic chunking
4. **/ideas_brainstorm** - Brainstorm async batch processing
5. **/sessions_summarize** - Summarize development sessions
6. **/git_status** - Check project changes

## Development

```bash
# Run tests
pytest tests/

# Format code
black docprep/

# Type checking
mypy docprep/
```

## License

MIT License - This is a test project for dotagent validation.
