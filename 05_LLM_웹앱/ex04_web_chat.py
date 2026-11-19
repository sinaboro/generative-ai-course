# ex04_web_chat.py : 웹 페이지(HTML) + 챗봇 API 를 함께 제공하는 서버
# 실행 후 브라우저에서: http://127.0.0.1:8000  (이 폴더에서 실행해야 static 폴더를 찾아요)
# ── 전체 흐름 ──────────────────────────────────────────────
# ① 브라우저가 "/" 에 오면 → 채팅 화면(static/ex04_chat.html)을 보내 줘요
# ② 화면에서 [보내기] → 화면의 JavaScript 가 POST /chat 으로 질문을 보내요
# ③ 서버가 체인으로 답을 만들어 {"answer": …} 로 돌려주면 → 화면이 답을 보여 줘요
# ────────────────────────────────────────────────────────
import uvicorn                                              # 서버 실행 프로그램
from fastapi import FastAPI                                 # 웹 서버 도구
from fastapi.responses import FileResponse    # 파일(HTML)을 그대로 보내 주는 도구
from langchain_core.output_parsers import StrOutputParser   # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate       # 질문 틀
from pydantic import BaseModel                              # 받을 데이터 모양

from common import get_llm                                  # AI 를 만드는 함수

app = FastAPI()
template = ChatPromptTemplate.from_messages([                # 상담원 규칙 + 손님 말
    ("system", "너는 친절한 상담원이야. 세 문장 이내로 답해."),
    ("human", "{message}"),
])
chain = template | get_llm(temperature=0.3) | StrOutputParser()   # 틀 → AI → 글자


class ChatRequest(BaseModel):     # 화면이 보내는 데이터 모양: {"message": "..."}
    message: str


@app.get("/")                     # ① 주소 "/" → 채팅 화면(HTML 파일)을 보내 줘요
def home():
    return FileResponse("static/ex04_chat.html")


@app.post("/chat")                # ② 화면의 JavaScript 가 질문을 보내는 곳
def chat(request: ChatRequest):
    answer = chain.invoke({"message": request.message})   # ③ 답 만들기
    return {"answer": answer}


uvicorn.run(app, host="127.0.0.1", port=8000)   # 서버 켜기
