import streamlit as st
import os
from dotenv import load_dotenv

# Yan dosyaları doğrudan import ediyoruz (Klasörleme yok)
from gemini_model import get_gemini_response
from gpt_model import get_llama_response

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(page_title="👨‍🍳 Şef Bot Karşılaştırma", layout="wide")
st.title("👨‍🍳 Akıllı Yemek Asistanı")

# 1. RAG Hazırlığı (Yerel Embedding - Ücretsiz ve Sorunsuz)
@st.cache_resource
def init_rag():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    # CSV dosyasını doğrudan ana dizinden oku
    loader = CSVLoader(file_path="yemek_tarifleri_tablosu.csv", encoding="utf-8")
    docs = loader.load()
    vectorstore = Chroma.from_documents(documents=docs, embedding=embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": 3})

retriever = init_rag()

# 2. ÖNCEDEN GİRİLİ SİSTEM PROMPTU (Niyet Yönetimi)
system_msg = (
    "Sen uzman bir şefsin. Aşağıdaki kurallara kesinlikle uy:\n"
    "1. Kullanıcı selam verirse neşeli bir şef gibi karşıla.\n"
    "2. Sadece yemekler ve yemek tarifleri hakkında konuş. Alakasız her soruyu nazikçe reddet.\n"
    "3. Kullanıcı 'sepete ekle' veya 'malzemeleri listele' derse, malzemeleri madde madde sun.\n"
    "4. Vedalaşırken afiyet dileyerek vedalaş.\n\n"
    "Bağlam (Tarif Veritabanı):\n{context}"
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_msg),
    ("human", "{input}")
])

# 3. ARAYÜZ
query = st.chat_input("Hangi yemeği sormak istersiniz?")

if query:
    st.info(f"Soru: {query}")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🤖 Google Gemini 2.5")
        with st.spinner("Gemini hazırlanıyor..."):
            res_gemini = get_gemini_response(retriever, prompt_template, query)
            st.markdown(res_gemini)
            
    with col2:
        st.subheader("⚡ Meta Llama 3.3 (Groq)")
        with st.spinner("Llama hazırlanıyor..."):
            res_llama = get_llama_response(retriever, prompt_template, query)
            st.markdown(res_llama)
