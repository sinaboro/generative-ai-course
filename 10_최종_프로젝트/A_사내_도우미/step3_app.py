# step3_app.py : [3단계] 사내 도우미 웹 앱 (Part 05)
# 실행: python step3_app.py → http://127.0.0.1:8000  (먼저 step1_build_index.py 실행)
# 흐름: "/" → 채팅 화면 / 화면이 POST /chat {"user_id", "message"} → answer() → {"answer", "tools"}
import uvicorn                                # 서버 실행 프로그램
from fastapi import FastAPI                   # 웹 서버 도구
from fastapi.responses import FileResponse    # HTML 파일 보내기
from pydantic import BaseModel                # 받을 데이터 모양

from assistant import answer                  # 사내 도우미 함수

app = FastAPI()


class ChatRequest(BaseModel):
    user_id: str                  # 누가 묻는지 (사람마다 대화를 따로 기억해요)
    message: str


@app.get("/")                     # 채팅 화면 보내기
def home():
    return FileResponse("static/index.html")


@app.post("/chat")                # 질문 받기
def chat(request: ChatRequest):
    reply, tools_used = answer(request.user_id, request.message)
    return {"answer": reply, "tools": tools_used}   # 화면이 답과 🔧 도구 표를 보여 줘요


uvicorn.run(app, host="127.0.0.1", port=8000)   # 서버 켜기
