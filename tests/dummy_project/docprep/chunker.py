"""
Document chunking with multiple strategies
"""
from enum import Enum
from typing import List, Optional
import re


class ChunkStrategy(Enum):
    """Chunking strategies"""
    SENTENCE = "sentence"
    PARAGRAPH = "paragraph"
    FIXED = "fixed"
    SEMANTIC = "semantic"  # TODO: Implement semantic chunking


class DocumentChunker:
    """Chunk documents into smaller pieces for RAG"""
    
    def __init__(
        self,
        chunk_size: int = 512,
        overlap: int = 50,
        strategy: ChunkStrategy = ChunkStrategy.SENTENCE
    ):
        """
        Initialize chunker
        
        Args:
            chunk_size: Target size in tokens
            overlap: Number of tokens to overlap between chunks
            strategy: Chunking strategy to use
        """
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.strategy = strategy
        
    def chunk_text(self, text: str) -> List[str]:
        """
        Chunk text according to strategy
        
        Args:
            text: Input text to chunk
            
        Returns:
            List of text chunks
        """
        if self.strategy == ChunkStrategy.SENTENCE:
            return self._chunk_by_sentence(text)
        elif self.strategy == ChunkStrategy.PARAGRAPH:
            return self._chunk_by_paragraph(text)
        elif self.strategy == ChunkStrategy.FIXED:
            return self._chunk_fixed_size(text)
        elif self.strategy == ChunkStrategy.SEMANTIC:
            # TODO: Implement semantic chunking using embeddings
            raise NotImplementedError("Semantic chunking not yet implemented")
            
    def _chunk_by_sentence(self, text: str) -> List[str]:
        """Chunk by sentence boundaries"""
        # BUG: This breaks on code blocks!
        # It treats code as sentences, destroying formatting
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        chunks = []
        current_chunk = []
        current_size = 0
        
        for sentence in sentences:
            sentence_size = len(sentence.split())  # Rough token estimate
            
            if current_size + sentence_size > self.chunk_size and current_chunk:
                chunks.append(' '.join(current_chunk))
                # Apply overlap
                overlap_sentences = current_chunk[-2:] if len(current_chunk) >= 2 else current_chunk
                current_chunk = overlap_sentences
                current_size = sum(len(s.split()) for s in current_chunk)
                
            current_chunk.append(sentence)
            current_size += sentence_size
            
        if current_chunk:
            chunks.append(' '.join(current_chunk))
            
        return chunks
        
    def _chunk_by_paragraph(self, text: str) -> List[str]:
        """Chunk by paragraph boundaries"""
        paragraphs = text.split('\n\n')
        
        chunks = []
        current_chunk = []
        current_size = 0
        
        for para in paragraphs:
            para_size = len(para.split())
            
            if current_size + para_size > self.chunk_size and current_chunk:
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = []
                current_size = 0
                
            current_chunk.append(para)
            current_size += para_size
            
        if current_chunk:
            chunks.append('\n\n'.join(current_chunk))
            
        return chunks
        
    def _chunk_fixed_size(self, text: str) -> List[str]:
        """Chunk by fixed character size"""
        words = text.split()
        chunks = []
        current_chunk = []
        current_size = 0
        
        for word in words:
            current_size += 1
            current_chunk.append(word)
            
            if current_size >= self.chunk_size:
                chunks.append(' '.join(current_chunk))
                # FIXME: Overlap not properly implemented here
                current_chunk = []
                current_size = 0
                
        if current_chunk:
            chunks.append(' '.join(current_chunk))
            
        return chunks

