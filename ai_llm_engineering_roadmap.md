# AI / LLM Engineering Roadmap
## From Senior Software Engineer to AI Engineer

**Environment:** Ubuntu Linux · Python · React/TypeScript · Local LLMs · AI Agents

**Hardware:** AMD Ryzen 5 9600X · NVIDIA RTX 5060 Ti 16GB · 2TB NVMe SSD · 64GB RAM if both 32GB kits are installed

**Goal:** Build production-style AI applications, learn LLM engineering, develop backend agents, stream responses, use tools and handoffs, implement RAG, and prepare for AI engineering interviews.

---

## 1. What You Will Learn

By the end of this roadmap, you should be able to:

- Run LLMs locally on your NVIDIA GPU.
- Understand tokens, context windows, embeddings, transformers, and inference.
- Build AI backends using Python and FastAPI.
- Stream LLM responses to a React frontend.
- Build agents that call Python functions and external APIs.
- Implement tool calling, handoffs, manager agents, and guardrails.
- Build RAG systems over PDFs, documents, and codebases.
- Work with vector databases and semantic search.
- Evaluate model quality, latency, token usage, and retrieval accuracy.
- Deploy and monitor AI applications.
- Explain architecture and trade-offs during interviews.

### Recommended technology stack

| Area | Technologies |
|---|---|
| Operating system | Ubuntu Linux |
| Languages | Python, TypeScript |
| Local LLM runtime | Ollama |
| Backend | FastAPI, Pydantic, Uvicorn |
| Frontend | React, TypeScript, Vite |
| ML fundamentals | NumPy, PyTorch, Hugging Face |
| Agent engineering | Direct tool calling, OpenAI Agents SDK, LangGraph |
| Streaming | Async generators, SSE, Fetch API |
| Embeddings | Sentence Transformers, embedding APIs |
| Vector search | Chroma first, Qdrant later |
| Databases | PostgreSQL, Redis |
| Testing | Pytest, HTTPX, Vitest |
| Deployment | Docker, Docker Compose |
| Observability | Structured logging, tracing, evaluation |
| Version control | Git, GitHub |

You do not need to install everything immediately. Introduce each tool when you need it.

---

## 2. Phase Zero — Set Up Your Development Environment

**Estimated duration: 1 day**

### 2.1 Directory structure

Keep installed software, downloaded models, datasets, and source code organized separately.

```text
/home/aakash/
├── ai-projects/                # All your source code
│   ├── 00-python-foundations/
│   ├── 01-llm-playground/
│   ├── 02-llm-streaming-api/
│   ├── 03-ai-chat-frontend/
│   ├── 04-tool-calling-agent/
│   ├── 05-multi-agent-workflow/
│   ├── 06-rag-document-assistant/
│   ├── 07-ai-job-assistant/
│   └── 08-capstone-ai-platform/
├── ai-data/                    # Datasets and evaluation data
│   ├── datasets/
│   ├── documents/
│   └── evaluations/
├── ai-models/                  # Optional manually downloaded models
└── Documents/
```

Create the folders:

```bash
mkdir -p ~/ai-projects
mkdir -p ~/ai-data/{datasets,documents,evaluations}
mkdir -p ~/ai-models
```

**Directory rules:**

- `~/ai-projects`: your source code and Git repositories.
- Each Python project: its own `.venv` virtual environment.
- `~/ai-data`: datasets and test documents.
- `~/ai-models`: optional manually downloaded model files.
- Ollama normally manages its own model storage; you do not need to move its models manually.
- Do not use `sudo pip install` for ordinary project dependencies.

### 2.2 Update Ubuntu

```bash
sudo apt update
sudo apt upgrade
```

Restart if Ubuntu requests it.

### 2.3 Install development utilities

```bash
sudo apt install -y \
  git \
  curl \
  wget \
  build-essential \
  pkg-config \
  python3 \
  python3-pip \
  python3-venv \
  python3-dev \
  pipx \
  jq \
  tree \
  htop \
  nvme-cli
```

Verify:

