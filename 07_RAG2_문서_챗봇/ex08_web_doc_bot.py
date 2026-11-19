# ex08_web_doc_bot.py : 문서 챗봇 웹 앱 — Part 05 의 웹 화면 + Part 07 의 문서 RAG
# 실행 후 브라우저에서: http://127.0.0.1:8000  (먼저 ex04_build_store.py 를 실행해 두세요)
# 흐름: 서버가 켜질 때 저장소를 한 번 불러오기 → "/" 화면 보내기
#       → 화면이 POST /ask {"question": …} → ask() 로 답 · 쪽 목록 → {"answer", "pages"} 돌려주기
import uvicorn                                # 서버 실행 프로그램
from fastapi import FastAPI                   # 웹 서버 도구
from fastapi.responses import FileResponse    # HTML 파일 보내기
from pydantic import BaseModel                # 받을 데이터 모양

from doc_tools import ask, load_store         # 문서 챗봇 함수 · 저장소 불러오기

app = FastAPI()
store = load_store()                          # 서버가 켜질 때 저장소를 한 번만 불러와요


class Question(BaseModel):                    # 화면이 보내는 모양: {"question": "..."}
    question: str


@app.get("/")                                 # 질문 화면 보내기
def home():
    return FileResponse("static/doc_bot.html")


@app.post("/ask")                             # 질문 받기
def ask_api(request: Question):
    answer, pages = ask(store, request.question)
    return {"answer": answer, "pages": pages}   # 답과 찾아본 쪽을 함께 보내요


uvicorn.run(app, host="127.0.0.1", port=8000)   # 서버 켜기
