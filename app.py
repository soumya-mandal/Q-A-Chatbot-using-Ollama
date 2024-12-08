import streamlit as st
#import openai
#from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import ollama

import os
from dotenv import load_dotenv

load_dotenv()


###LangSmith Tracking

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACKING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = "Q&A ChatBOT using Ollama"


###Promp Templates

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful chatbot system, you need to help the user with information regarding the queries from the user."),
        ("user", "Question : {question}")
    ]
)

def generate_response(question, engine, temperature, max_tokens):
    #openai.api_key = api_key
    llm = Ollama(model = engine)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain.invoke({'question' : question})
    return answer

###Title of the app
st.title("Q&A Chatbot using Ollama")

###SideBar Menu
#st.sidebar.title("Setting")
#api_key = st.sidebar.text_input("Enter the API_KEY : ", type = "password")

###DropDown Menu
llm_options = ["mistral", "llama3.2:1b", "gemma2:2b", "moondream"]
engine = st.sidebar.selectbox("Select Language Model", llm_options)

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max_Tokens", 50, 500, 250)

###User Input
st.write("Ask me anything!!!")
user_input = st.text_input("You : ")

if user_input : 
    response = generate_response(user_input, engine, temperature, max_tokens)
    st.write(response)
else :
    st.write("You haven't entered any question.")