```bash
python3 --version
git --version
curl --version
nvidia-smi
```

Your NVIDIA driver is already reporting the RTX 5060 Ti, so do not reinstall it just to start learning.

### 2.4 Install an editor

Install Visual Studio Code from: https://code.visualstudio.com/

Recommended extensions:

- Python
- Pylance
- Ruff
- ESLint
- Prettier
- Docker
- GitLens
- REST Client

### 2.5 Configure Git

```bash
git config --global user.name "Aakash"
git config --global user.email "YOUR_EMAIL"
git config --global init.defaultBranch main
```

Replace `YOUR_EMAIL` with the email you use for Git. Never commit API keys, passwords, `.env` files, or private documents.

---

## 3. Phase One — Python for AI Engineering

**Estimated duration: 1 week**

Focus on Python features used frequently in AI backends.

### Python essentials

- Lists, dictionaries, tuples, and sets
- List and dictionary comprehensions
- Functions and decorators
- Classes, inheritance, and composition
- Type hints and dataclasses
- Exceptions and custom exceptions
- Iterators and generators
- `yield` and `yield from`
- Context managers
- File handling and JSON serialization
- Environment variables
- Modules and packages

### Backend-focused Python

- `async` and `await`
- `asyncio`
- Async generators
- HTTP clients
- Dependency management
- Pydantic models
- Logging
- Unit testing
- Timeouts and retries

These topics matter because an LLM backend waits on model inference, API calls, database queries, and tool execution.

### Create your first project

```bash
cd ~/ai-projects
mkdir 00-python-foundations
cd 00-python-foundations

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
touch main.py
```

Example `main.py`:

```python
from collections.abc import Iterator


def count_tokens_approximately(text: str) -> int:
    # Rough demonstration, not a real tokenizer.
    return len(text.split())


def generate_chunks(text: str) -> Iterator[str]:
    for word in text.split():
        yield word + " "


if __name__ == "__main__":
    prompt = "Explain how a language model generates text"
    print(count_tokens_approximately(prompt))

    for chunk in generate_chunks(prompt):
        print(chunk, end="", flush=True)
```

### Practice exercises

1. Read a JSON file and validate its structure.
2. Create a class representing a chat conversation.
3. Build an asynchronous function that calls an HTTP endpoint.
4. Implement retries and timeouts.
5. Write tests using `pytest`.
6. Stream generated chunks using an async generator.

**Milestone:** Write, test, and debug a small asynchronous Python application without copying every line from a tutorial.

---

## 4. Phase Two — Understand LLMs and Run One Locally

**Estimated duration: 1–2 weeks**

### 4.1 Learn the core concepts

Study in this order:

1. What is a large language model?
2. What is a token?
3. What is tokenization?
4. What are parameters?
5. What is a context window?
6. What are prompt tokens and output tokens?
7. What is inference?
8. What is temperature?
9. What are top-p and top-k sampling?
10. What are model weights?
11. What is quantization?
12. What is a transformer?
13. What are attention and self-attention?
14. What are embeddings?
15. Fine-tuning versus RAG

You do not need to train a foundation model from scratch. First learn to run and integrate pretrained models.

### 4.2 Install Ollama

Official Linux guide: https://docs.ollama.com/linux

The standard installer command is:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify:

```bash
ollama --version
systemctl status ollama
nvidia-smi
```

If the service is not running, inspect its status and logs before changing GPU drivers.

### 4.3 Download your first model

Start with a small instruct model, for example:

```bash
ollama run qwen3:8b
```

If that tag is unavailable, check the official model library: https://ollama.com/library

An 8B model is a reasonable starting point for your 16GB GPU. Actual performance and memory use depend on architecture, quantization, context length, and runtime overhead.

Try prompts such as:

```text
Explain React useEffect to a senior frontend developer.
```

```text
Write a Python function that validates an email address.
```

```text
Explain the difference between RAG and fine-tuning.
```

### 4.4 Learn model management

```bash
ollama list
ollama ps
ollama show qwen3:8b
```

