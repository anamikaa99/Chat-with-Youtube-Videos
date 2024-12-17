import requests
import streamlit as st
import json


def get_response(input_text):
    try:
        # Send the input to FastAPI
        payload = {"input": input_text}
        response = requests.post(
            "http://host.docker.internal:8001/podcastprompt/invoke", # COMMENT THIS WHEN HOSTING ON LOCAL MACHINE WITHOUT DOCKER
            # "http://127.0.0.1:8001/podcastprompt/invoke", # UNCOMMENT THIS TO HOST ON YOUR LOCAL MACHINE WITHOUT DOCKER
            json=payload
        )
        response.raise_for_status()  # Raise an error for HTTP issues
        try:
            data = json.loads(response.text)  # Convert string to dictionary
            return data.get("output", "No content found.")  # Extract the 'output' field
        except json.JSONDecodeError:
            return "Unable to parse response as JSON."

    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Streamlit app
st.title("Q/A about Youtube video")
input_text = st.text_input("What would you like to know about the Lex Fridman Podcast with Elon Musk?")

if input_text:
    response = get_response(input_text)
    st.write("Response:")
    st.write(response)
