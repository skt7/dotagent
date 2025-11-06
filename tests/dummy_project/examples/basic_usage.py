"""
Basic usage example for DocPrep library
"""
from docprep import DocumentChunker, TokenCounter, DocumentParser, ChunkStrategy


def main():
    # Example document
    doc = """
# Introduction to RAG

Retrieval-Augmented Generation (RAG) is a technique that enhances LLMs.

## How It Works

RAG systems retrieve relevant documents and include them in prompts.

```python
def rag_query(question, documents):
    relevant = retrieve(question, documents)
    return llm.generate(question, context=relevant)
```

## Benefits

- Reduces hallucinations
- Provides source attribution
- Enables domain-specific knowledge
"""

    # 1. Parse document metadata
    parser = DocumentParser()
    metadata = parser.parse(doc, format="markdown")
    print(f"Title: {metadata.title}")
    print(f"Headers: {metadata.headers}")
    print(f"Has code: {metadata.has_code}")
    
    # 2. Chunk document
    chunker = DocumentChunker(
        chunk_size=100,
        overlap=20,
        strategy=ChunkStrategy.SENTENCE
    )
    chunks = chunker.chunk_text(doc)
    print(f"\nCreated {len(chunks)} chunks")
    
    # 3. Count tokens
    counter = TokenCounter(model="gpt-3.5-turbo")
    for i, chunk in enumerate(chunks):
        tokens = counter.count(chunk)
        print(f"Chunk {i+1}: {tokens} tokens")
        

if __name__ == "__main__":
    main()