Learn the difference between downloading a model, loading it into memory, inference, unloading it, quantized weights, and CPU versus GPU inference.

Use `nvidia-smi` during generation to observe VRAM usage.

### 4.5 Call the local model API

Ollama normally exposes a local API at `http://localhost:11434`.

```bash
curl http://localhost:11434/api/chat \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "qwen3:8b",
    "messages": [
      {
        "role": "user",
        "content": "Explain what an AI agent is."
      }
    ],
    "stream": false
  }'
```

Your Python application does not need to know how the GPU executes the model. It sends an HTTP request to the model runtime and receives a response.

### Project 1: Local LLM Playground

Build a Python CLI application that:

- Accepts user prompts.
- Calls Ollama.
- Displays responses.
- Maintains conversation history.
- Supports resetting the conversation.
- Records response time.
- Handles model-not-running and timeout errors.

**Milestone:** Run a local model and call it programmatically.

---

## 5. Phase Three — PyTorch, Transformers, and Hugging Face

**Estimated duration: 2 weeks**

You can build useful applications without mastering deep learning mathematics first. However, an AI engineer should understand the underlying components.

### Learn NumPy and tensors

- Arrays and shapes
- Broadcasting
- Matrix multiplication
- Tensors
- CPU versus GPU tensors
- Memory usage
- Basic derivatives and gradients

### Learn PyTorch

- `torch.Tensor`
- `requires_grad`
- Autograd
- Loss functions
- Optimizers
- Neural network layers
- Training versus inference mode
- `model.eval()`
- `torch.no_grad()` and inference mode
- Moving tensors and models to CUDA

Install a compatible PyTorch build using the official selector: https://pytorch.org/get-started/locally/

Choose Linux, Pip, Python, and a CUDA build supported by the current PyTorch release and your installed NVIDIA driver.

Verify GPU access:

```python
import torch

print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("VRAM:", torch.cuda.get_device_properties(0).total_memory)
```

Having `nvidia-smi` working does not automatically mean every Python package is configured for GPU execution.

### Learn Hugging Face

Study Transformers, tokenizers, model loading, model configuration, generation parameters, datasets, Accelerate, model cards, and model licenses.

Documentation: https://huggingface.co/docs/transformers/

### Project 2: Model Comparison Lab

Compare two local models on a fixed collection of 20 prompts.

Record:

- Response quality
- Time to first token
- Total generation time
- Tokens per second
- VRAM usage
- Instruction-following accuracy

**Milestone:** Evaluate models rather than choosing one based only on popularity.

---

## 6. Phase Four — Build an LLM Backend with FastAPI

**Estimated duration: 1 week**

### Learn FastAPI

- Routes and HTTP methods
- Request and response models
- Pydantic validation
- Dependency injection
- Async endpoints
- Error handling
- Middleware
- CORS
- Authentication
- API documentation
- Background work
- Streaming responses
- Testing with HTTPX and Pytest

Official tutorial: https://fastapi.tiangolo.com/tutorial/

### Create the project

```bash
cd ~/ai-projects
mkdir 02-llm-streaming-api
cd 02-llm-streaming-api

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install fastapi "uvicorn[standard]" ollama pydantic-settings
```

Structure:

```text
02-llm-streaming-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── schemas.py
│   └── services/
│       ├── __init__.py
│       └── llm_service.py
├── tests/
├── .env.example
├── .gitignore
└── requirements.txt
```

### Your first API

Create `app/main.py`:

```python
from fastapi import FastAPI
from pydantic import BaseModel
from ollama import AsyncClient

app = FastAPI(title="Local LLM API")
client = AsyncClient(host="http://localhost:11434")


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat")
async def chat(request: ChatRequest):
    response = await client.chat(
        model="qwen3:8b",
        messages=[
            {"role": "user", "content": request.message}
        ],
        stream=False,
    )

    return {"response": response.message.content}
```

Run it:

```bash
uvicorn app.main:app --reload --port 8000
```

Open http://127.0.0.1:8000/docs

### Project 3: Local LLM REST API

