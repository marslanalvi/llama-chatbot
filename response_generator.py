import ollama


def generate_response(messages):
    """
    Generates a response from the Ollama model in a streaming manner.

    Args:
        messages (list): List of chat messages.

    Yields:
        str: A token of the assistant's response.
    """
    response = ollama.chat(model='llama3.2:latest', stream=True, messages=messages)
    for partial_resp in response:
        yield partial_resp["message"]["content"]
