# 정답_문제2.py : 긴 글을 붙여 넣고 [요약하기] 를 누르면 세 줄로 요약해 주는 웹 앱
# 실행 후 브라우저에서: http://127.0.0.1:8000
# 흐름: "/" → 요약 화면 보내기 / 화면이 POST /summary {"text": …} → 요약 체인 실행 → {"summary": …}
import uvicorn                                              # 서버 실행 프로그램
from fastapi import FastAPI                                 # 웹 서버 도구
from fastapi.responses import FileResponse                  # HTML 파일 보내기
from langchain_core.output_parsers import StrOutputParser   # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate       # 질문 틀
from pydantic import BaseModel                              # 받을 데이터 모양

from common import get_llm                                  # AI 를 만드는 함수

app = FastAPI()
template = ChatPromptTemplate.from_template("다음 글을 초등학생도 알 수 있게 세 줄로 요약해. 줄마다 '- ' 로 시작해.\n\n{text}")
chain = template | get_llm(temperature=0) | StrOutputParser()   # 요약 체인


class SummaryRequest(BaseModel):  # 화면이 보내는 모양: {"text": "..."}
    text: str


@app.get("/")                     # 요약 화면 보내기
def home():
    return FileResponse("static/정답_문제2.html")


@app.post("/summary")             # 요약 요청 받기
def summary(request: SummaryRequest):
    return {"summary": chain.invoke({"text": request.text})}   # 요약해서 바로 돌려주기


uvicorn.run(app, host="127.0.0.1", port=8000)   # 서버 켜기
