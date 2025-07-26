# 🧠 DICOM Specialist

A lightweight but powerful [fastMCP](https://github.com/grobian/fastmcp) servers for navigating the complexity of the DICOM standard.

## Features:
- 🔍 **RAG (Retrieval-Augmented Generation)** over the DICOM standard documentation.
- 📚 **Knowledge Tools**:
  - List and explore DICOM *CIUDs*, *modules*, and *attributes*
  - Look up detailed info on specific attributes
  - Find and explain UIDs quickly

## 🧪 Tech Stack

These servers are built with performance and local inference in mind:

| Component | Description |
|----------|-------------|
| 🧠 **LLM Engine** | [`Jan Nano 4B`](https://github.com/janhq/jan) – a lightweight, local LLM |
| ⚙️ **Server Framework** | [`fastMCP`](https://github.com/grobian/fastmcp) – fast, minimal LLM HTTP API |
| 📦 **Vector DB** | [DuckDB](https://duckdb.org) – efficient, in-process database |
| 🧩 **Embeddings** | `all-MiniLM-L6-v2` via [`llama-index`](https://github.com/jerryjliu/llama_index) |
| 🧠 **Chunking** | Optional AI-assisted chunk context generation for better retrieval quality |


## 🚀 Getting Started

The project is managed using *uv*. You can start the server using `uv run dicom-knowledge-mcp`. To run in Jan.ai run `uv build`, followed by `uv tools install`. Afterwards it can be used with `uvx dicom-knowledge-mcp`.

## 🙌 Acknowledgements

- [Jan LLM](https://github.com/janhq/jan)
- [fastMCP](https://github.com/grobian/fastmcp)
- [LlamaIndex](https://github.com/jerryjliu/llama_index)
- [DuckDB](https://duckdb.org)
- [MiniLM](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [SentenceTransformer 🤗](https://huggingface.co/sentence-transformers)
