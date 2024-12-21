import requests
import streamlit as st

# Ollama API Endpoint
OLLAMA_API_URL = "http://localhost:11434/api/chat"

# Streamlit App
st.title("Chatbot using Llama3")

# User Input
prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            try:
                # Prepare the request payload
                payload = {
                    "model": "llama3.2:latest",  # Specify your model
                    "messages": [{"role": "user", "content": prompt}]
                }

                # Send the request to the Ollama endpoint
                response = requests.post(OLLAMA_API_URL, json=payload)

                # Handle the response
                if response.status_code == 200:
                    data = response.json()
                    st.write("Chatbot Response:", data.get("response", "No response received"))
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")

            except Exception as e:
                st.error(f"An error occurred: {e}")
