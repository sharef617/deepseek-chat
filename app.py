from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "deepseek-r1:1.5b"

@app.get("/")
def root():
    return {"message": "DeepSeek Chat API is running!"}

@app.post("/chat")
def chat_with_deepseek(prompt: str):
    payload = {"model": MODEL_NAME, "prompt": prompt}
    response = requests.post(OLLAMA_URL, json=payload)
    return {"response": response.json()}
