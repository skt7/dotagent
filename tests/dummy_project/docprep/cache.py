"""
Embedding cache to avoid recomputation
"""
import hashlib
from typing import Optional, List
import numpy as np


class EmbeddingCache:
    """Cache embeddings to avoid redundant API calls"""
    
    def __init__(self, max_size: int = 10000):
        """
        Initialize cache
        
        Args:
            max_size: Maximum number of cached embeddings
        """
        self.max_size = max_size
        self._cache: dict[str, np.ndarray] = {}
        self._access_count: dict[str, int] = {}
        
    def _hash_text(self, text: str) -> str:
        """Generate hash for text"""
        return hashlib.sha256(text.encode()).hexdigest()
        
    def get(self, text: str) -> Optional[np.ndarray]:
        """
        Get cached embedding for text
        
        Args:
            text: Input text
            
        Returns:
            Cached embedding or None if not found
        """
        key = self._hash_text(text)
        if key in self._cache:
            self._access_count[key] = self._access_count.get(key, 0) + 1
            return self._cache[key]
        return None
        
    def put(self, text: str, embedding: np.ndarray) -> None:
        """
        Cache an embedding
        
        Args:
            text: Input text
            embedding: Embedding vector
        """
        key = self._hash_text(text)
        
        # BUG: Memory leak! Cache never evicts old entries!
        # When cache exceeds max_size, we should evict LRU items
        # Currently just keeps growing indefinitely
        if len(self._cache) >= self.max_size:
            # FIXME: Should implement LRU eviction here
            pass  # Just ignore for now (wrong!)
            
        self._cache[key] = embedding
        self._access_count[key] = 0
        
    def clear(self) -> None:
        """Clear all cached embeddings"""
        self._cache.clear()
        self._access_count.clear()
        
    def size(self) -> int:
        """Get number of cached items"""
        return len(self._cache)
        
    def hit_rate(self) -> float:
        """
        Calculate cache hit rate
        
        TODO: Track hits and misses properly
        """
        # Placeholder - not tracking hits/misses correctly
        return 0.0

