# 🤖 LLM Chatbots — From Zero to RAG

A collection of chatbot projects showcasing the progression from a simple embedding-based study bot to a full-fledged RAG (Retrieval Augmented Generation) chatbot — built with Python, Streamlit, LangChain, and more.

## 💡 Motivation

Building chatbots can seem daunting, but it doesn't have to be. This repository demonstrates three progressive approaches to chatbot development:

1. **No LLM approach** — Pure semantic search using embeddings
2. **Local LLM approach** — Full RAG with local models (no cloud dependencies)
3. **Cloud API approach** — Leveraging powerful cloud LLMs with minimal setup

Whether you're exploring vector databases, learning RAG architecture, or building production-ready chatbots, you'll find practical examples here.

## 📂 Projects

### 1. `simple.py` — Study Bot (No LLM / No API)
A lightweight study assistant that uses **sentence-transformers** and **ChromaDB** to index your notes (PDF, PPTX, TXT) and retrieve the most relevant passages using semantic search — **no LLM or API required**.

**Tech:** Streamlit, SentenceTransformers, ChromaDB, PyPDF

### 2. `ollam_bot.py` — Local RAG ChatBuddy (Ollama)
A fully local RAG chatbot powered by **Ollama** (phi3 model). Upload documents (PDF, PPTX, DOCX, TXT), and chat with them using conversational memory — all running on your machine, **no cloud APIs needed**.

**Tech:** Streamlit, LangChain, Ollama, HuggingFace Embeddings, ChromaDB

### 3. `chat_buddyAPI.py` — T.H.O.R Chatbot (Groq Cloud API)
A cloud-powered chatbot using the **Groq API** with the Llama 3.3 70B model. Fast inference with conversational memory — requires a Groq API key.

**Tech:** Streamlit, Groq SDK, Llama 3.3 70B

## 🚀 Quick Start

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

## 💬 Usage

### Study Bot (No API needed)
```bash
streamlit run simple.py
```
- Upload your notes (PDF, PPTX, TXT)
- Ask questions and get relevant passages retrieved via semantic search

### Local RAG ChatBuddy (Needs Ollama running)
```bash
streamlit run ollam_bot.py
```
- Make sure Ollama is running: `ollama serve`
- Upload documents and chat with full RAG capabilities
- Conversations are kept in memory during the session

### T.H.O.R Chatbot (Needs Groq API key)
```bash
streamlit run chat_buddyAPI.py
```
- Add your Groq API key to `.env`
- Upload documents and chat with Llama 3.3 70B
- Fastest inference thanks to Groq's LPU

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

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository** and create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and test thoroughly

3. **Commit with a clear message**:
   ```bash
   git commit -m "Add: description of your changes"
   ```

4. **Push to your fork** and create a **Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```

### Areas for Contribution
- Add support for more document types (DOCX, RTF, etc.)
- Implement additional LLM providers
- Improve UI/UX in Streamlit
- Add unit tests
- Enhance documentation
- Bug fixes and performance optimizations

## 📝 License

MIT
