# DeepSeek Chat with Ollama

This project provides:
- A **FastAPI REST API** for chatting with `deepseek-r1:1.5b`
- A **Command-Line Chat** interface

## 🚀 Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure **Ollama** server is running:
```bash
ollama serve
```

3. Run the API:
```bash
uvicorn app:app --reload --port 8000
```

4. Run the CLI chat:
```bash
python cli_chat.py
```

## 🛠️ API Example
```bash
curl -X POST "http://127.0.0.1:8000/chat" -H "Content-Type: application/json" \
    -d '{"prompt": "Hello AI"}'
```