Add conversation IDs, multiple messages per conversation, input validation, timeouts, error responses, request logging, model selection, and unit tests.

**Milestone:** Your local LLM is available through an API that other applications can consume.

---

## 7. Phase Five — Streaming LLM Responses

**Estimated duration: 1 week**

This is particularly relevant because you already understand React and real-time systems.

### Streaming architecture

```text
React Frontend
      |
      | POST /chat/stream
      v
FastAPI Backend
      |
      | Request stream=True
      v
Ollama Runtime
      |
      | Partial response chunks
      v
FastAPI async generator
      |
      | Server-Sent Events
      v
React reads the response stream
      |
      v
UI updates incrementally
```

The backend forwards chunks as they arrive instead of waiting for the complete answer.

### Learn these concepts

- Token-by-token generation
- Time to first token
- Async generators
- `yield`
- HTTP chunked transfer
- Server-Sent Events (SSE)
- JSON Lines
- Client-side stream reading
- Cancellation and disconnect handling
- Error events
- Backpressure and buffering

Documentation:

- https://fastapi.tiangolo.com/tutorial/server-sent-events/
- https://fastapi.tiangolo.com/advanced/stream-data/

### Add a streaming endpoint

Extend `app/main.py` with:

```python
import json
from fastapi.responses import StreamingResponse


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):

    async def generate():
        try:
            stream = await client.chat(
                model="qwen3:8b",
                messages=[
                    {"role": "user", "content": request.message}
                ],
                stream=True,
            )

            async for chunk in stream:
                content = chunk.message.content

                if content:
                    event = {
                        "type": "token",
                        "content": content,
                    }
                    yield f"data: {json.dumps(event)}\n\n"

                if chunk.done:
                    yield 'data: {"type":"done"}\n\n'

        except Exception:
            error = {
                "type": "error",
                "message": "The model request failed.",
            }
            yield f"data: {json.dumps(error)}\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
```

This is a learning example. Check the installed Ollama Python SDK's streaming interface for your version, and test disconnect handling and error behavior before production use.

### Build the React frontend

```bash
cd ~/ai-projects
npm create vite@latest 03-ai-chat-frontend -- --template react-ts
cd 03-ai-chat-frontend

npm install
npm run dev
```

Use `fetch()` with a POST request and `response.body.getReader()` to read the stream. Append each decoded chunk to the displayed assistant message.

Do not assume the entire response arrives in one network chunk. A network chunk can contain partial SSE events or multiple events, so implement a proper event parser.

Build:

- Chat history
- Streaming text
- Loading indicator
- Stop generation
- Error handling
- Retry
- Markdown rendering
- Code syntax highlighting
- Conversation reset

**Milestone:** A ChatGPT-style application running locally, with React frontend and Python backend.

---

## 8. Phase Six — AI Agents and Tool Calling

**Estimated duration: 2 weeks**

This is one of the most important phases for your job goal.

### Understand the difference

An LLM produces text. An agent combines an LLM with instructions, tools, state, and a control loop.

A typical agent loop:

1. Receive the user request.
2. Send the request and available tool definitions to the model.
3. Inspect the model response.
4. If the model requests a tool, validate the arguments.
5. Execute the corresponding function.
6. Return the tool result to the model.
7. Repeat until the model produces a final answer or a limit is reached.

A tool call is not the same as ordinary text mentioning a tool. Your application must actually execute the selected function.

### Learn these concepts

- System instructions
- Function calling
- JSON schemas
- Tool definitions
- Tool execution
- Tool results
- Agent loops
- Maximum iteration limits
- State management
- Error recovery
- Structured outputs
- Human approval

### Build your first tool-calling agent

```bash
cd ~/ai-projects
mkdir 04-tool-calling-agent
cd 04-tool-calling-agent

python3 -m venv .venv
source .venv/bin/activate

pip install ollama pydantic pytest
```

Example tool:

```python
def calculate_total(price: float, quantity: int) -> float:
    if price < 0 or quantity < 0:
        raise ValueError("Values must not be negative")

    return round(price * quantity, 2)
```

