# llm.py : LLM 을 쉽게 부르는 작은 도우미 (Part 02 부터 씀, 안의 원리는 Part 03 에서 배워요)
# - .env 의 LLM_BASE_URL · LLM_API_KEY · LLM_MODEL 을 읽어 OpenAI 형식 API 를 불러요 (OpenRouter · OpenAI 모두 가능)
# - 키가 없으면 "연습 모드" 로 정해 둔 답을 돌려줘서, 키가 없어도 코드는 끝까지 실행돼요
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())                       # 이 파일에서 위쪽 폴더로 올라가며 .env 를 찾아 읽어요

BASE_URL = os.getenv("LLM_BASE_URL", "https://openrouter.ai/api/v1")
API_KEY = os.getenv("LLM_API_KEY", "")
MODEL = os.getenv("LLM_MODEL", "openai/gpt-4o-mini")
MOCK = API_KEY in ("", "여기에_내_키를_붙여_넣기")  # 키가 없으면 연습 모드

_client = None


def client():
    """OpenAI 형식 클라이언트를 한 번만 만들어 다시 써요."""
    global _client
    if _client is None:
        from openai import OpenAI
        _client = OpenAI(base_url=BASE_URL, api_key=API_KEY)
    return _client


def chat(messages, model=None, temperature=0.7, max_tokens=500):
    """대화 목록(messages)을 보내고 답 글자만 돌려줘요."""
    if MOCK:
        last = messages[-1]["content"]
        return f"[연습 모드] 키가 없어서 정해 둔 답을 보여 줘요. (질문: {last[:30]}...)"
    r = client().chat.completions.create(
        model=model or MODEL, messages=messages,
        temperature=temperature, max_tokens=max_tokens,
    )
    return r.choices[0].message.content.strip()


def ask(prompt, system=None, model=None, temperature=0.7, max_tokens=500):
    """질문 하나를 보내고 답을 받아요. system 에는 AI 의 역할 · 규칙을 적어요."""
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    return chat(messages, model=model, temperature=temperature, max_tokens=max_tokens)
