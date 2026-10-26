# AI Application Engineer — Project Roadmap

## Goal

Build practical AI applications to develop skills in LLMs, RAG, vector databases, tool calling, agents, evaluation, and production engineering.

## Project 1: Company Policy RAG Assistant

**Difficulty:** Beginner to Intermediate  
**Priority:** Start here

Build a chatbot that answers questions from employment documents, company policies, and PDFs.

**Core features**
- Extract text from PDF documents.
- Split documents into chunks.
- Generate embeddings using `nomic-embed-text`.
- Store and retrieve chunks using ChromaDB.
- Generate answers using a local LLM through Ollama.
- Provide source citations and PDF page references.
- Handle questions when the answer is not in the document.

**Skills to learn**
- RAG architecture
- Chunking and embeddings
- Vector similarity search
- Retrieval quality and hallucination handling
- FastAPI and streaming responses
- RAG evaluation

**Stretch goal:** Support multiple documents and metadata filters.

---

## Project 2: AI Customer Support Assistant

**Difficulty:** Intermediate

Build an assistant that answers customer questions using product documentation and troubleshooting guides.

**Core features**
- Search multiple knowledge sources.
- Maintain conversation history.
- Classify customer intent.
- Generate structured responses.
- Escalate unresolved queries to a human.
- Create support tickets through an API.

**Skills to learn**
- Advanced RAG
- Conversation context management
- Intent classification
- Structured outputs
- Human handoffs
- API integration

**Stretch goal:** Build a dashboard for customer support agents.

---

## Project 3: Chat With Your Database

**Difficulty:** Intermediate

Build an application that converts natural-language questions into database queries.

**Example:** "Which products had the highest sales last month?"

**Core features**
- Understand database schemas.
- Generate SQL queries.
- Validate queries before execution.
- Execute read-only queries.
- Explain results in natural language.
- Display results in tables and charts.

**Skills to learn**
- LLM tool calling
- Structured outputs and Pydantic
- SQL generation and validation
- Database integration
- Permission controls
- Query safety

**Stretch goal:** Support multiple databases and visualization options.

---

## Project 4: AI Email and Document Assistant

**Difficulty:** Intermediate

Build an assistant that summarizes emails and documents, extracts information, and drafts replies.

**Core features**
- Summarize long documents.
- Extract names, dates, tasks, and deadlines.
- Generate structured JSON output.
- Draft email responses.
- Save drafts for human approval.
- Track extracted tasks.

**Skills to learn**
- Structured extraction
- Pydantic validation
- Prompt design
- Multi-step LLM workflows
- Human-in-the-loop approval
- Third-party API integration

**Stretch goal:** Integrate an email provider and calendar.

---

## Project 5: AI Research Assistant With Tools

**Difficulty:** Intermediate to Advanced

Build an assistant that researches a topic by executing a series of approved tools and producing a report.

**Core features**
- Break a research request into smaller steps.
- Call approved search or application tools.
- Collect and organize results.
- Track task state and progress.
- Retry transient failures and enforce stopping conditions.
- Produce a report with sources.

**Skills to learn**
- Agent loops and tool calling
- State management
- Workflow orchestration
- Retries, timeouts, and error handling
- Source tracking
- Human approval for consequential actions

**Stretch goal:** Support pausing and resuming long-running tasks.

---

## Project 6: AI Code Review Assistant

**Difficulty:** Advanced

Build a tool that reviews Git diffs and identifies potential bugs, risky changes, and missing tests.

**Core features**
- Accept a Git diff or pull request.
- Identify potential bugs and edge cases.
- Return structured findings with file and line references.
- Explain the risk behind each finding.
- Suggest fixes and relevant tests.
- Track false positives and missed issues.

**Skills to learn**
- Code-aware prompting
- Long-context handling and code retrieval
- Structured findings
- Automated validation
- Evaluation of false positives
- GitHub integration

**Stretch goal:** Integrate with GitHub pull requests.

---

## Project 7: LLM Observability and Evaluation Platform

**Difficulty:** Advanced

Build a dashboard to monitor AI requests, failures, latency, and answer quality.

**Core features**
- Record request and response metadata.
- Track latency and errors.
- Track token usage and cost when available.
- Store traces for multi-step workflows.
- Evaluate answers against a test dataset.
- Compare models and prompt versions.

**Skills to learn**
- Logging and tracing
- Evaluation datasets
- Retrieval and answer quality metrics
- Model comparison
- Observability
- Performance optimization

**Stretch goal:** Run the same evaluation set against multiple models and display a comparison report.

---

## Recommended Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React + TypeScript |
| Backend | Python + FastAPI |
| Local inference | Ollama |
| Embeddings | `nomic-embed-text` |
| Vector database | ChromaDB |
| Data validation | Pydantic |
| Relational database | SQLite first, PostgreSQL later |
| Streaming | Server-Sent Events (SSE) |
| Testing and evaluation | Pytest and custom evaluation datasets |

Learn the underlying concepts before relying heavily on orchestration frameworks.

---

## Recommended Learning Order

1. Company Policy RAG Assistant
2. AI Customer Support Assistant
3. Chat With Your Database
4. AI Email and Document Assistant
5. AI Research Assistant With Tools
6. AI Code Review Assistant
7. LLM Observability and Evaluation Platform

You do not need to finish every project before applying for jobs. Prioritize a few projects that you can explain, test, and debug thoroughly.

## Definition of Done for Each Project

- [ ] Build a minimal working version.
- [ ] Understand and explain each major component.
- [ ] Test invalid inputs and failure cases.
- [ ] Add validation, error handling, and logging.
- [ ] Evaluate quality with repeatable test cases.
- [ ] Document architecture and setup instructions.
- [ ] Add a clear README with screenshots or a demo.
- [ ] Keep API keys and personal documents out of public repositories.
