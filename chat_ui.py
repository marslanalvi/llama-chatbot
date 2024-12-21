import streamlit as st


def initialize_session():
    """Initializes the session state with a default assistant message."""
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Hi! Glad to have you here! How can I help you?"}]
    if "full_message" not in st.session_state:
        st.session_state["full_message"] = ""


def display_chat_history():
    """Displays the chat message history from the session state."""
    for msg in st.session_state.messages:
        avatar = "🧑‍💻" if msg["role"] == "user" else "🤖"
        st.chat_message(msg["role"], avatar=avatar).write(msg["content"])


def add_user_message(prompt):
    """Adds the user's message to the session state."""
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)


def add_assistant_message_stream(generator):
    """
    Streams the assistant's response token by token and updates the session state in real-time.
    """
    st.session_state["full_message"] = ""
    # Create a container for the assistant's response
    assistant_message_container = st.chat_message("assistant", avatar="🤖").container()
    response_placeholder = assistant_message_container.empty()  # Placeholder for dynamic updates

    # Stream tokens and update the response dynamically
    full_message = ""
    for token in generator:
        full_message += token
        response_placeholder.write(full_message)  # Dynamically update the assistant's response in real-time

    # Add the full response to session state after streaming completes
    st.session_state["full_message"] = full_message
    st.session_state.messages.append({"role": "assistant", "content": full_message})
