# Chatbot with Ollama AI (Llama 3.2)

## Project Name: **LlamaChatBot**

## Repository Name: **llama-chatbot**

### Introduction

Welcome to the **LlamaChatBot** project! This project leverages the **Ollama** API and **Streamlit** to build a responsive chatbot powered by the Llama 3.2 model. The bot streams its responses dynamically, providing a real-time chat experience. Users can interact with the bot, and it will respond in a conversational style, making it ideal for integration into various applications such as websites, helpdesks, and virtual assistants.

### Features

- **Real-time streaming responses**: The chatbot streams messages from the assistant in real-time.
- **User-friendly interface**: Built using **Streamlit**, the UI is simple and responsive, making it easy to integrate and use.
- **Session state management**: Maintains the conversation history between the user and the assistant.

### Prerequisites

Before you begin, ensure you have met the following requirements:

1. **Python 3.x** installed on your machine.
2. **Streamlit** and **Ollama** installed. You can install them using the following command:
   ```bash
   pip install -r requirements.txt

### Installation

Follow these steps to get the chatbot up and running on your local machine:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/marslanalvi/llama-chatbot.git
    cd llama-chatbot
    ```

2. **Install the required dependencies**: Make sure to install all necessary packages by running:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**: Use Streamlit to run the app. Execute the following command in your terminal:
    ```bash
    streamlit run app.py
    ```
    This will start a local server. Open the provided link (usually `http://localhost:8501`) in your browser to interact with the chatbot.

### Project Structure

This project consists of the following files:

- **app.py**: The main entry point of the chatbot, which initializes and runs the Streamlit app.
- **chat_ui.py**: Contains functions related to managing the chat interface, displaying the chat history, and adding messages.
- **response_generator.py**: Contains logic for generating responses using the Ollama API, with real-time streaming.
- **requirements.txt**: Contains a list of Python dependencies.

### How the Chatbot Works

The chatbot consists of several key components that work together to provide the user with a dynamic and interactive experience:

1. **Session Management**:
    - **initialize_session()**: Initializes the session state with default assistant messages.
    - **display_chat_history()**: Displays the entire conversation history between the user and the assistant.

2. **User Interaction**:
    - **add_user_message()**: When the user types a message, it gets appended to the conversation history.
    - **add_assistant_message_stream()**: This function streams the assistant's response from Ollama, updating the message in real-time.

3. **Response Generation**:
    - **generate_response()**: This function communicates with the Ollama API to generate responses based on the conversation history. It streams tokens one by one for dynamic display.

### How to Build Your Own Chatbot

To create your own chatbot with a similar setup, follow these steps:

1. **Set up your environment**:
    - Install Python (version 3.6 or later).
    - Install the required libraries (`Streamlit`, `Ollama`).

2. **Create a new Python file for the backend logic**:
    - Use the **response_generator.py** file as a template. This file communicates with the Ollama model and generates responses in real-time. You can replace the `llama3.2:latest` model with any other model available in Ollama.

3. **Design the chat UI**:
    - Use **Streamlit** to build the front end. The **chat_ui.py** file handles the chat history and dynamic message streaming. You can customize the UI by modifying the `initialize_session()`, `display_chat_history()`, and `add_assistant_message_stream()` functions.

4. **Modify `app.py` to integrate the backend and frontend**:
    - The `app.py` file is where the backend (response generation) and frontend (chat UI) meet. It handles user inputs, displays messages, and triggers the generation of responses.

5. **Deploy the app**:
    - Once you're happy with the chatbot, you can deploy the app using **Streamlit Sharing** or any cloud service that supports Python applications (such as Heroku, AWS, or Google Cloud).