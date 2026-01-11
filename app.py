from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from pydantic import BaseModel, Field


from graph import app as agent_app

app = FastAPI()

# ✅ MUST BE BEFORE ROUTES
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],   # includes OPTIONS
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    question: str
    user_id: str
    chat_history: List[str] = Field(default_factory=list)

class AskResponse(BaseModel):
    answer: str

@app.post("/ask")
def ask_agent(payload: AskRequest):
    result = agent_app.invoke({
        "question": payload.question,
        "user_id": payload.user_id,
        "chat_history": payload.chat_history
    })
    return {"answer": result["answer"]}

# ✅ ADD THIS (IMPORTANT)
@app.options("/ask")
def options_ask():
    return {}