Your model should be able to request the tool with arguments such as:

```json
{
  "price": 250,
  "quantity": 3
}
```

Your application executes the function and sends its result back to the model.

Start with the native tool-calling interface offered by your chosen model and runtime. Validate arguments yourself, and never use `eval()` to execute model-generated code.

### Tool-calling exercises

1. Calculator tool
2. Current-time tool
3. Read-only database lookup
4. Job-description parser
5. Search a local document collection
6. Create a draft email
7. Request human approval before sending an email

### Project 4: Developer Assistant Agent

Build an agent that can:

- Explain code snippets
- Search a small local knowledge base
- Calculate values
- Retrieve information from a database
- Return structured results
- Explain which tool it used
- Stop after a configured number of tool calls

**Milestone:** Understand how an agent chooses tools, how your backend executes them, and how tool results feed back into the model.

---

## 9. Phase Seven — Agent Frameworks, Handoffs, and Manager Agents

**Estimated duration: 1–2 weeks**

Once you understand the basic agent loop, learn a framework that handles orchestration.

### Learn the OpenAI Agents SDK

Documentation: https://openai.github.io/openai-agents-python/

Install inside a dedicated project's virtual environment:

```bash
pip install openai-agents
```

The SDK supports agents, function tools, handoffs, guardrails, sessions, and tracing. Its standard OpenAI model integrations require suitable API credentials. It does not guarantee that every local Ollama model can be used without additional integration.

Start with an appropriate API-backed model, then learn provider and adapter integration. Keep your local Ollama implementation separate until you verify compatibility.

### Pattern A: Single agent

```text
User
 |
 v
Assistant Agent
 |
 +---- Calculator Tool
 |
 +---- Search Tool
 |
 v
Final Answer
```

### Pattern B: Handoffs

```text
User
 |
 v
Triage Agent
 |
 +----> Coding Agent
 |
 +----> Research Agent
 |
 +----> Writing Agent
          |
          v
      Final Answer
```

A handoff transfers control to another agent.

### Pattern C: Manager agent

```text
             User
               |
               v
        Manager Agent
          /    |    \
         v     v     v
      Research Coding Review
         \     |     /
          v    v    v
        Manager Agent
               |
               v
          Final Answer
```

A manager agent can invoke specialist agents as tools and retain responsibility for the overall workflow.

### What you must understand

- Agent versus tool
- Handoff versus agents-as-tools
- Manager versus specialist
- Shared versus isolated state
- Context passing
- Tool permissions
- Maximum steps
- Failure handling
- Human-in-the-loop approvals
- Tracing and debugging

### Project 5: Multi-Agent Job Assistant

Build an application that:

1. Accepts a job description.
2. Uses a research agent to extract requirements.
3. Uses a skills agent to compare the role with your experience.
4. Uses a writing agent to draft a tailored CV summary.
5. Uses a reviewer agent to check relevance and unsupported claims.
6. Returns the result for your approval.

Start with local files and sample job descriptions. Do not automate applications or send messages without explicit human approval.

**Milestone:** Explain and implement handoffs and manager-style delegation.

---

## 10. Phase Eight — Guardrails, Security, and Reliability

**Estimated duration: 1 week**

Production AI engineering is not just about getting a model to answer questions.

Learn:

- Input validation
- Output validation
- Pydantic schemas
- Tool-level permissions
- Prompt injection
- Untrusted retrieved documents
- Rate limiting
- Request timeouts
- Retry policies
- Maximum agent steps
- Token and cost budgets
- Sensitive-data handling
- Audit logs
- Human approval
- Secret management
- Sandboxing

### Example: restrict a tool

For a file-reading tool:

- Restrict access to an approved directory.
- Reject paths that escape that directory.
- Apply file-size limits.
- Handle missing files safely.
- Log the operation.
- Do not expose secrets.

For tools that send emails, modify records, execute shell commands, or make purchases, use explicit permission checks and human approval where appropriate.

**Interview point:** The model should not be the security boundary. The backend must enforce authorization and validation.

---

