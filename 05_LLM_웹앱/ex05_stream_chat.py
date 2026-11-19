# ex05_stream_chat.py : 답을 만들어지는 대로 화면에 조금씩 보여 주는 챗봇 (스트리밍)
# 실행 후 브라우저에서: http://127.0.0.1:8000
# ── 전체 흐름 ──────────────────────────────────────────────
# ① "/" → 스트리밍 화면(static/ex05_stream.html) 보내기
# ② 화면이 POST /chat-stream 으로 질문 → 서버는 chain.stream 의 조각을 생기는 대로 바로바로 보냄
# ③ 화면은 조각이 올 때마다 읽어서 답 칸에 이어 붙임 (ex04 는 다 만든 뒤 한 번에 보냈어요)
# ────────────────────────────────────────────────────────
import uvicorn                                              # 서버 실행 프로그램
from fastapi import FastAPI                                 # 웹 서버 도구
from fastapi.responses import FileResponse, StreamingResponse   # 조금씩 보내는 응답
from langchain_core.output_parsers import StrOutputParser   # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate       # 질문 틀
from pydantic import BaseModel                              # 받을 데이터 모양

from common import get_llm                                  # AI 를 만드는 함수

app = FastAPI()
template = ChatPromptTemplate.from_messages([
    ("system", "너는 친절한 상담원이야. 다섯 문장 이내로 답해."),
    ("human", "{message}"),
])
chain = template | get_llm(temperature=0.3) | StrOutputParser()


class ChatRequest(BaseModel):
    message: str


@app.get("/")                     # ① 화면 보내기
def home():
    return FileResponse("static/ex05_stream.html")


@app.post("/chat-stream")         # ② 스트리밍으로 답하는 주소
def chat_stream(request: ChatRequest):
    pieces = chain.stream({"message": request.message})   # 답 조각을 차례로 내주는 통로 (Part 04 의 stream)
    return StreamingResponse(pieces, media_type="text/plain; charset=utf-8")   # 조각이 생길 때마다 보내요


uvicorn.run(app, host="127.0.0.1", port=8000)   # 서버 켜기
