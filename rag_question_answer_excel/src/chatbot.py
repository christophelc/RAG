import streamlit as st
from Rag import *

rag=Rag()
st.title("Flower assistant")

#initialize chat history
if "messages" not in st.session_state:
    messages = [message_init]
    st.session_state.messages = messages

#Display chat messages from history on app return
filtered_messages = [msg for msg in st.session_state.messages if msg["role"] != "system"]
for message in filtered_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    response = rag.query(prompt, history = st.session_state.messages)
    print(response)
    st.session_state.messages.append({"role":"user", "content": prompt})
    with st.chat_message("assistant"):
        st.markdown(response)
        st.session_state.messages.append({"role":"assistant", "content": response})