## 11. Phase Nine — RAG and Vector Databases

**Estimated duration: 2 weeks**

RAG means Retrieval-Augmented Generation. It lets an application retrieve relevant information from external documents and provide it to an LLM as context.

### RAG pipeline

```text
Documents
   |
   v
Extract Text
   |
   v
Clean and Split into Chunks
   |
   v
Generate Embeddings
   |
   v
Store Vectors + Metadata
   |
   v
User Question
   |
   v
Embed the Question
   |
   v
Retrieve Relevant Chunks
   |
   v
Build Context for the LLM
   |
   v
Generate an Answer with Sources
```

### Learn these concepts

- Embeddings
- Vector similarity
- Cosine similarity
- Chunking strategies
- Chunk overlap
- Metadata filtering
- Top-k retrieval
- Semantic search
- Hybrid search
- Reranking
- Context-window limits
- Citations
- Retrieval evaluation
- Hallucination reduction

### Recommended learning order

1. Build basic vector search using an embedding model.
2. Store vectors and metadata in Chroma.
3. Retrieve relevant chunks.
4. Pass those chunks into Ollama.
5. Return source references with the answer.
6. Evaluate retrieval quality.
7. Learn Qdrant for a more production-oriented workflow.

Resources:

- Sentence Transformers: https://www.sbert.net/
- Chroma: https://docs.trychroma.com/
- Qdrant: https://qdrant.tech/documentation/

### Project 6: Personal Knowledge Assistant

Build a RAG application that answers questions about your CV, technical notes, interview preparation documents, project documentation, and public technical documentation you have permission to use.

Requirements:

- Upload PDF and text documents.
- Extract and chunk text.
- Generate embeddings.
- Store document metadata.
- Search relevant passages.
- Generate answers using a local model.
- Show the sources used.
- Say when retrieved information is insufficient.
- Support document removal and re-indexing.

**Milestone:** Explain the difference between fine-tuning, prompt engineering, and RAG, and build a working RAG pipeline.

---

## 12. Phase Ten — Memory, Databases, and Workflow Orchestration

**Estimated duration: 1–2 weeks**

An AI application needs more than a conversation window.

Understand the difference between conversation history, session state, user preferences, long-term application data, retrieved knowledge, and agent execution state.

### PostgreSQL

Use it for:

- Users
- Conversations
- Messages
- Tool execution records
- Agent runs
- Approval requests
- Application data

### Redis

Use it for:

- Caching
- Rate limiting
- Short-lived state
- Queue-related use cases
- Coordination between backend processes

### Workflow orchestration

After building basic agents, learn LangGraph:

https://docs.langchain.com/oss/python/langgraph/overview

Study:

- Graph-based workflows
- Nodes and edges
- Conditional routing
- Persistent state
- Checkpointing
- Human-in-the-loop
- Resume after interruption
- Retry and failure paths

Use a graph framework when a workflow has meaningful branching, state, or recovery requirements. A simple agent does not always need a framework.

### Project 7: Stateful AI Support Assistant

Build an assistant that:

- Maintains conversation history.
- Retrieves customer records with proper authorization.
- Searches internal knowledge.
- Routes complex requests to specialist agents.
- Requests approval before sensitive actions.
- Persists workflow state.
- Recovers safely from failed tool calls.

---

## 13. Phase Eleven — Fine-Tuning and Deeper Model Engineering

**Estimated duration: 2–3 weeks, after the preceding phases**

You do not need fine-tuning to build your first useful AI agent. Learn it after inference, prompts, data preparation, and evaluation.

Study:

- Supervised fine-tuning
- Training versus inference
- Training datasets
- Train/validation splits
- Loss and overfitting
- LoRA
- QLoRA
- PEFT
- Hugging Face TRL
- Quantization
- Model checkpoints
- Evaluation before and after tuning

Resources:

- PEFT: https://huggingface.co/docs/peft/
- TRL: https://huggingface.co/docs/trl/

Your 16GB VRAM is suitable for many small-model experiments, including some parameter-efficient fine-tuning workflows, but not every model or configuration. Model size, sequence length, batch size, quantization, and optimizer memory all matter.

