# LangChain-Essentials

A comprehensive learning repository showcasing the core components and patterns of LangChain framework for building applications with Large Language Models (LLMs).

## Overview

This project systematically covers the essential building blocks of LangChain, including prompt engineering, output parsing, LCEL (LangChain Expression Language) chains, RAG (Retrieval-Augmented Generation), and chat models. It serves as both a learning resource and a practical reference for implementing LangChain-based applications.

## Project Structure

```
LangChain-Essentials/
├── env.py                      # Environment configuration
├── ChatModel/                  # Chat model implementations
│   ├── app.py                 # Chat application entry point
│   └── message.py             # Message handling
├── LCEL/                      # LangChain Expression Language
│   ├── LCEL_Chain.py          # LCEL chain implementations
│   └── notes.txt              # LCEL concepts and notes
├── OutputParser/              # Output parsing strategies
│   ├── CommaSeparatedList.py  # Comma-separated list parser
│   ├── JsonOutputParser.py    # JSON output parser
│   ├── PydanticOutputParser.py# Pydantic model parser
│   ├── StrOutputParser.py     # String output parser
│   └── structured_output.py   # Structured output handling
├── PromptTemplate/            # Prompt engineering
│   ├── BasicPromptTemplate.py # Basic prompt templates
│   └── ChatPromptTemplate.py  # Chat-specific prompts
└── RAG/                       # Retrieval-Augmented Generation
    ├── data.txt               # Sample data for RAG
    └── loadSplit.py           # Document loading and splitting
```

## Components

### ChatModel
Implementations of chat-based LLM interactions, including message formatting and conversation management.

### LCEL (LangChain Expression Language)
Core examples of building composable chains using LangChain's expression language for creating workflows with LLMs.

### OutputParser
Various strategies for parsing and structuring LLM outputs:
- **CSV/List formats** - Parse comma-separated outputs
- **JSON** - Extract and validate JSON structures
- **Pydantic** - Type-safe output with data models
- **String** - Simple text output handling

### PromptTemplate
Prompt engineering techniques:
- Basic template construction and variable substitution
- Chat-specific prompt formatting

### RAG
Retrieval-Augmented Generation implementation:
- Document loading and processing
- Text splitting strategies
- Integration with retrieval systems

## Getting Started

### Prerequisites
- Python 3.8+
- LangChain library
- Required API keys (OpenAI, etc.) in environment variables

### Installation

1. Clone the repository
2. Set up environment configuration in `env.py`
3. Install dependencies:
   ```bash
   pip install langchain openai python-dotenv
   ```

### Usage

Each module can be run independently. For example:

```bash
# Run chat model example
python ChatModel/app.py

# Run LCEL chain example
python LCEL/LCEL_Chain.py

# Run output parser examples
python OutputParser/JsonOutputParser.py
```

## Key Concepts

- **Prompts**: Structured inputs to guide LLM behavior
- **Chains**: Composable sequences of operations using LCEL
- **Parsers**: Extract structured data from LLM outputs
- **RAG**: Enhance LLM responses with external knowledge
- **Chat Models**: Interactive dialogue with LLMs

## Learning Path

1. Start with `PromptTemplate/` to understand prompt engineering
2. Explore `OutputParser/` to learn output structuring
3. Study `LCEL/` for building composable chains
4. Implement `ChatModel/` for interactive applications
5. Integrate `RAG/` for knowledge-augmented responses

## Notes

- Check `LCEL/notes.txt` for detailed LCEL concepts
- Refer to individual module comments for implementation details
- Adapt examples to your use case and API providers

## License

This project is for educational purposes.

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
