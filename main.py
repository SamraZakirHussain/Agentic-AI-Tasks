from agents import Agent
import os
import requests
import json

BASE_URL = "https://openrouter.ai/api/v1"
MODEL = "mistralai/devstral-small:free"

API_KEY = os.getenv("OPENROUTER_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

data =  {
    "model": MODEL,
    "messages": [
        {
            "role": "user",
            "content": "What is the philosopy of individualism?"
        }
    ]
}


response = requests.post(f"{BASE_URL}/chat/completions", headers=headers, data=json.dumps(data))

print(response.json())
#for clear answer
data = response.json()
assistant_reply = data["choices"][0]["message"]["content"]
print(assistant_reply)

