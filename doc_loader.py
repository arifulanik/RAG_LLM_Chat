from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
#from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def load_and_index_document(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents=loader.load()

    splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs=splitter.split_documents(documents)

    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb=FAISS.from_documents(docs,embeddings)

    return vectordb