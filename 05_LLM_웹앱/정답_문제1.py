# 정답_문제1.py : 번역 API — POST /translate 에 {"text": ..., "language": ...} 를 보내면 번역해 줘요
# 실행 후 브라우저에서: http://127.0.0.1:8000/docs
import uvicorn
from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel

from common import get_llm

app = FastAPI()
template = ChatPromptTemplate.from_template("다음 글을 {language}로 자연스럽게 번역해. 번역문만 써.\n\n{text}")
chain = template | get_llm(temperature=0) | StrOutputParser()


class TranslateRequest(BaseModel):
    text: str                     # 번역할 글
    language: str = "영어"        # 어떤 말로? (안 보내면 영어)


@app.post("/translate")
def translate(request: TranslateRequest):
    result = chain.invoke({"text": request.text, "language": request.language})
    return {"language": request.language, "result": result}


uvicorn.run(app, host="127.0.0.1", port=8000)
