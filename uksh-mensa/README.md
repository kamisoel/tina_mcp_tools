# 🥗 UKSH Mensa Tool

A lightweight MCP server to access and query the daily menu of the UKSH Mensa.

---

## Features:
- 📄 **PDF Plan Parsing**: Automatically fetches and parses the weekly menu PDF from the Mensa website.
- 🤖 **Smart Q&A**: Ask questions like:  
  > “What vegetarian menu does the mensa serve today?”
- 📅 **Date Handling Tools** *(optional)*: Understands natural language dates like “next Friday” or “today”.
- ✅ **Useful every day!** (if you work at the UKSH Kiel 😜)

---

## 🚀 Getting Started

You may have to [install ghostscript](https://camelot-py.readthedocs.io/en/latest/user/install-deps.html) first for Camelot to run.

The project is managed using *uv*. You can start the server using `uv run uksh-mensa-mcp`. To run in Jan.ai run `uv build`, followed by `uv tools install`. Afterwards it can be used with `uvx uksh-mensa-mcp`.

---

## 🙌 Acknowledgements

- [Jan LLM](https://github.com/janhq/jan)
- [fastMCP](https://github.com/grobian/fastmcp)
---

## 📬 Feedback / Contributions

Pull requests, suggestions, and issues are welcome!