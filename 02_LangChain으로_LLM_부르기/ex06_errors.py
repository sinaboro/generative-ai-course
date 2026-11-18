# ex06_errors.py : 오류가 나도 프로그램이 멈추지 않게 — try / except
import os

import openai
from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv())

# 일부러 틀린 키로 AI 를 만들어요
wrong_llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),
    base_url=os.getenv("LLM_BASE_URL"),
    api_key="sk-or-v1-wrong-key",
    max_retries=0,                # 실패하면 다시 시도하지 않기 (오류를 바로 보려고)
)

try:
    wrong_llm.invoke("안녕?")
    print("성공")
except openai.AuthenticationError:
    print("키가 틀렸어요. .env 의 LLM_API_KEY 를 확인하세요. (401)")
except openai.RateLimitError:
    print("요청이 너무 많아요. 잠시 뒤에 다시 해 보세요. (429)")
