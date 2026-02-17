# 📄 PDF Context-Aware Chatbot (RAG)  
### Built with LangChain, Streamlit, and Cloud LLMs

A context-aware PDF chatbot that allows users to upload documents and ask questions based strictly on the content of the uploaded file.

This project demonstrates a lightweight Retrieval-Augmented Generation (RAG) pipeline using modern LLM tooling and a simple, deployable Streamlit interface.

---

## 🚀 Features

- 📂 Upload any PDF document  
- 🔍 Automatic text extraction and chunking  
- 🧠 Context-based question answering  
- ☁️ Cloud LLM integration (Groq API)  
- 💬 Interactive chat interface  
- 🔒 Privacy-friendly (no data storage)

---

## 🧠 How It Works

This project follows a simple RAG workflow:

1. **PDF Upload**  
   - User uploads a document  
   - Text is extracted using PyPDFLoader  

2. **Text Chunking**  
   - Document split into smaller chunks  
   - Improves retrieval accuracy  

3. **Context Retrieval**  
   - Relevant chunks selected using keyword scoring  

4. **LLM Response**  
   - Context + question sent to cloud LLM  
   - Model answers only from document context  

---

## 🛠 Tech Stack

- **LangChain** – LLM orchestration  
- **Streamlit** – Web interface  
- **Groq API** – High-speed cloud LLM  
- **PyPDF** – PDF processing  

---

## 📦 Installation

### 1. Clone Repository
```bash
git clone <repo-url>
cd <folder>
