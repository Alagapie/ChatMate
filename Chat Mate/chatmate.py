import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

api_key=st.secrets["general"]["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
generation_config={
    "temperature":0.8,
    "top_k":40,
    "top_p":0.8
}
model=genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config)
st.set_page_config(
    page_icon=":brain:",
    page_title="Alagapie chatbot",
    layout="centered"
)
st.title("🤖 Alagapie - ChatBot")
def streamlit_role(user_role):
    if user_role=="model":
        return "assistant"
    else:
        return user_role
if "chat_session" not in st.session_state:
    st.session_state.chat_session=model.start_chat(history=[])
if st.button("Start a New Chat"):
    st.session_state.chat_session = model.start_chat(history=[])
for message in st.session_state.chat_session.history:
    with st.chat_message(streamlit_role(message.role)):
        st.markdown(message.parts[0].text)

prompt=st.chat_input("Ask Alagapie chatbot anything ")
if prompt:
    st.chat_message('user').markdown(prompt)
    
    with st.spinner("Generating response..."):
            response = st.session_state.chat_session.send_message(prompt)
          

    with st.chat_message("assistant"):
      st.markdown(response.text)



