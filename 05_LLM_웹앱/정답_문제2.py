# 정답_문제2.py : 긴 글을 붙여 넣고 [요약하기] 를 누르면 세 줄로 요약해 주는 웹 앱
# 실행 후 브라우저에서: http://127.0.0.1:8000
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from common import get_llm

app = FastAPI()
template = ChatPromptTemplate.from_template("다음 글을 초등학생도 알 수 있게 세 줄로 요약해. 줄마다 '- ' 로 시작해.\n\n{text}")
chain = template | get_llm(temperature=0) | StrOutputParser()


class SummaryRequest(BaseModel):
    text: str


@app.get("/")
def home():
    return FileResponse("static/정답_문제2.html")


@app.post("/summary")
def summary(request: SummaryRequest):
    return {"summary": chain.invoke({"text": request.text})}


uvicorn.run(app, host="127.0.0.1", port=8000)
