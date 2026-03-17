# 📄 RAG Chatbot using LangChain & FAISS

## 💡 Overview
This project is a Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions based on a PDF document.

## 🚀 Features
- Load and process PDF documents
- Semantic search using embeddings
- Accurate answers using LLM
- Fast retrieval using FAISS

## 🛠️ Tech Stack
- Python
- LangChain
- FAISS (Vector Database)
- OpenAI API

## ⚙️ How it Works
1. PDF is loaded and split into chunks
2. Text is converted into embeddings
3. Stored in FAISS vector database
4. User query is matched with relevant chunks
5. LLM generates answer using retrieved context

## ⚙️ How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Add your OpenAI API key in app.py

3. Add a PDF file named sample.pdf

4. Run:
   python app.py

## 🧠 Future Improvements
- Streamlit UI for better user experience
- Multiple PDF support
- Chat history memory
