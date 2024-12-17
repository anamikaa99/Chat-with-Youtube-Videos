FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose necessary ports
EXPOSE 8001  
EXPOSE 8501  

# Command to start FastAPI and Streamlit
CMD uvicorn app:app --host 0.0.0.0 --port 8001 & streamlit run client.py --server.port 8501 --server.address 0.0.0.0