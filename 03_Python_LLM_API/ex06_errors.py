# ex06_errors.py : 오류 처리 — 잘못된 키 · 없는 모델 · 요청 너무 많음(429)
import os
import time

import openai
from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())
BASE = os.getenv("LLM_BASE_URL")
MSG = [{"role": "user", "content": "안녕"}]

# ① 잘못된 키 → 401 AuthenticationError
try:
    OpenAI(base_url=BASE, api_key="sk-or-v1-wrong-key").chat.completions.create(
        model=os.getenv("LLM_MODEL"), messages=MSG)
except openai.AuthenticationError as e:
    print("① 키가 틀렸어요:", e.status_code)

client = OpenAI(base_url=BASE, api_key=os.getenv("LLM_API_KEY"))

# ② 없는 모델 이름 → 400 또는 404
try:
    client.chat.completions.create(model="no-such/model-123", messages=MSG)
except (openai.BadRequestError, openai.NotFoundError) as e:
    print("② 모델 이름을 확인하세요:", e.status_code)


# ③ 요청이 많아 429 가 나면 잠깐 기다렸다가 다시 시도하는 함수
def ask_with_retry(messages, model, tries=3):
    for i in range(tries):
        try:
            r = client.chat.completions.create(model=model, messages=messages, max_tokens=50)
            return r.choices[0].message.content
        except openai.RateLimitError:
            wait = 2 ** i                       # 1초, 2초, 4초 … 점점 길게 기다리기
            print(f"   429: 요청이 많아요. {wait}초 기다렸다 다시 해요 ({i + 1}/{tries})")
            time.sleep(wait)
    return "(여러 번 시도했지만 실패했어요. 잠시 후 다시 해 보세요)"


print("③", ask_with_retry(MSG, os.getenv("LLM_MODEL")))