Start with a small model and modest dataset. Compare the tuned model with the original on a fixed evaluation set.

**Milestone:** Understand when fine-tuning is appropriate and conduct a controlled experiment.

---

## 14. Phase Twelve — Testing, Evaluation, Deployment, and Observability

**Estimated duration: 1–2 weeks**

### Testing

- Unit tests for tool functions
- API integration tests
- Mocked model responses
- RAG retrieval tests
- Agent workflow tests
- Streaming tests
- Failure-path tests
- Authorization tests

### Evaluation

Create a fixed dataset of representative prompts and expected outcomes.

Measure:

- Correctness
- Instruction adherence
- Tool selection accuracy
- Tool argument validity
- Retrieval precision and recall
- Citation correctness
- Latency
- Tokens generated
- Resource usage
- Failure rate

Avoid relying only on subjective impressions of a few outputs.

### Deployment

Learn:

- Docker images
- Docker Compose
- Environment configuration
- Database migrations
- Health checks
- Structured logging
- Metrics
- API authentication
- Reverse proxies
- Production CORS settings
- Secret management
- Graceful shutdown

Keep the local LLM runtime separate from the API service when that helps deployment and resource management.

Exposing an unauthenticated local model API to the public internet is unsafe. Bind development services to localhost unless you intentionally configure and secure remote access.

---

## 15. Portfolio Projects

Build these in order. Each project should have a Git repository, README, architecture diagram, setup instructions, tests, screenshots, and a short demo.

| # | Project | Skills demonstrated |
|---|---|---|
| 1 | Local LLM Playground | Ollama, prompts, inference |
| 2 | Model Comparison Lab | Evaluation, latency, VRAM |
| 3 | Streaming AI Chat | FastAPI, SSE, React |
| 4 | Tool-Calling Developer Agent | Tools, validation, agent loop |
| 5 | Multi-Agent Job Assistant | Handoffs, manager agents, guardrails |
| 6 | Document RAG Assistant | Embeddings, vector search, citations |
| 7 | Stateful AI Support Assistant | PostgreSQL, memory, orchestration |
| 8 | AI Operations Platform | Authentication, agents, RAG, observability |

### Capstone: AI Operations Assistant

Build a full-stack application using your existing strengths.

**Frontend**

- React and TypeScript
- Streaming chat
- Conversation history
- Agent execution status
- Tool-call timeline
- Approval interface
- Source citations

**Backend**

- FastAPI
- Model provider abstraction
- Local Ollama integration
- Agent orchestration
- Tool registry
- Input/output validation
- RAG retrieval service
- PostgreSQL persistence
- Redis where useful

**Example workflow**

A user asks: "Review this support ticket, find the relevant documentation, recommend a solution, and prepare a response."

The system:

1. Validates the request.
2. Retrieves relevant customer and ticket information.
3. Searches the knowledge base.
4. Uses a specialist agent to analyze the issue.
5. Drafts a response.
6. Checks the response against policy.
7. Requests human approval before sending.
8. Records the final action.

This demonstrates backend engineering, AI integration, workflow design, security, and frontend experience in one portfolio piece.

---

## 16. Suggested Weekly Schedule

Assume approximately 2 hours per day, 5 days per week. These are estimates, not deadlines.

| Weeks | Focus | Deliverable |
|---|---|---|
| 1 | Python async, generators, typing, testing | Python foundations project |
| 2 | LLM concepts and Ollama | Local LLM CLI |
| 3–4 | PyTorch, Transformers, model evaluation | Model comparison lab |
| 5 | FastAPI and model integration | LLM REST API |
| 6 | SSE and React streaming | Streaming chat app |
| 7–8 | Tool calling and agent loops | Developer assistant agent |
| 9 | Handoffs, manager agents, guardrails | Multi-agent job assistant |
| 10–11 | Embeddings, RAG, vector databases | Document assistant |
| 12 | Memory, PostgreSQL, workflow state | Stateful AI assistant |
| 13–14 | Testing, Docker, evaluation, observability | Production-style release |
| 15–16 | Capstone and interview preparation | Portfolio-ready project |

