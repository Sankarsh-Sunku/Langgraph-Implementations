
# Langgraph Implementations AI Projects

This repository contains multiple projects demonstrating the use of LangChain, LangGraph, and related tools for building AI agents, chatbots, and state-based applications. Each folder represents a specific project with its own purpose and implementation.

---

## Folder Structure

### 1. **BasicReflectionAgent**
This project implements a reflection-based agent that generates and critiques Twitter posts.

- **Files:**
  - `chains.py`: Defines the generation and reflection chains using LangChain prompts.
  - `graphs.py`: Implements a `MessageGraph` to manage the flow between generation and reflection nodes.
  - `.env`: Contains environment variables like API keys.

- **Key Features:**
  - Generates Twitter posts based on user input.
  - Critiques and provides recommendations for improving the generated posts.

---

### 2. **ChatBot**
This folder contains various chatbot implementations with different features like memory, tools, and SQLite-based persistence.

- **Files:**
  - `basicChatBot.py`: A simple chatbot without memory.
  - `ChatBotWithMemory.py`: A chatbot with in-memory conversation history.
  - `ChatBotWithSqqliteMemory.py`: A chatbot with SQLite-based memory persistence.
  - `ChatBotWithTools.py`: A chatbot integrated with external tools like TavilySearchResults.
  - `.env`: Contains environment variables like API keys.

- **Key Features:**
  - Basic chatbot functionality.
  - Memory-enabled chatbots for maintaining conversation context.
  - Tool integration for enhanced responses.
  - SQLite-based persistence for saving conversation states.

---

### 3. **introduction**
This folder contains a basic implementation of a ReAct agent.

- **Files:**
  - `basic_reAct_agent.py`: Demonstrates a zero-shot ReAct agent using LangChain and tools like TavilySearchResults.
  - `.env`: Contains environment variables like API keys.

- **Key Features:**
  - Uses LangChain's `initialize_agent` to create a ReAct agent.
  - Includes tools for fetching system time and performing searches.

---

### 4. **ReActAgentUsingLanggraph**
This folder contains an advanced implementation of a ReAct agent using LangGraph.

- **Files:**
  - `agentReasonRunnable.py`: Defines the tools and the ReAct agent runnable.
  - `graphs.py`: Implements a `StateGraph` for managing the reasoning and acting phases of the agent.
  - `reactStateSchema.py`: Defines the schema for the agent's state.
  - `.env`: Contains environment variables like API keys.

- **Key Features:**
  - Implements a reasoning and acting loop using LangGraph.
  - Supports tool execution and intermediate steps tracking.

---

### 5. **ReflexionAgent**
This folder contains a Reflexion-based agent that iteratively improves its answers.

- **Files:**
  - `chains.py`: Defines the first responder and revisor chains using LangChain prompts.
  - `execute_tools.py`: Implements tool execution logic for the agent.
  - `graphs.py`: Implements a `MessageGraph` for managing the agent's flow.
  - `schema.py`: Defines the schema for the agent's answers and reflections.
  - `.env`: Contains environment variables like API keys.

- **Key Features:**
  - Generates initial answers and critiques them.
  - Revises answers based on reflections and external tool results.

---

### 6. **StateGraph**
This folder demonstrates the use of LangGraph's `StateGraph` for state-based applications.

- **Files:**
  - `basic_state.py`: Implements a simple state graph for incrementing a counter.
  - `complex_state.py`: Implements a more complex state graph with additional state properties like history and sum.

- **Key Features:**
  - Demonstrates state-based logic using LangGraph.
  - Includes conditional transitions and state updates.

---

### 7. **StructuredOutputsForLLM**
This folder demonstrates the use of structured outputs with LangChain.

- **Files:**
  - `notebook.ipynb`: A Jupyter notebook showcasing structured outputs using Pydantic models and JSON schemas.
  - `.env`: Contains environment variables like API keys.

- **Key Features:**
  - Uses Pydantic models to define structured outputs.
  - Demonstrates JSON schema-based output validation.

---

## Environment Variables

Each folder contains a `.env` file with the following keys:
- `GROQ_API_KEY`: API key for ChatGroq.
- `LANGSMITH_TRACING`: Enables tracing for LangSmith.
- `LANGSMITH_ENDPOINT`: Endpoint for LangSmith API.
- `LANGSMITH_API_KEY`: API key for LangSmith.
- `LANGSMITH_PROJECT`: Project name for LangSmith.
- `TAVILY_API_KEY`: API key for TavilySearchResults.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
