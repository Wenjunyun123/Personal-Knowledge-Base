---
author: unknown
source: GitHub
url: https://github.com/Zleap-AI/SAG
saved: 2026-06-24 14:17:02
tags:
  - 笔记同步助手
id: aa13effe-f483-4bd9-b5d9-b1fac0375dd7
---

![[笔记同步助手/images/e3a287208d2e3a58fe8c16cf4480ee31_MD5.svg|Zleap AI]]

**Language**: English | [简体中文](/Zleap-AI/SAG/blob/main/README-CN.md)

> **SAG:** Graph retrieval technology capable of running on large-scale dynamic data.
> 
> **Paper:** [https://arxiv.org/abs/2606.15971](https://arxiv.org/abs/2606.15971)

This project is an out-of-the-box document retrieval workbench built on SAG. After you upload Markdown or TXT documents, SAG automatically handles chunking, vectorization, event extraction, entity extraction, and relation organization. You can ask questions over project documents in a ChatGPT-like interface, inspect chunks, events, entities, embeddings, search traces, raw model logs, and explore the knowledge graph.

![[笔记同步助手/images/9eebfcdfc1aedff4bc946e7e684331a6_MD5.png|SAG chat workbench]]

## RAG SOTA and Benchmark

[](#rag-sota-and-benchmark)

SAG benchmark reproduction code: [Zleap-AI/SAG-Benchmark](https://github.com/Zleap-AI/SAG-Benchmark)

SAG is a next-generation RAG approach designed for agents. Instead of stuffing more chunks into the model, it organizes document knowledge with a lighter structure:

chunk -> event
chunk -> entities
event <-> entities

Each chunk extracts one complete event and multiple entities. The event preserves the full semantic unit, while entities build the index and enable relational expansion, so retrieval can start from a matched event and continue through multi-hop recall without the rebuild cost of a heavyweight knowledge graph.

![[笔记同步助手/images/99bdf7a45e4fbf5f17f7f83496680422_MD5.jpg|SAG architecture]]

On HotpotQA / 2WikiMultiHop / MuSiQue, under the same configuration:

Embedding = bge-large-en-v1.5
LLM = qwen3.6-flash
Datasets = HotpotQA / 2WikiMultiHop / MuSiQue

Compared with HippoRAG 2, SAG achieves clear recall improvements on multi-hop QA: **average Recall@2 improves from 68.14% to 79.30%, a gain of 11.16 percentage points, or about 16.4% relative improvement**. Higher Recall@2 means agents can hit key evidence earlier with less context, reducing token cost, latency, and distraction in multi-turn tasks.

![[笔记同步助手/images/ca6c02680128746035c0331d62972e52_MD5.png|SAG benchmark summary]]

On MuSiQue Recall@5, SAG improves from HippoRAG 2's 65.13% to 80.04%; after switching to NV-Embed-v2, it further reaches 81.71%, showing that the gain mainly comes from the structure rather than only a stronger embedding model.

## What SAG Can Do

[](#what-sag-can-do)

This project turns SAG into a local workbench that can run immediately. It is suitable for:

-   Project document Q&A
-   Personal knowledge base search
-   RAG / agent prototype validation
-   Document event and entity analysis
-   MCP tool integration testing
-   Search pipeline debugging and model-call inspection

Core features:

-   **Project management**: each project has its own documents, conversations, graph, and MCP configuration.
-   **Multi-document upload**: upload multiple Markdown / TXT files at once, with processing stages and progress.
-   **Document processing results**: inspect chunks, events, entities, embedding data, keyword title search, and paginated browsing.
-   **Conversational retrieval**: ask multi-turn questions over the current project, with streaming output and stop generation.
-   **Source citations**: answers can show numbered citations; click a number to view the original chunk.
-   **Search trace visualization**: the right panel shows SAG's internal retrieval steps and latency in real time.
-   **Raw logs**: browser cache stores raw LLM / Embedding / Rerank requests and responses.
-   **Knowledge graph**: explore project relations with event and entity nodes; drag, zoom, expand, and open details.
-   **MCP integration**: each project exposes its own MCP configuration so external agents can call the current project directly.

## Tech Stack

[](#tech-stack)

SAG uses TypeScript across the stack. The frontend is a React + Vite + Tailwind CSS WebUI. The backend uses Fastify HTTP APIs, the MCP TypeScript SDK, and layered service modules. The data layer uses PostgreSQL, pgvector, full-text search, and SQL multi-hop queries. Model providers are OpenAI-compatible LLM, Embedding, and Rerank APIs.

## Workbench Preview

[](#workbench-preview)

### Document Processing

[](#document-processing)

In the Document tab, you can upload documents, inspect processing status, chunks, events, entities, and embeddings.

![[笔记同步助手/images/ee8c08244b825a3f11b477e837bd5640_MD5.png|SAG document view]]

### Graph Exploration

[](#graph-exploration)

In the Graph tab, you can explore entity-event relations across a project. Nodes support drag, zoom, click-to-expand, and double-click details.

![[笔记同步助手/images/184d319472d974160fa384cf059a9fca_MD5.png|SAG graph view]]

### Conversational Retrieval

[](#conversational-retrieval)

In the Chat tab, you can ask continuous questions over the current project. Each retrieval refreshes the right-side trace panel for debugging the current call chain.

## Search Modes

[](#search-modes)

SAG provides two modes:

-   **Fast mode**: directly matches the query against the entity store using full-text / BM25 search, expands through SAG multi-hop retrieval, and finally uses `qwen3-rerank` to select top-k. This mode does not use an LLM to extract query entities or filter candidates, so it is much faster.
-   **Standard mode**: uses an LLM to extract query entities, then runs SAG multi-route recall and LLM reranking. This is useful when you want to compare the higher-precision pipeline.

Both modes are more than ordinary vector search because both use SAG's event/entity index and SQL multi-hop expansion.

## Quick Start

[](#quick-start)

### 1\. Prepare the Environment

[](#1-prepare-the-environment)

You need:

-   Node.js 20 or later
-   npm
-   PostgreSQL
-   pgvector

If you want the fastest setup, use Docker to start PostgreSQL.

### 2\. Clone the Project

[](#2-clone-the-project)

git clone https://github.com/Zleap-AI/SAG.git
cd SAG

### 3\. Create the Config File

[](#3-create-the-config-file)

cp .env.example .env

`.env.example` already contains default values. For real usage, fill in your own LLM and Embedding API keys.

### 4\. Start PostgreSQL

[](#4-start-postgresql)

Using Docker:

docker compose up -d

If you do not want to use Docker, you can use Homebrew on macOS:

brew install postgresql@17 pgvector
brew services start postgresql@17

/opt/homebrew/opt/postgresql@17/bin/createdb sag\_lite
/opt/homebrew/opt/postgresql@17/bin/psql -d sag\_lite -c 'create extension if not exists vector;'

If you use a local PostgreSQL instance, update `DATABASE_URL` in `.env`, for example:

DATABASE\_URL\=postgres://your\_user@localhost:5432/sag\_lite

### 5\. Install Dependencies and Initialize the Database

[](#5-install-dependencies-and-initialize-the-database)

npm install
npm run db:setup

### 6\. Start the Development Server

[](#6-start-the-development-server)

npm run dev

Default development URLs:

WebUI: http://localhost:5173
API:   http://localhost:4173

### 7\. Build and Start Production

[](#7-build-and-start-production)

npm run build
npm start

Default production URL:

http://localhost:4173

## First Use

[](#first-use)

1.  Open the WebUI.
2.  Click "New Project" at the top of the left project list.
3.  Go to the Document tab and click "Add Document".
4.  Upload `.md` or `.txt` files.
5.  Wait for the processing queue to finish.
6.  Inspect chunks, events, entities, and embedding status.
7.  Return to the Chat tab and ask questions over the current project.
8.  For debugging, inspect the right-side Search Trace and Raw Logs.
9.  For relationship exploration, open the Graph tab.
10.  For external agents, open the MCP tab and copy the current project's configuration.

## Configure LLM and Embedding

[](#configure-llm-and-embedding)

SAG supports OpenAI-compatible APIs. Default example:

EMBEDDING\_BASE\_URL\=https://api.302ai.cn/v1
EMBEDDING\_MODEL\=text-embedding-3-large
EMBEDDING\_DIMENSIONS\=1024

LLM\_BASE\_URL\=https://api.302ai.cn/v1
LLM\_MODEL\=qwen3.6-flash

RERANK\_MODEL\=qwen3-rerank
DEFAULT\_SEARCH\_MODE\=fast

You can configure models in two ways:

### Option 1: WebUI Global Settings

[](#option-1-webui-global-settings)

Click the settings icon at the top of the left sidebar, open Global Settings, and fill in provider, model names, and API keys.

API keys only show as "Configured / Not configured". Plaintext keys are not echoed in the UI or API responses.

### Option 2: `.env`

[](#option-2-env)

EMBEDDING\_API\_KEY\=your\_embedding\_key
LLM\_API\_KEY\=your\_llm\_key

If no API key is configured, the system uses a local deterministic fallback. This is useful for tests and UI inspection, but real retrieval quality requires remote models.

## MCP Integration

[](#mcp-integration)

SAG can act as an MCP Server for external agents. Each project's MCP configuration binds the current project ID, so tool calls do not need to pass `projectId`.

Open the MCP tab in the WebUI to see the auto-generated `mcpServers` JSON for the current project. It looks like this:

{
  "mcpServers": {
    "sag": {
      "command": "npm",
      "args": \["run", "mcp"\],
      "env": {
        "SAG\_MCP\_SOURCE\_ID": "current\_project\_id"
      }
    }
  }
}

Available MCP tools:

-   `sag_ingest_document`: import a document and run chunking, event extraction, entity extraction, and vectorization.
-   `sag_search`: run SAG multi-route retrieval on the current project and return the internal trace.
-   `sag_explain_search`: return the current project's retrieval pipeline explanation and trace.
-   `sag_get_event`: query event details by event ID.

## HTTP API Examples

[](#http-api-examples)

Health check:

curl http://localhost:4173/health

Create a project:

curl -X POST http://localhost:4173/api/projects \\
  -H 'Content-Type: application/json' \\
  -d '{"name":"Demo Project"}'

Ingest a document:

curl -X POST http://localhost:4173/ingest \\
  -H 'Content-Type: application/json' \\
  -d '{"sourceId":"project\_id","title":"Demo","content":"# Demo\\n\\nSAG can search project documents.","extract":true}'

Run search:

curl -X POST http://localhost:4173/api/search \\
  -H 'Content-Type: application/json' \\
  -d '{"query":"Why is SAG suitable for multi-hop retrieval?","sourceIds":\["project\_id"\],"strategy":"multi","searchMode":"fast","topK":5,"returnTrace":true}'

Stream search trace:

curl -N -X POST http://localhost:4173/api/search/stream \\
  -H 'Content-Type: application/json' \\
  -d '{"query":"Explain SAG event/entity indexing","sourceIds":\["project\_id"\],"strategy":"multi","returnTrace":true}'

## Common Commands

[](#common-commands)

# Type check
npm run typecheck

# Run tests
npm test

# Build production assets
npm run build

# Start production server
npm start

# Start MCP stdio server
npm run mcp

## Project Structure

[](#project-structure)

src/
  ai/                 LLM, Embedding, and Rerank clients
  api/                HTTP API
  config/             Environment configuration
  db/                 Database connection, migrations, repositories, vector tools
  ingestion/          Document chunking and event extraction
  mcp/                MCP Server
  observability/      Logs and model-call records
  services/           Document processing, search, graph, and WebUI services

web/
  src/                React WebUI

migrations/           PostgreSQL schema
test/                 Unit tests
docs/assets/          README screenshots and diagrams

## FAQ

[](#faq)

### PostgreSQL Connection Failed

[](#postgresql-connection-failed)

First confirm that the database is running:

docker compose ps

Then confirm that `DATABASE_URL` in `.env` is correct.

### pgvector Is Missing

[](#pgvector-is-missing)

Make sure pgvector is installed and run:

create extension if not exists vector;

If you use `docker compose up -d`, the image already includes pgvector.

### Why Do I Not See Real Model Quality?

[](#why-do-i-not-see-real-model-quality)

If `LLM_API_KEY` and `EMBEDDING_API_KEY` are not configured, the system enters local fallback mode. This is useful for testing, but it is not suitable for judging real retrieval quality.

### Document Processing Is Slow

[](#document-processing-is-slow)

Document processing calls Embedding and LLM APIs. Speed mainly depends on document count, chunk count, model API latency, and concurrency settings. You can tune this in `.env`:

INGEST\_CONCURRENCY\=5

### The Port Is Already in Use

[](#the-port-is-already-in-use)

In development mode, update `.env`:

HTTP\_PORT\=4173

The Vite WebUI uses `5173` by default. If the port is occupied, Vite will show the new address automatically.

## License

[](#license)

MIT License. See [LICENSE](/Zleap-AI/SAG/blob/main/LICENSE).

---

内容效果不满意？[点此反馈](https://feedback.notebooksyncer.com/feedback/c487dfaa_1782281817569?u=https%3A%2F%2Fgithub.com%2FZleap-AI%2FSAG&s=obsidian)