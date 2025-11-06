"""
Utility functions for document processing
"""
import re
from typing import List


def remove_extra_whitespace(text: str) -> str:
    """Remove extra whitespace from text"""
    # Replace multiple spaces with single space
    text = re.sub(r' +', ' ', text)
    # Replace multiple newlines with double newline
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def extract_code_blocks(text: str) -> List[str]:
    """
    Extract code blocks from markdown
    
    Returns:
        List of code blocks (without fence markers)
    """
    pattern = r'```[\w]*\n(.*?)\n```'
    return re.findall(pattern, text, re.DOTALL)


def is_likely_code(text: str) -> bool:
    """
    Heuristic to detect if text is code
    
    Checks for common code patterns like indentation,
    semicolons, brackets, etc.
    """
    indicators = [
        text.count('{') > 2,
        text.count(';') > 3,
        text.count('def ') > 0,
        text.count('class ') > 0,
        text.count('import ') > 0,
        text.startswith('    '),  # Indented
    ]
    return sum(indicators) >= 2

