
from ui import launch_tkinter_ui
'''
from llm_model import load_mistral_model
from llm_model import load_flan_model
from doc_loader import load_and_index_document
from rag_chain import build_rag_chain


def chat():
    print("🔍 Loading model...")
    #hf_pipeline = load_mistral_model()
    hf_pipeline=load_flan_model()


    print("📄 Indexing your document...")
    vectordb = load_and_index_document("sample.pdf")

    rag_chain = build_rag_chain(vectordb, hf_pipeline)
    #hf_pipeline=load_flan_model()

    print("💬 Ask questions about your document (type 'exit' to quit):")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            break
        answer = rag_chain.run(query)
        print(f"Bot: {answer}\n")

if __name__ == "__main__":
    chat()
'''

if __name__ == "__main__":
    launch_tkinter_ui()