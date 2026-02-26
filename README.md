# 🤖 LLM Chatbots — From Zero to RAG

A collection of chatbot projects showcasing the progression from a simple embedding-based study bot to a full-fledged RAG (Retrieval Augmented Generation) chatbot — built with Python, Streamlit, LangChain, and more.

## 📂 Projects

### 1. `simple.py` — Study Bot (No LLM / No API)
A lightweight study assistant that uses **sentence-transformers** and **ChromaDB** to index your notes (PDF, PPTX, TXT) and retrieve the most relevant passages using semantic search — **no LLM or API key required**.

**Tech:** Streamlit, SentenceTransformers, ChromaDB, PyPDF

### 2. `ollam_bot.py` — Local RAG ChatBuddy (Ollama)
A fully local RAG chatbot powered by **Ollama** (phi3 model). Upload documents (PDF, PPTX, DOCX, TXT), and chat with them using conversational memory — all running on your machine, **no cloud APIs needed**.

**Tech:** Streamlit, LangChain, Ollama, HuggingFace Embeddings, ChromaDB

### 3. `chat_buddyAPI.py` — T.H.O.R Chatbot (Groq Cloud API)
A cloud-powered chatbot using the **Groq API** with the Llama 3.3 70B model. Fast inference with conversational memory — requires a Groq API key.

**Tech:** Streamlit, Groq SDK, Llama 3.3 70B

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) installed (for `ollam_bot.py`)

### Installation

```bash
# Clone the repo
git clone https://github.com/nishant-gupta911/LLM-chatbots.git
cd LLM-chatbots

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### Environment Setup

```bash
cp .env.example .env
# Edit .env and add your API keys
```

### Run

```bash
# Study Bot (no API needed)
streamlit run simple.py

# Local RAG ChatBuddy (needs Ollama running)
streamlit run ollam_bot.py

# T.H.O.R Chatbot (needs Groq API key)
streamlit run chat_buddyAPI.py
```

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Streamlit | Web UI |
| LangChain | RAG pipeline & memory |
| ChromaDB | Vector database |
| SentenceTransformers | Embeddings |
| Ollama | Local LLM inference |
| Groq | Cloud LLM inference |
| PyPDF / python-pptx | Document parsing |

## 📝 License

MIT
