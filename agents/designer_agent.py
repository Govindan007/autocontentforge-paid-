import requests
import os
from dotenv import load_dotenv

load_dotenv()

def run_designer_agent(topic):
    prompt = f"Create a digital illustration for a blog post about: {topic}"
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}", "Content-Type": "application/json"},
        json={"prompt": prompt, "n": 1, "size": "512x512"}
    )
    return response.json()["data"][0]["url"]
