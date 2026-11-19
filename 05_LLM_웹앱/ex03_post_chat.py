# ex03_post_chat.py : POST 로 질문을 받는 챗봇 API (/docs 화면에서 시험해요)
# 실행 후 브라우저에서: http://127.0.0.1:8000/docs
# ── 전체 흐름 ──────────────────────────────────────────────
# ① 상담원 체인 준비 (Part 03 그대로) → ② 받을 데이터 모양 ChatRequest 정하기
# ③ POST /chat 으로 {"message": "…"} 가 오면 → 체인에 넣어 답 → {"answer": "…"} 돌려주기
# ────────────────────────────────────────────────────────
import uvicorn                                              # 서버 실행 프로그램
from fastapi import FastAPI                                 # 웹 서버 도구
from langchain_core.output_parsers import StrOutputParser   # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate       # 질문 틀
from pydantic import BaseModel                              # 받을 데이터의 모양 정하기

from common import get_llm                                  # AI 를 만드는 함수

app = FastAPI()

template = ChatPromptTemplate.from_messages([                # ① 상담원 규칙 + 손님 말
    ("system", "너는 친절한 상담원이야. 세 문장 이내로 답해."),
    ("human", "{message}"),
])
chain = template | get_llm(temperature=0.3) | StrOutputParser()   # Part 03 의 체인 그대로


class ChatRequest(BaseModel):     # ② 받을 데이터의 모양: {"message": "..."}
    message: str


@app.post("/chat")                # ③ POST 방식으로 /chat 에 오면
def chat(request: ChatRequest):   # 보낸 JSON 이 request 에 담겨요 (모양이 틀리면 FastAPI 가 422 오류)
    answer = chain.invoke({"message": request.message})   # 체인 실행
    return {"answer": answer}                             # 답을 JSON 으로


uvicorn.run(app, host="127.0.0.1", port=8000)   # 서버 켜기
