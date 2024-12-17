# Chat-with-Youtube-Videos

Retrieval-Augmented Generation (RAG) application for interacting with YouTube video content. This project lets you transcribe YouTube videos, ask detailed questions about their content, and explore insightful answers powered by OpenAI's GPT-3.5 and Pinecone vector store.


## Features
- 🚀 YouTube Video Q&A: Extract insights and answers from YouTube video transcriptions.
- 🎤 On-Demand Transcription: Use Whisper AI to transcribe YouTube videos into text.
- ⚡ FastAPI Backend: A robust backend for handling transcription and Q&A queries.
- 🖥️ Streamlit Frontend: Interactive UI for querying video content and exploring answers.
- 🐳 Dockerized Deployment: Fully containerized with Docker for consistent performance across environments

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
  
## Dockerized Deployment 

1. Create a .env file for API keys

Store your API keys securely in a .env file in the root directory:
```plaintext
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```
2. Build the Docker Image

Run the following command to build the Docker image:
 ```bash
docker build -t rag-app .
```
3. Run the Container

Start the container using the .env file and map the ports
 ```bash
docker run -p 8001:8001 -p 8501:8501 --env-file .env rag-app
```
4. Access the app

- Streamlit Frontend: Open your browser and visit:
```plaintext
http://localhost:8501
```
- FastAPI Backend: Explore the API documentation:
```plaintext
http://localhost:8001/docs
```
  
## Deployment without Docker

1. Clone the repository:
 ```bash
git clone https://github.com/anamikaa99/Chat-with-Youtube-Videos.git
cd Chat-with-Youtube-Videos
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Create a .env file for API keys:
```plaintext
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```
4. Start the FastAPI Backend
Run the backend server to handle queries and transcriptions:
```bash
python app.py
```
By default, the backend runs at http://0.0.0.0:8001.

5. Launch the Streamlit client
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