After the initial 16 weeks, continue with fine-tuning, deeper model internals, advanced retrieval, and more complex workflow systems.

---

## 17. AI Engineering Interview Preparation

Prepare to explain these topics in your own words and support answers with code from your projects.

### LLM fundamentals

- What is a token?
- What is a context window?
- How does a transformer work?
- What is an embedding?
- What is quantization?
- How does inference differ from training?
- How do you estimate GPU memory requirements?

### Backend and streaming

- How does FastAPI handle asynchronous requests?
- What is the difference between SSE and WebSockets?
- How would you stream an LLM response to React?
- How do you handle client cancellation?
- How would you handle model timeouts and retries?

### Agents

- What is an agent?
- What is function calling?
- Who executes a tool call?
- What is the difference between an agent and a workflow?
- What is a handoff?
- When would you use a manager agent?
- How do you prevent infinite tool-call loops?
- How do you validate tool arguments?
- How do you safely execute sensitive actions?

### RAG

- What are embeddings?
- What is vector similarity?
- Why do chunk size and overlap matter?
- What is top-k retrieval?
- How do you evaluate retrieval quality?
- What is reranking?
- When is RAG preferable to fine-tuning?
- How do you reduce hallucinations?

### Production engineering

- How do you test nondeterministic model outputs?
- How do you manage API keys?
- How do you prevent prompt injection from causing unsafe tool execution?
- How do you measure latency and model quality?
- How do you manage concurrent requests to a local GPU?
- How do you control model memory consumption?

---

## 18. Official Learning Resources

Use official documentation as your primary reference.

1. Python — https://docs.python.org/3/tutorial/
2. FastAPI — https://fastapi.tiangolo.com/tutorial/
3. Ollama — https://docs.ollama.com/
4. PyTorch — https://pytorch.org/get-started/locally/
5. Hugging Face Transformers — https://huggingface.co/docs/transformers/
6. Sentence Transformers — https://www.sbert.net/
7. Chroma — https://docs.trychroma.com/
8. Qdrant — https://qdrant.tech/documentation/
9. OpenAI Agents SDK — https://openai.github.io/openai-agents-python/
10. LangGraph — https://docs.langchain.com/oss/python/langgraph/overview
11. Docker — https://docs.docker.com/
12. PostgreSQL — https://www.postgresql.org/docs/

---

## 19. Rules to Follow While Learning

1. Build a working project at every major phase.
2. Understand the code you write; do not merely copy tutorials.
3. Start with one agent before building multi-agent systems.
4. Learn direct tool calling before adopting a large agent framework.
5. Use local models to experiment without per-token API charges, while remembering that hardware, electricity, storage, and optional external services still have costs.
6. Keep Python dependencies isolated per project.
7. Commit working milestones to Git.
8. Test failure paths as carefully as successful paths.
9. Keep secrets outside source control.
10. Never let the model bypass backend authorization.
11. Measure quality, latency, and resource usage rather than guessing.
12. Write a short architecture explanation for every portfolio project.

---

## 20. First-Day Checklist

Start here. Do not try to install the entire AI ecosystem on day one.

- [ ] Verify `nvidia-smi` works.
- [ ] Install Git, Python, `venv`, and VS Code.
- [ ] Create `~/ai-projects`, `~/ai-data`, and `~/ai-models`.
- [ ] Create `00-python-foundations`.
- [ ] Create and activate its `.venv`.
- [ ] Practice Python generators and async functions.
- [ ] Install Ollama using its official Linux instructions.
- [ ] Download one small instruct model.
- [ ] Run a prompt and observe GPU memory usage.
- [ ] Commit the first project to Git.

### Immediate next step

Start with environment setup and local model installation. Once Ollama is running, build the Python CLI before adding FastAPI or React.

The goal is to understand each layer separately, then combine them into a production-style AI application. That approach will help you explain the architecture and implementation confidently in AI engineering interviews.
