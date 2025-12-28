from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def get_gemini_response(retriever, prompt, user_input):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # RAG Zinciri
    chain = (
        {"context": retriever | format_docs, "input": RunnablePassthrough()}
        | prompt 
        | llm 
        | StrOutputParser()
    )
    return chain.invoke(user_input)
