from fastapi import FastAPI
from langserve import add_routes
import uvicorn
import nest_asyncio
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
import tempfile
import whisper
from pytubefix import YouTube
from pytubefix.cli import on_progress
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
import os
from dotenv import load_dotenv



load_dotenv()

# USE YOUR OWN API KEYS
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

YOUTUBE_VIDEO = "https://www.youtube.com/watch?v=JN3KPFbWCy8"

app = FastAPI(
    title = "Youtube RAG",
    version = "1.0",
    description="A RAG app to talk about Youtube videos"
)

model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model= "gpt-3.5-turbo" )
parser = StrOutputParser()
template = """
Answer the question based on the context below. If you can't answer the question, reply "I don't know".

Context: {context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

# To create new transcription for your own video uncomment the code snippet below
# if not os.path.exists("transcription.txt"):
#     youtube = YouTube(YOUTUBE_VIDEO, on_progress_callback = on_progress)
#     print(youtube.title)
#     audio = youtube.streams.get_audio_only()

#     whisper_model = whisper.load_model("base")

#     with tempfile.TemporaryDirectory() as tmpdir:
#         file = audio.download(output_path=tmpdir)
#         transcription = whisper_model.transcribe(file, fp16 = False)["text"].strip()

#         with open("transcription.txt", "w") as file:
#             file.write(transcription)


#USE THE EXISTING TRANSCRIPTION FOR LEX FRIEDMAN'S CONVERSTATION WITH ELON MUSK
with open("transcription.txt") as file:
    transcription = file.read()

# transcription[:98]
    
loader = TextLoader("transcription.txt")
text_documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
documents = text_splitter.split_documents(text_documents)

embed = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY,
    model="text-embedding-3-large"
    # With the `text-embedding-3` class
    # of models, you can specify the size
    # of the embeddings you want returned.
    # dimensions=1024
)

index_name = "youtube-index"
pinecone = PineconeVectorStore.from_documents(documents, embed, pinecone_api_key= PINECONE_API_KEY,index_name=index_name)

chain = (
    {"context": pinecone.as_retriever(), "question": RunnablePassthrough()}
    | prompt
    | model
    | parser
)

add_routes(app, chain, path="/podcastprompt")

nest_asyncio.apply()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8001)