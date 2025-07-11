from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline


def build_rag_chain(vectordb, hf_pipeline):
    llm=HuggingFacePipeline(pipeline=hf_pipeline)
    retriever=vectordb.as_retriever(search_kwargs={"k":3})
    rag_chain= RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return rag_chain