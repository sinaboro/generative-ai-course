# ex05_stream_chat.py : 답을 만들어지는 대로 화면에 조금씩 보여 주는 챗봇 (스트리밍)
# 실행 후 브라우저에서: http://127.0.0.1:8000
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse   # 조금씩 보내는 응답
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from common import get_llm

app = FastAPI()
template = ChatPromptTemplate.from_messages([
    ("system", "너는 친절한 상담원이야. 다섯 문장 이내로 답해."),
    ("human", "{message}"),
])
chain = template | get_llm(temperature=0.3) | StrOutputParser()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return FileResponse("static/ex05_stream.html")


@app.post("/chat-stream")
def chat_stream(request: ChatRequest):
    pieces = chain.stream({"message": request.message})   # 답 조각을 차례로 내주는 통로 (Part 04 의 stream)
    return StreamingResponse(pieces, media_type="text/plain; charset=utf-8")   # 조각이 생길 때마다 보내요


uvicorn.run(app, host="127.0.0.1", port=8000)
