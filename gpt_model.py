from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def get_llama_response(retriever, prompt, user_input):
    # En güncel Llama modelini kullanıyoruz
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.3)
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "input": RunnablePassthrough()}
        | prompt 
        | llm 
        | StrOutputParser()
    )
    return chain.invoke(user_input)