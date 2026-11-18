# ex08_web_doc_bot.py : 문서 챗봇 웹 앱 — Part 05 의 웹 화면 + Part 07 의 문서 RAG
# 실행 후 브라우저에서: http://127.0.0.1:8000  (먼저 ex04_build_store.py 를 실행해 두세요)
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from doc_tools import ask, load_store

app = FastAPI()
store = load_store()                          # 서버가 켜질 때 저장소를 한 번만 불러와요


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return FileResponse("static/doc_bot.html")


@app.post("/ask")
def ask_api(request: Question):
    answer, pages = ask(store, request.question)
    return {"answer": answer, "pages": pages}   # 답과 찾아본 쪽을 함께 보내요


uvicorn.run(app, host="127.0.0.1", port=8000)
