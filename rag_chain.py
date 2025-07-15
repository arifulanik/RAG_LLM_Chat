from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from langchain.memory import ConversationSummaryMemory


def build_rag_chain(vectordb, hf_pipeline):
    llm=HuggingFacePipeline(pipeline=hf_pipeline)
    retriever=vectordb.as_retriever(search_kwargs={"k":3})

    memory=ConversationSummaryMemory(
        llm=llm,
        memory_key="Chat_history",
        return_messages=True
    )


    rag_chain= ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=False 
        )
    return rag_chain