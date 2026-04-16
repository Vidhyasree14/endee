# 🚀 AI Question Answering System using RAG + Endee Vector Database

## 📌 Overview
This project is an AI-powered Question Answering System built using a Retrieval-Augmented Generation (RAG) pipeline. It allows users to input custom data and ask questions, and the system retrieves relevant context using a vector database before generating accurate answers using an LLM.

---

## 🎯 Features
- 🔍 Semantic Search using embeddings
- 🧠 Context-aware AI responses
- ⚡ Fast retrieval using vector similarity
- 📚 Custom knowledge base support
- 💬 Simple interactive UI using Streamlit

---

## 🏗️ System Architecture
1. User inputs data (knowledge base)
2. Data is converted into vector embeddings
3. Embeddings are stored in Endee Vector Database
4. User asks a question
5. Query is embedded and matched with stored vectors
6. Relevant context is retrieved
7. LLM generates answer based on context

---

## 🛠️ Tech Stack
- Python
- Streamlit
- OpenAI API (Embeddings + LLM)
- Endee Vector Database
- NumPy

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
