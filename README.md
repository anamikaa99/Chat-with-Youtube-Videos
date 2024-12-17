# Chat-with-Youtube-Videos

Retrieval-Augmented Generation (RAG) application for interacting with YouTube video content. This project lets you transcribe YouTube videos, ask detailed questions about their content, and explore insightful answers powered by OpenAI's GPT-3.5 and Pinecone vector store.


## Features
- 🚀 YouTube Video Q&A: Extract insights and answers from YouTube video transcriptions.
- 🎤 On-Demand Transcription: Use Whisper AI to transcribe YouTube videos into text.
- ⚡ FastAPI Backend: A robust backend for handling transcription and Q&A queries.
- 🖥️ Streamlit Frontend: Interactive UI for querying video content and exploring answers.
- 🐳 Dockerized Deployment: Fully containerized with Docker for consistent performance across environments

  ---

## **Project Structure**

```plaintext
Chat-with-Youtube-Videos/
├── app.py                     # FastAPI backend for transcription & Q&A
├── client.py                  # Streamlit frontend for interactive Q&A
├── transcription.txt          # Sample transcription file for querying
├── requirements.txt           # Dependencies for the app
├── Dockerfile                 # Dockerfile to containerize the app
└── .gitignore                 # Files to ignore in version control
```

---

## How it works
1. Transcription: Whisper AI transcribes video content into text.
2. Chunking & Embedding: Transcriptions are split into smaller chunks and embedded using OpenAI's embedding models.
3. Querying: User questions are mapped to relevant chunks using Pinecone's vector search, generating contextual answers.
4. Response Generation: The app uses OpenAI GPT-3.5 to answer user queries based on the relevant transcriptions.

## Setup Instructions
### Prerequisites
- Python 3.9
- Docker and Docker Compose installed (Get Docker)
- Pinecone API Key
- OpenAI API Key

  
## Run the App with Docker

You can run the app directly from Docker Hub without cloning the repository.

### 1. Pull the Docker Image
Pull the latest image from Docker Hub:

```bash
docker pull anamikasingh99/rag-app:latest
```

---

### 2. Create a `.env` File
To securely pass API keys, create a `.env` file in your local directory with the following content:

```plaintext
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

Replace `your_openai_api_key` and `your_pinecone_api_key` with your actual API keys.

---

### 3. Run the Container
Run the container with port mappings and the `.env` file:

```bash
docker run -p 8001:8001 -p 8501:8501 --env-file .env anamikasingh/rag-app:latest
```

- **FastAPI Backend** will be accessible at:
  ```
  http://localhost:8001/docs
  ```

- **Streamlit Frontend** will be available at:
  ```
  http://localhost:8501
  ```

---


  
## Deployment without Docker

1. Clone the repository:
 ```bash
git clone https://github.com/anamikaa99/Chat-with-Youtube-Videos.git
cd Chat-with-Youtube-Videos
```
2. Create a .env file for API keys

Store your API keys securely in a .env file in the root directory:
```plaintext
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```


3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Start the FastAPI Backend
Run the backend server to handle queries and transcriptions:
```bash
python app.py
```
By default, the backend runs at http://0.0.0.0:8001.

4. Launch the Streamlit client
Run the client to interact with the app:
```bash
streamlit run client.py
```
The client opens at http://localhost:8501.

## Usage
## Ask Questions about a YouTube Video
- Open the Streamlit app.
- Input your question, e.g., "What does Elon Musk think about aliens?"
- The app queries the video's transcription and returns relevant answers.
## Transcribe New Videos
- Modify the YOUTUBE_VIDEO link in app.py with your desired video URL.
- Restart the backend server.
- The new transcription will be available for Q&A.

## Technologies Used
- FastAPI: Backend API framework.
- Streamlit: Frontend for user interaction.
- Whisper AI: State-of-the-art transcription model.
- Pinecone: Vector database for efficient retrieval.
- LangChain: Modular framework for building LLM-based applications.
- OpenAI GPT-3.5: Language model for contextual responses.
- Docker: For containerizing and deploying the app.

