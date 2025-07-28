import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "deepseek-r1:1.5b"

def chat():
    print("🤖 DeepSeek CLI Chat (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = requests.post(OLLAMA_URL, json={
            "model": MODEL_NAME,
            "prompt": user_input
        })
        data = response.json()
        print("Bot:", data.get("response", "No response"))

if __name__ == "__main__":
    chat()
