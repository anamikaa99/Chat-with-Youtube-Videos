# Chat-with-Youtube-Videos

Retrieval-Augmented Generation (RAG) application for interacting with YouTube video content. This project lets you transcribe YouTube videos, ask detailed questions about their content, and explore insightful answers powered by OpenAI's GPT-3.5 and Pinecone vector store.


## Features
- YouTube Video Q&A: Extract insights and answers from a YouTube video's transcript using a conversational interface.
- On-Demand Video Transcription: Upload or link new YouTube videos, and transcribe them with the Whisper AI module.
- FastAPI Backend: A robust backend powered by FastAPI and LangChain for seamless interaction.
- Streamlit Frontend: A user-friendly Streamlit app for exploring transcriptions and asking questions interactively.

## How it works
1. Transcription: Whisper AI transcribes video content into text.
2. Chunking & Embedding: Transcriptions are split into smaller chunks and embedded using OpenAI's embedding models.
3. Querying: User questions are mapped to relevant chunks using Pinecone's vector search, generating contextual answers.

## Setup Instructions
### Prerequisites
- Python 3.9 
- Pinecone API Key
- OpenAI API Key
### Installation
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
### Running the App
1. Start the FastAPI Backend
Run the backend server to handle queries and transcriptions:
```bash
python app.py
```
By default, the backend runs at http://127.0.0.1:8001.
2. Launch the Streamlit client
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

