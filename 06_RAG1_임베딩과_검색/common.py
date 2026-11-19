# common.py : 이 과정의 모든 예제가 함께 쓰는 설정 파일
# .env 파일에서 주소 · 키 · 모델 이름을 읽어서, LangChain 의 LLM 을 만들어 줘요
# (이 파일의 내용은 Part 02 에서 한 줄씩 배워요. 지금은 get_llm() 만 쓸 줄 알면 돼요)
# ── 전체 흐름 ──────────────────────────────────────────────
# ① .env 읽기 → ② 주소 · 키 · 모델 이름 꺼내기 → ③ 키가 없으면 연습 모드
# ④ get_llm(): 대화하는 AI 를 만들어 돌려줘요 (연습 모드면 정해 둔 답만 하는 가짜 AI)
# ⑤ get_embeddings(): 글을 숫자 목록으로 바꾸는 임베딩 모델을 만들어 돌려줘요 (Part 06 부터)
# ⑥ similarity(): 두 숫자 목록이 얼마나 비슷한지 점수로 (이 Part 에서만 써요)
# ────────────────────────────────────────────────────────
import os                           # 환경 변수(설정 값)를 읽는 도구

from dotenv import find_dotenv, load_dotenv   # .env 파일을 찾고 읽는 도구

load_dotenv(find_dotenv())          # ① 위쪽 폴더로 올라가며 .env 파일을 찾아서 읽어요

BASE_URL = os.getenv("LLM_BASE_URL", "https://openrouter.ai/api/v1")   # ② 요청을 보낼 서버 주소
API_KEY = os.getenv("LLM_API_KEY", "")                                  # 내 API 키
MODEL = os.getenv("LLM_MODEL", "openai/gpt-4o-mini")                    # 쓸 모델 이름

# ③ 키가 없거나 예시 글자 그대로면 "연습 모드" 로 돌아가요
PRACTICE_MODE = API_KEY == "" or API_KEY == "여기에_내_키를_붙여_넣기"


def get_llm(temperature=0.7, max_tokens=500, model=None):
    """LLM(대화형 AI 모델)을 만들어서 돌려줘요."""
    if PRACTICE_MODE:
        # 키가 없을 때: 진짜 AI 대신 정해 둔 답을 돌려주는 연습용 모델
        from langchain_core.language_models import FakeListChatModel
        return FakeListChatModel(responses=["[연습 모드] .env 에 API 키를 넣으면 진짜 AI 가 답해요."])

    from langchain_openai import ChatOpenAI   # ④ 진짜 AI 를 부르는 도구 (필요할 때만 가져와요)
    if model is None:                          # 모델 이름을 따로 안 주면
        model = MODEL                          # .env 에 적은 모델을 써요
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

    from langchain_openai import OpenAIEmbeddings   # ⑤ 진짜 임베딩 모델 도구
    return OpenAIEmbeddings(
        model=EMBED_MODEL,                  # 임베딩 모델 이름
        base_url=BASE_URL,                  # 서버 주소
        api_key=API_KEY,                    # 내 키
        check_embedding_ctx_length=False,   # OpenRouter 의 "회사/모델" 이름을 그대로 쓰기 위한 설정
    )


def similarity(vector_a, vector_b):
    """두 벡터가 얼마나 같은 방향을 가리키는지(코사인 유사도) 계산해요. 1 에 가까울수록 뜻이 비슷해요."""
    import numpy as np                  # 숫자 목록 계산 도구
    a = np.array(vector_a)              # 목록 → 넘파이 배열 (계산하기 쉽게)
    b = np.array(vector_b)
    # 두 벡터의 곱의 합(dot) ÷ (각 벡터의 길이 곱) = 방향이 같을수록 1, 반대면 -1
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
