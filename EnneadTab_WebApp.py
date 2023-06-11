##
# 
# python -m streamlit run EnneadTab_WebApp.py

import os
import streamlit as st
import pickle
from PyPDF2 import PdfReader
#from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv
 
# Sidebar contents
with st.sidebar:
    st.title('🤗💬 EnneadTab GPT')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built using:
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
 
    ''')
    #add_vertical_space(5)
    st.write('This is a beta version.')
 
load_dotenv()
KEY = "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"


def main():
    st.header("Chat with QAQC report PDF 💬")
 
 
    # upload a PDF file
    pdf = st.file_uploader("Upload your report PDF", type='pdf')
 
    # st.write(pdf)
    if pdf is None:
        return

    pdf_reader = PdfReader(pdf)
    
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
        )
    chunks = text_splitter.split_text(text=text)

    # # embeddings
    store_name = pdf.name[:-4] # remove .pdf extension
    st.write(f'{store_name}')
    # st.write(chunks)

    if os.path.exists(f"{store_name}.pkl"):
        with open(f"{store_name}.pkl", "rb") as f:
            VectorStore = pickle.load(f)
        # st.write('Embeddings Loaded from the Disk')s
    else:
        embeddings = OpenAIEmbeddings(openai_api_key = KEY)
        VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        with open(f"{store_name}.pkl", "wb") as f:
            pickle.dump(VectorStore, f)

    # embeddings = OpenAIEmbeddings()
    # VectorStore = FAISS.from_texts(chunks, embedding=embeddings)

    # Accept user questions/query
    query = st.text_input("Ask questions about your QAQC report file:")
    # st.write(query)

    if not query:
        return
    
    docs = VectorStore.similarity_search(query=query, k=5)

    llm = OpenAI(openai_api_key = KEY)
    chain = load_qa_chain(llm=llm, chain_type="stuff")
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=query)
        print(cb)
    st.write(response)
 
if __name__ == '__main__':
    main()