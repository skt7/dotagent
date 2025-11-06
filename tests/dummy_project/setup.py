"""
DocPrep - Document preprocessing for RAG systems
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="docprep",
    version="0.3.0",
    author="AI Team",
    author_email="ai@example.com",
    description="Document preprocessing for RAG systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/example/docprep",
    packages=find_packages(exclude=["tests*", "examples*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=[
        "tiktoken>=0.5.0",
        "numpy>=1.24.0",
        "openai>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "mypy>=1.5.0",
            "ruff>=0.1.0",
        ],
        "pdf": [
            "pypdf2>=3.0.0",  # TODO: Add when PDF support implemented
        ],
    },
)
