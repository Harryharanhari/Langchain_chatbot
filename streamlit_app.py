import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
import tempfile
import os

# ========== PAGE CONFIG ==========
st.set_page_config(page_title="PDF Chatbot", layout="wide")
st.title("📄 PDF Chatbot (Cloud LLM)")

# ========== API KEY ==========
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# ========== FUNCTIONS ==========

def process_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        path = tmp.name

    loader = PyPDFLoader(path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(docs)

    return [chunk.page_content for chunk in chunks]


def find_context(question, data):
    q_words = question.lower().split()
    scored = []

    for chunk in data:
        score = sum(w in chunk.lower() for w in q_words)
        scored.append((score, chunk))

    scored.sort(reverse=True)

    top_chunks = [c for s,c in scored[:2] if s>0]

    # Limit size
    context = "\n".join(top_chunks)
    return context[:3000]



def ask_llm(question, context):
    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant"
    )

    messages = [
        ("system", "Answer only from provided context. If not found, say 'Not in document'."),
        ("human", f"Context:\n{context}\n\nQuestion: {question}")
    ]

    res = llm.invoke(messages)
    return res.content




# ========== SESSION STATE ==========

if "pdf_data" not in st.session_state:
    st.session_state.pdf_data = None

if "history" not in st.session_state:
    st.session_state.history = []


# ========== UI ==========

uploaded = st.file_uploader("Upload PDF", type="pdf")

if uploaded:
    if st.button("Process PDF"):
        with st.spinner("Processing..."):
            st.session_state.pdf_data = process_pdf(uploaded)
        st.success("PDF ready for chat!")

# ========== CHAT ==========

if st.session_state.pdf_data:

    q = st.text_input("Ask a question")

    if st.button("Ask") and q:
        context = find_context(q, st.session_state.pdf_data)

        if context:
            ans = ask_llm(q, context)
        else:
            ans = "No relevant info found."

        st.session_state.history.append((q, ans))

    for q,a in st.session_state.history:
        st.markdown(f"**🧑 You:** {q}")
        st.markdown(f"**🤖 Bot:** {a}")


