# ex02_ask_api.py : 주소에 질문을 담아 보내면 AI 가 답하는 API
# 실행 후 브라우저에서: http://127.0.0.1:8000/ask?question=하늘은 왜 파래?
import uvicorn
from fastapi import FastAPI

from common import get_llm

app = FastAPI()
llm = get_llm(temperature=0.3, max_tokens=300)   # 서버가 켜질 때 AI 를 한 번만 준비해요


@app.get("/ask")
def ask(question: str):           # 주소의 ?question=... 값이 question 변수에 들어와요
    answer = llm.invoke(question)
    return {"question": question, "answer": answer.content}


uvicorn.run(app, host="127.0.0.1", port=8000)
