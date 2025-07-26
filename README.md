# 🛠️ TINA - MCP Tools for an individualized assistant

This project includes two lightweight but powerful [fastMCP](https://github.com/grobian/fastmcp) servers built to solve real-world problems using local LLMs, smart embedding, and fast retrieval — all without the need for cloud dependencies. They are the result of an [opencampus.sh](https://edu.opencampus.sh/) LLM course work. TINA stands for *"TINA Is Not an Acronym"*  
The MCP servers were tested with [Jan.ai](https://jan.ai/) v0.6.5 and Jan Nano 4B.

---

## 🔧 Included Servers

### 1. 🥗 UKSH Mensa Tool

A handy tool to access and query the daily menu of the UKSH Mensa.

#### Features:
- 📄 **PDF Plan Parsing**: Automatically fetches and parses the weekly menu PDF from the Mensa website.
- 🤖 **Smart Q&A**: Ask questions like:  
  > “What vegetarian menu does the mensa serve today?”
- 📅 **Date Handling Tools** *(optional)*: Understands natural language dates like “next Friday” or “today”.
- ✅ **Useful every day!** (if you work at the UKSH Kiel 😜)

---

### 2. 🧠 DICOM Specialist

A specialized helper for navigating the complexity of the DICOM standard.

#### Features:
- 🔍 **RAG (Retrieval-Augmented Generation)** over the DICOM standard documentation.
- 📚 **Knowledge Tools**:
  - List and explore DICOM *CIUDs*, *modules*, and *attributes*
  - Look up detailed info on specific attributes
  - Find and explain UIDs quickly

---

## 🚀 Getting Started

Clone the repo and follow the instructions in each server's directory (`uksh-mensa/` and `dicom-specialist/`).  
Each is a standalone `fastMCP` server.

---

## 📂 Folder Structure
```
root
├── dicom-specialist
│   ├── dicom_db
│   │   └── embeddings.db
│   ├── dicom_docs
│   │   └── markdown
│   │       └── part01.md
│   ├── src
│   │   ├── dicom_knowledge_mcp
│   │   │   ├── __init__.py
│   │   │   ├── db_utils.py
│   │   │   ├── dicom_embeddings.ipynb
│   │   │   ├── keyword_search.py
│   │   │   └── server.py
│   │   └── client.py
│   ├── pyproject.toml
│   └── README.md
├── uksh-mensa
│   ├── src
│   │   └── uksh_mensa_mcp
│   │       ├── __init__.py
│   │       └── server.py
│   ├── pyproject.toml
│   └── README.md
├── LICENCE
└── README.md
```

---

## 🙌 Acknowledgements

- [Jan LLM](https://github.com/janhq/jan)
- [fastMCP](https://github.com/grobian/fastmcp)
- [LlamaIndex](https://github.com/jerryjliu/llama_index)
- [DuckDB](https://duckdb.org)
- [MiniLM](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [SentenceTransformer 🤗](https://huggingface.co/sentence-transformers)
- [Camelot](https://camelot-py.readthedocs.io)

---

## 📬 Feedback / Contributions

Pull requests, suggestions, and issues are welcome!