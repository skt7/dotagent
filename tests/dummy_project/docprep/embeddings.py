"""
Embedding generation wrapper
"""
from typing import List, Optional
import numpy as np
from openai import OpenAI

from .cache import EmbeddingCache


class EmbeddingGenerator:
    """Generate embeddings with caching"""
    
    def __init__(
        self,
        model: str = "text-embedding-ada-002",
        use_cache: bool = True,
        api_key: Optional[str] = None
    ):
        """
        Initialize embedding generator
        
        Args:
            model: OpenAI embedding model name
            use_cache: Whether to cache embeddings
            api_key: OpenAI API key (uses env var if None)
        """
        self.model = model
        self.client = OpenAI(api_key=api_key)
        self.cache = EmbeddingCache() if use_cache else None
        
    def embed(self, text: str) -> np.ndarray:
        """
        Generate embedding for text
        
        Args:
            text: Input text
            
        Returns:
            Embedding vector as numpy array
        """
        # Check cache first
        if self.cache:
            cached = self.cache.get(text)
            if cached is not None:
                return cached
                
        # Generate embedding
        response = self.client.embeddings.create(
            model=self.model,
            input=text
        )
        
        embedding = np.array(response.data[0].embedding)
        
        # Cache result
        if self.cache:
            self.cache.put(text, embedding)
            
        return embedding
        
    def embed_batch(self, texts: List[str]) -> List[np.ndarray]:
        """
        Generate embeddings for multiple texts
        
        Args:
            texts: List of input texts
            
        Returns:
            List of embedding vectors
            
        TODO: Implement true batch processing (currently just loops)
        TODO: Add async support for better performance
        """
        # FIXME: This should batch API calls, not call one by one
        return [self.embed(text) for text in texts]
        
    def similarity(self, text1: str, text2: str) -> float:
        """
        Calculate cosine similarity between two texts
        
        Args:
            text1: First text
            text2: Second text
            
        Returns:
            Similarity score (0-1)
        """
        emb1 = self.embed(text1)
        emb2 = self.embed(text2)
        
        # Cosine similarity
        return float(np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2)))

