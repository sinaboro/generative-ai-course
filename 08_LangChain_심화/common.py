# common.py : 심화 과정 공통 설정 — .env 를 읽어 LangChain 용 LLM · 임베딩을 만들어요
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
BASE_URL = os.getenv("LLM_BASE_URL", "https://openrouter.ai/api/v1")
API_KEY = os.getenv("LLM_API_KEY", "")
MODEL = os.getenv("LLM_MODEL", "openai/gpt-4o-mini")
EMBED_MODEL = os.getenv("EMBED_MODEL", "openai/text-embedding-3-small")


def get_llm(temperature=0):
    """LangChain 의 ChatOpenAI 를 OpenRouter 주소로 만들어요 (Part 03 의 OpenAI(...) 와 같은 설정)."""
    from langchain_openai import ChatOpenAI
    return ChatOpenAI(model=MODEL, base_url=BASE_URL, api_key=API_KEY, temperature=temperature)


def get_embeddings():
    """글을 숫자 목록(벡터)으로 바꾸는 임베딩 모델 (Part 06 에서 원리를 배워요)."""
    from langchain_openai import OpenAIEmbeddings
    # check_embedding_ctx_length=False: OpenRouter 모델 이름("openai/...")을 그대로 쓰기 위한 설정
    return OpenAIEmbeddings(model=EMBED_MODEL, base_url=BASE_URL, api_key=API_KEY,
                            check_embedding_ctx_length=False)
