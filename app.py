import streamlit as st
from chat_ui import initialize_session, display_chat_history, add_user_message, add_assistant_message_stream
from response_generator import generate_response


# Initialize the chatbot
st.title("llama3.2 Chatbot")
initialize_session()

# Display chat history
display_chat_history()

# Handle user input
if prompt := st.chat_input():
    add_user_message(prompt)
    response_generator = generate_response(st.session_state.messages)
    add_assistant_message_stream(response_generator)
