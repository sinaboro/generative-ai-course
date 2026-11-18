# ex03_post_chat.py : POST 로 질문을 받는 챗봇 API (/docs 화면에서 시험해요)
# 실행 후 브라우저에서: http://127.0.0.1:8000/docs
import uvicorn
from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from common import get_llm

app = FastAPI()

template = ChatPromptTemplate.from_messages([
    ("system", "너는 친절한 상담원이야. 세 문장 이내로 답해."),
    ("human", "{message}"),
])
chain = template | get_llm(temperature=0.3) | StrOutputParser()   # Part 03 의 체인 그대로


class ChatRequest(BaseModel):     # 받을 데이터의 모양: {"message": "..."}
    message: str


@app.post("/chat")                # POST 방식으로 /chat 에 오면
def chat(request: ChatRequest):   # 보낸 JSON 이 request 에 담겨요
    answer = chain.invoke({"message": request.message})
    return {"answer": answer}


uvicorn.run(app, host="127.0.0.1", port=8000)
