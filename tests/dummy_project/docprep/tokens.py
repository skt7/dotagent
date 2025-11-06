"""
Token counting for different LLM models
"""
from typing import Optional
import tiktoken


class TokenCounter:
    """Count tokens for different LLM models"""
    
    def __init__(self, model: str = "gpt-3.5-turbo"):
        """
        Initialize token counter
        
        Args:
            model: Model name (gpt-3.5-turbo, gpt-4, etc.)
        """
        self.model = model
        self._encoding = None
        self._load_encoding()
        
    def _load_encoding(self):
        """Load tokenizer encoding for model"""
        try:
            # BUG: This uses wrong encoding for GPT-4!
            # GPT-4 needs "cl100k_base" but this always uses "gpt2"
            if "gpt-4" in self.model:
                # FIXME: This is incorrect, should use cl100k_base
                self._encoding = tiktoken.get_encoding("gpt2")
            elif "gpt-3.5" in self.model:
                self._encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
            else:
                self._encoding = tiktoken.get_encoding("cl100k_base")
        except Exception as e:
            print(f"Warning: Could not load encoding, using cl100k_base: {e}")
            self._encoding = tiktoken.get_encoding("cl100k_base")
            
    def count(self, text: str) -> int:
        """
        Count tokens in text
        
        Args:
            text: Input text
            
        Returns:
            Number of tokens
        """
        if not self._encoding:
            return len(text.split())  # Fallback to word count
            
        return len(self._encoding.encode(text))
        
    def count_messages(self, messages: list[dict]) -> int:
        """
        Count tokens in chat messages format
        
        Args:
            messages: List of message dicts with 'role' and 'content'
            
        Returns:
            Total token count including message formatting
        """
        # Approximate token count for messages
        # Each message adds ~4 tokens for formatting
        total = 0
        for message in messages:
            total += self.count(message.get('content', ''))
            total += 4  # Message formatting tokens
            
        total += 2  # Assistant reply priming
        return total
        
    def truncate(self, text: str, max_tokens: int) -> str:
        """
        Truncate text to fit within token limit
        
        Args:
            text: Input text
            max_tokens: Maximum number of tokens
            
        Returns:
            Truncated text
            
        TODO: Add support for truncating from middle (keep start and end)
        TODO: Add smart truncation at sentence boundaries
        """
        if not self._encoding:
            words = text.split()
            return ' '.join(words[:max_tokens])
            
        tokens = self._encoding.encode(text)
        if len(tokens) <= max_tokens:
            return text
            
        truncated_tokens = tokens[:max_tokens]
        return self._encoding.decode(truncated_tokens)

