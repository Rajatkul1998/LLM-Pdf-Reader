import streamlit as st
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings,HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import GooglePalm
from htmltemplates import css, bot_template, user_template

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

def get_text_chunks(raw_text):
    
    text_splitter=CharacterTextSplitter(separator="\n",chunk_size=1000,chunk_overlap=200,length_function=len)
    chunks=text_splitter.split_text(raw_text)
    return chunks

def get_vectors(text_chunks):
    # embeddings=OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings()
    vectorstore=FAISS.from_texts(texts=text_chunks,embedding=embeddings)
    return vectorstore
    
def get_conversation_chain(vectorstore):
    api_key="AIzaSyCP1VVKzStJW-PKhvEzjChUCKpKeKtSyBY"
    llm=GooglePalm(google_api_key=api_key,temperature=0.7)
    memory=ConversationBufferMemory(memory_key="chat_history",return_messages=True)
    conversation_chain=ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    
    msg=st.session_state.chat_history[-1]
    st.write(msg.content)

    # for i, message in enumerate(st.session_state.chat_history):
    #     if i % 2 == 0:
    #         st.write(user_template.replace(
    #             "{{MSG}}", message.content), unsafe_allow_html=True)
    #     else:
    #         st.write(bot_template.replace(
    #             "{{MSG}}", message.content), unsafe_allow_html=True)
def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with PDF Content",page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.coversation=None
        
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
        
    st.header("Chat with Multiple PDFs")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)
   
    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs=st.file_uploader("Upload PDFs and click on process",accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                raw_text=get_pdf_text(pdf_docs)
                text_chunks=get_text_chunks(raw_text)
                vectorstore=get_vectors(text_chunks)
                st.session_state.conversation=get_conversation_chain(vectorstore)
    
if __name__=="__main__":
    main()