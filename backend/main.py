from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

from chatbot import get_answer
from model_trainer import train_model
from judge import evaluate_model

app = FastAPI()

# Existing Chatbot route
class ChatRequest(BaseModel):
    history: List[Dict[str, str]]

@app.post("/ask")
def ask_question(request: ChatRequest):
    reply = get_answer(request.history)
    return {"response": reply}

# New: Model Training API
class TrainRequest(BaseModel):
    model_type: str  # "regression" or "classification"

@app.post("/train_model")
def train(train_req: TrainRequest):
    model, X_test, y_test = train_model(model_type=train_req.model_type)
    return {"message": f"{train_req.model_type.capitalize()} model trained successfully."}

# New: Judge API
class JudgeRequest(BaseModel):
    model_type: str

@app.post("/judge_model")
def judge(judge_req: JudgeRequest):
    model, X_test, y_test = train_model(model_type=judge_req.model_type)
    results = evaluate_model(model, X_test, y_test, model_type=judge_req.model_type)
    return {"evaluation": results}
