# ex02_ask_api.py : 주소에 질문을 담아 보내면 AI 가 답하는 API
# 실행 후 브라우저에서: http://127.0.0.1:8000/ask?question=하늘은 왜 파래?
# 흐름: 브라우저 → /ask?question=… → ask 함수가 question 을 AI 에게 보냄 → {질문, 답} JSON 으로 돌려줌
import uvicorn                    # 서버 실행 프로그램
from fastapi import FastAPI       # 웹 서버 도구

from common import get_llm        # AI 를 만드는 함수

app = FastAPI()                   # 앱 만들기
llm = get_llm(temperature=0.3, max_tokens=300)   # 서버가 켜질 때 AI 를 한 번만 준비해요


@app.get("/ask")                  # GET 방식으로 /ask 에 오면
def ask(question: str):           # 주소의 ?question=... 값이 question 변수에 들어와요
    answer = llm.invoke(question)                            # AI 에게 묻기
    return {"question": question, "answer": answer.content}  # 사전 → JSON


uvicorn.run(app, host="127.0.0.1", port=8000)   # 서버 켜기
