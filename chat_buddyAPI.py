import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# ---------- CONFIG ----------
st.set_page_config(page_title="T.H.O.R 🤖", layout="centered")
st.title("🤖 T.H.O.R Chatbot")

load_dotenv()
GROQ_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_KEY:
    st.error("GROQ_API_KEY not found in .env")
    st.stop()

client = Groq(api_key=GROQ_KEY)

# ---------- MEMORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a God of Thunder."}
    ]

# ---------- DISPLAY CHAT ----------
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- INPUT ----------
if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",  # Updated model
                messages=st.session_state.messages,
                temperature=0.7
            )
            answer = response.choices[0].message.content
            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
