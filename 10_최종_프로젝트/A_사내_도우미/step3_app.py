# step3_app.py : [3단계] 사내 도우미 웹 앱 (Part 05)
# 실행: python step3_app.py → http://127.0.0.1:8000  (먼저 step1_build_index.py 실행)
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from assistant import answer

app = FastAPI()


class ChatRequest(BaseModel):
    user_id: str                  # 누가 묻는지 (사람마다 대화를 따로 기억해요)
    message: str


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.post("/chat")
def chat(request: ChatRequest):
    reply, tools_used = answer(request.user_id, request.message)
    return {"answer": reply, "tools": tools_used}


uvicorn.run(app, host="127.0.0.1", port=8000)
