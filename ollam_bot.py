import streamlit as st
import tempfile
from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    UnstructuredPowerPointLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory

from langchain_core.prompts import PromptTemplate

# ================= UI =================
st.set_page_config(page_title="Local RAG ChatBuddy", layout="centered")
st.title("📚 Context ChatBuddy — Multi-Doc RAG")

# ================= LLM =================
llm = Ollama(model="phi3:latest")

# ================= VECTOR STORE =================
@st.cache_resource
def get_vectorstore():
    emb = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma(
        persist_directory="./rag_store",
        embedding_function=emb
    )

# ================= PROMPT =================
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a precise study assistant.

Answer ONLY from the provided context.
If not found, say:
"I cannot find this in the provided material."

Context:
{context}

Question:
{question}

Answer clearly with headings if useful:
"""
)

# ================= MEMORY =================
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

# ================= CHAIN =================
def get_chain():
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=get_vectorstore().as_retriever(search_kwargs={"k": 5}),
        memory=st.session_state.memory,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

if "chain" not in st.session_state:
    st.session_state.chain = get_chain()

# ================= MULTI FILE UPLOAD =================
uploaded_files = st.file_uploader(
    "Upload PDFs / PPT / DOCX / TXT (multiple allowed)",
    type=["pdf", "pptx", "docx", "txt"],
    accept_multiple_files=True
)

if uploaded_files:
    vectordb = get_vectorstore()

    for uploaded in uploaded_files:
        with st.spinner(f"Indexing {uploaded.name} ..."):
            with tempfile.NamedTemporaryFile(delete=False) as tmp:
                tmp.write(uploaded.read())
                path = tmp.name

            # ---------- Loader selection ----------
            if uploaded.name.endswith(".pdf"):
                docs = PyPDFLoader(path).load()

            elif uploaded.name.endswith(".pptx"):
                docs = UnstructuredPowerPointLoader(path).load()

            elif uploaded.name.endswith(".docx"):
                docs = Docx2txtLoader(path).load()

            else:
                docs = TextLoader(path).load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            chunks = splitter.split_documents(docs)
            vectordb.add_documents(chunks)

            st.success(f"{uploaded.name} indexed ✅")

# ================= CHAT =================
if "messages" not in st.session_state:
    st.session_state.messages = []

for role, msg in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(msg)

if q := st.chat_input("Ask from your uploaded material..."):
    st.session_state.messages.append(("user", q))

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = st.session_state.chain({"question": q})
            ans = result["answer"]
            st.markdown(ans)

    st.session_state.messages.append(("assistant", ans))
