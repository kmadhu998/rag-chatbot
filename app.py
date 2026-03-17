import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# 🔑 Add your API key here
os.environ["OPENAI_API_KEY"] = "your-api-key-here"

print("📄 Loading PDF...")
loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print("✂️ Splitting text...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
texts = text_splitter.split_documents(documents)

print("🧠 Creating embeddings...")
embeddings = OpenAIEmbeddings()

print("📦 Storing in FAISS...")
db = FAISS.from_documents(texts, embeddings)

print("🤖 Ready! Ask questions from your PDF\n")

qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0),
    retriever=db.as_retriever()
)

while True:
    query = input("Ask: ")
    if query.lower() == "exit":
        break
    
    answer = qa.run(query)
    print("\nAnswer:", answer, "\n")