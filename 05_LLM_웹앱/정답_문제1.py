# 정답_문제1.py : 번역 API — POST /translate 에 {"text": ..., "language": ...} 를 보내면 번역해 줘요
# 실행 후 브라우저에서: http://127.0.0.1:8000/docs
# 흐름: ① 번역 체인 준비 → ② 받을 모양(글 · 언어) 정하기 → ③ /translate 로 오면 체인 실행 후 결과 돌려주기
import uvicorn                                              # 서버 실행 프로그램
from fastapi import FastAPI                                 # 웹 서버 도구
from langchain_core.output_parsers import StrOutputParser   # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate       # 질문 틀
from pydantic import BaseModel                              # 받을 데이터 모양

from common import get_llm                                  # AI 를 만드는 함수

app = FastAPI()
template = ChatPromptTemplate.from_template("다음 글을 {language}로 자연스럽게 번역해. 번역문만 써.\n\n{text}")
chain = template | get_llm(temperature=0) | StrOutputParser()   # ① 빈칸 두 개짜리 체인


class TranslateRequest(BaseModel):  # ②
    text: str                     # 번역할 글
    language: str = "영어"        # 어떤 말로? (안 보내면 영어)


@app.post("/translate")           # ③
def translate(request: TranslateRequest):
    result = chain.invoke({"text": request.text, "language": request.language})   # 빈칸 채워 실행
    return {"language": request.language, "result": result}


uvicorn.run(app, host="127.0.0.1", port=8000)   # 서버 켜기
