# ex01_hello_api.py : FastAPI 로 만드는 첫 웹 서버
# 실행: python ex01_hello_api.py → 브라우저에서 http://127.0.0.1:8000 열기 (끄기: Ctrl + C)
# 흐름: ① 앱 만들기 → ② "/" 주소에 함수 연결 → ③ 서버 켜기 → 브라우저가 "/" 로 오면 함수의 답을 보내요
import uvicorn                    # 웹 서버를 실제로 돌려 주는 프로그램
from fastapi import FastAPI       # 웹 서버(API)를 쉽게 만드는 도구

app = FastAPI()                   # ① 웹 서버 앱 만들기


@app.get("/")                     # ② 주소 "/" 로 들어오면 바로 아래 함수를 실행해요
def home():
    return {"message": "안녕하세요! 첫 웹 서버예요."}   # 사전을 돌려주면 JSON 으로 보내 줘요


uvicorn.run(app, host="127.0.0.1", port=8000)   # ③ 내 컴퓨터의 8000번 문으로 서버 켜기
