import openai
from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class Message(BaseModel):
    role: str  # "user" or "assistant"
    content: str

class ChatRequest(BaseModel):
    history: List[Message]

@app.post("/ask")
def ask_question(chat: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[msg.dict() for msg in chat.history]
        )
        answer = response.choices[0].message.content
        return {"answer": answer}
    except Exception as e:
        return {"answer": f"Error: {e}"}
