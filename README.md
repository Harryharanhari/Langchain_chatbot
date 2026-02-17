# 📄 PDF Context Chatbot (LangChain + Ollama + Streamlit)

A lightweight **PDF-based chatbot** that extracts content from a PDF, stores it as structured text (JSON-like chunks), and allows users to ask questions based strictly on the document context.

Built using:

* **LangChain**
* **Ollama (Local LLMs)**
* **Streamlit**
* **PyPDF**

---

# 🚀 Features

✅ Upload any PDF
✅ Automatic text extraction
✅ Smart text chunking
✅ Context-based Q&A
✅ Local LLM (no API cost)
✅ Simple Streamlit UI
✅ Privacy-friendly (runs locally)

---

# 🧠 How It Works

This project follows a **basic Retrieval-Augmented Generation (RAG)** workflow.

### Step 1 — PDF Processing

* PDF is uploaded
* Text is extracted using PyPDFLoader
* Text is split into chunks

### Step 2 — JSON Knowledge Base

* Each chunk is stored as structured data
* Acts as a mini knowledge base

### Step 3 — Context Retrieval

* User question is matched with relevant chunks
* Keyword-based scoring finds top matches

### Step 4 — LLM Answering

* Relevant context + question sent to Ollama
* Model answers ONLY from provided context

---

# 🛠️ Tech Stack

| Tool      | Purpose                |
| --------- | ---------------------- |
| LangChain | LLM pipeline framework |
| Ollama    | Run local LLMs         |
| Streamlit | Web UI                 |
| PyPDF     | PDF text extraction    |

---

# 📦 Installation

## 1️⃣ Clone Repo

```bash
git clone <your-repo-url>
cd <project-folder>
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Install Ollama

Download from:

[https://ollama.com](https://ollama.com)

---

## 5️⃣ Pull LLM Model

Recommended:

```bash
ollama pull phi3
```

or

```bash
ollama pull llama3
```

---

# ▶️ Running the App

```bash
streamlit run streamlit_app.py
```

Browser will open automatically.

---

# 📌 Usage

1. Upload a PDF
2. Click **Process PDF**
3. Ask questions related to the document
4. Get context-based answers

---

# ⚠️ Requirements

* Python **3.10 or 3.11 recommended**
* Ollama running locally
* Minimum 8GB RAM (for larger models)

---

# 🔮 Future Improvements

* Embedding-based semantic search
* FAISS/Chroma vector DB
* Chat memory
* Multi-PDF support
* Cloud deployment
* Streaming responses

---

# 🎯 Learning Outcomes

This project demonstrates:

* RAG architecture basics
* Document processing
* Context retrieval
* Local LLM integration
* Streamlit deployment

---

# 📜 License

MIT License
Free for learning and research.

---

# 🙌 Acknowledgements

* LangChain team
* Ollama
* Streamlit
* Open-source community

---

# 👨‍💻 Author

**Hari Haran**
AI & Data Science Student

Just say 👍
