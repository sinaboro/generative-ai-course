# common.py : 이 과정의 모든 예제가 함께 쓰는 설정 파일
# .env 파일에서 주소 · 키 · 모델 이름을 읽어서, LangChain 의 LLM 을 만들어 줘요
# (이 파일의 내용은 Part 02 에서 한 줄씩 배워요. 지금은 get_llm() 만 쓸 줄 알면 돼요)
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())          # 위쪽 폴더로 올라가며 .env 파일을 찾아서 읽어요

BASE_URL = os.getenv("LLM_BASE_URL", "https://openrouter.ai/api/v1")   # 요청을 보낼 서버 주소
API_KEY = os.getenv("LLM_API_KEY", "")                                  # 내 API 키
MODEL = os.getenv("LLM_MODEL", "openai/gpt-4o-mini")                    # 쓸 모델 이름

# 키가 없거나 예시 글자 그대로면 "연습 모드" 로 돌아가요
PRACTICE_MODE = API_KEY == "" or API_KEY == "여기에_내_키를_붙여_넣기"


def get_llm(temperature=0.7, max_tokens=500, model=None):
    """LLM(대화형 AI 모델)을 만들어서 돌려줘요."""
    if PRACTICE_MODE:
        # 키가 없을 때: 진짜 AI 대신 정해 둔 답을 돌려주는 연습용 모델
        from langchain_core.language_models import FakeListChatModel
        return FakeListChatModel(responses=["[연습 모드] .env 에 API 키를 넣으면 진짜 AI 가 답해요."])

    from langchain_openai import ChatOpenAI
    if model is None:
        model = MODEL
    return ChatOpenAI(
        model=model,                # 모델 이름
        base_url=BASE_URL,          # 서버 주소 (OpenRouter)
        api_key=API_KEY,            # 내 키
        temperature=temperature,    # 답의 다양함 (0 = 늘 같은 답)
        max_tokens=max_tokens,      # 답의 최대 길이
    )


# ---------- Part 06 부터: 임베딩 (글 → 숫자 목록) ----------
EMBED_MODEL = os.getenv("EMBED_MODEL", "google/gemini-embedding-001")   # 임베딩 모델 이름


def get_embeddings():
    """글을 숫자 목록(벡터)으로 바꿔 주는 임베딩 모델을 만들어요."""
    if PRACTICE_MODE:
        # 키가 없을 때: 글자에 따라 정해진 가짜 숫자를 만들어요 (실행은 되지만 뜻은 반영 안 돼요)
        from langchain_core.embeddings import DeterministicFakeEmbedding
        return DeterministicFakeEmbedding(size=256)

    from langchain_openai import OpenAIEmbeddings
    return OpenAIEmbeddings(
        model=EMBED_MODEL,
        base_url=BASE_URL,
        api_key=API_KEY,
        check_embedding_ctx_length=False,   # OpenRouter 의 "회사/모델" 이름을 그대로 쓰기 위한 설정
    )


def similarity(vector_a, vector_b):
    """두 벡터가 얼마나 같은 방향을 가리키는지(코사인 유사도) 계산해요. 1 에 가까울수록 뜻이 비슷해요."""
    import numpy as np
    a = np.array(vector_a)
    b = np.array(vector_b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
