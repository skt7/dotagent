"""
Document parsing and metadata extraction
"""
import re
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class DocumentMetadata:
    """Metadata extracted from document"""
    title: Optional[str] = None
    headers: List[str] = None
    word_count: int = 0
    has_code: bool = False
    language: Optional[str] = None
    
    def __post_init__(self):
        if self.headers is None:
            self.headers = []


class DocumentParser:
    """Extract structure and metadata from documents"""
    
    def __init__(self):
        self.metadata = DocumentMetadata()
        
    def parse(self, text: str, format: str = "markdown") -> DocumentMetadata:
        """
        Parse document and extract metadata
        
        Args:
            text: Document text
            format: Document format (markdown, text, html)
            
        Returns:
            DocumentMetadata object
        """
        if format == "markdown":
            return self._parse_markdown(text)
        elif format == "text":
            return self._parse_text(text)
        else:
            # TODO: Add HTML parsing support
            raise NotImplementedError(f"Format {format} not supported")
            
    def _parse_markdown(self, text: str) -> DocumentMetadata:
        """Parse markdown document"""
        metadata = DocumentMetadata()
        
        # Extract title (first H1)
        h1_match = re.search(r'^#\s+(.+)$', text, re.MULTILINE)
        if h1_match:
            metadata.title = h1_match.group(1).strip()
            
        # Extract headers
        # BUG: This only gets H1 headers, misses H2/H3!
        h1_headers = re.findall(r'^#\s+(.+)$', text, re.MULTILINE)
        metadata.headers = h1_headers  # FIXME: Should include all header levels
        
        # Check for code blocks
        metadata.has_code = '```' in text or '    ' in text
        
        # Word count
        # FIXME: This includes code blocks in word count
        metadata.word_count = len(text.split())
        
        return metadata
        
    def _parse_text(self, text: str) -> DocumentMetadata:
        """Parse plain text document"""
        metadata = DocumentMetadata()
        
        # Try to extract title from first line if it looks like a title
        lines = text.split('\n')
        if lines and len(lines[0]) < 100 and lines[0].isupper():
            metadata.title = lines[0].strip()
            
        metadata.word_count = len(text.split())
        metadata.has_code = False
        
        return metadata
        
    def extract_sections(self, text: str) -> Dict[str, str]:
        """
        Split document into sections by headers
        
        Returns:
            Dictionary mapping header names to section content
            
        TODO: Implement proper section extraction
        TODO: Handle nested sections (H2 under H1, etc.)
        """
        # Placeholder implementation
        sections = {}
        current_header = "Introduction"
        current_content = []
        
        for line in text.split('\n'):
            if line.startswith('#'):
                if current_content:
                    sections[current_header] = '\n'.join(current_content)
                current_header = line.lstrip('#').strip()
                current_content = []
            else:
                current_content.append(line)
                
        if current_content:
            sections[current_header] = '\n'.join(current_content)
            
        return sections

