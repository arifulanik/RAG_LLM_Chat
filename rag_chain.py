from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_community.llms import HuggingFacePipeline
from langchain.memory import ConversationSummaryBufferMemory

memory = None

def build_rag_chain(vectordb, hf_pipeline):
    global memory
    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    if vectordb is not None:
        retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    else:
        retriever = None

    if memory is None:
        memory = ConversationSummaryBufferMemory(
            llm=llm,
            memory_key="chat_history",
            return_messages=True
        )

    if retriever:
        rag_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=retriever,
            memory=memory,
            return_source_documents=False,
            verbose=True
        )
    else:
        # Fall back to simple llm chain with memory but no retriever
        from langchain.chains.conversation.base import ConversationChain
        rag_chain = ConversationChain(llm=llm, memory=memory, verbose=True)

    return rag_chain
