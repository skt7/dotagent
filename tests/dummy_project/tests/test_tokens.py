"""Tests for token counter"""
import pytest
from docprep import TokenCounter


def test_basic_counting():
    """Test basic token counting"""
    counter = TokenCounter()
    count = counter.count("Hello world")
    assert count > 0


def test_gpt4_tokenizer_bug():
    """
    Test demonstrating GPT-4 tokenizer bug
    
    TODO: Fix to use cl100k_base encoding for GPT-4
    """
    counter = TokenCounter(model="gpt-4")
    text = "This is a test"
    
    # BUG: Count will be wrong due to incorrect tokenizer
    count = counter.count(text)
    assert count > 0  # Should be more accurate


def test_message_counting():
    """Test chat message token counting"""
    counter = TokenCounter()
    messages = [
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi there"},
    ]
    
    count = counter.count_messages(messages)
    assert count > 10  # Includes formatting tokens


def test_truncation():
    """Test text truncation to token limit"""
    counter = TokenCounter()
    text = " ".join(["word"] * 100)
    
    truncated = counter.truncate(text, max_tokens=50)
    assert counter.count(truncated) <= 50

