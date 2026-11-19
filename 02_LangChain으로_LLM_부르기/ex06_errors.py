# ex06_errors.py : 오류가 나도 프로그램이 멈추지 않게 — try / except
# 흐름: ① 일부러 틀린 키로 AI 만들기 → ② try 안에서 부르기 → ③ 오류 종류에 맞는 안내 문장 출력
import os                                    # 환경 변수 읽기

import openai                                # 오류 종류(AuthenticationError 등)가 들어 있어요
from dotenv import find_dotenv, load_dotenv  # .env 읽기
from langchain_openai import ChatOpenAI      # AI 모델 도구

load_dotenv(find_dotenv())                   # .env 파일 읽기

# ① 일부러 틀린 키로 AI 를 만들어요
wrong_llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),
    base_url=os.getenv("LLM_BASE_URL"),
    api_key="sk-or-v1-wrong-key",            # 틀린 키
    max_retries=0,                # 실패하면 다시 시도하지 않기 (오류를 바로 보려고)
)

try:                                          # ② 오류가 날 수 있는 일은 try 안에서
    wrong_llm.invoke("안녕?")
    print("성공")                             # 오류가 없으면 여기까지 실행
except openai.AuthenticationError:            # ③ 키가 틀렸을 때 (401)
    print("키가 틀렸어요. .env 의 LLM_API_KEY 를 확인하세요. (401)")
except openai.RateLimitError:                 #    너무 자주 불렀을 때 (429)
    print("요청이 너무 많아요. 잠시 뒤에 다시 해 보세요. (429)")
