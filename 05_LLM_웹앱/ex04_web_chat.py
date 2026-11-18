# ex04_web_chat.py : 웹 페이지(HTML) + 챗봇 API 를 함께 제공하는 서버
# 실행 후 브라우저에서: http://127.0.0.1:8000  (이 폴더에서 실행해야 static 폴더를 찾아요)
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse    # 파일(HTML)을 그대로 보내 주는 도구
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from common import get_llm

app = FastAPI()
template = ChatPromptTemplate.from_messages([
    ("system", "너는 친절한 상담원이야. 세 문장 이내로 답해."),
    ("human", "{message}"),
])
chain = template | get_llm(temperature=0.3) | StrOutputParser()


class ChatRequest(BaseModel):
    message: str


@app.get("/")                     # ① 주소 "/" → 채팅 화면(HTML 파일)을 보내 줘요
def home():
    return FileResponse("static/ex04_chat.html")


@app.post("/chat")                # ② 화면의 JavaScript 가 질문을 보내는 곳
def chat(request: ChatRequest):
    answer = chain.invoke({"message": request.message})
    return {"answer": answer}


uvicorn.run(app, host="127.0.0.1", port=8000)
