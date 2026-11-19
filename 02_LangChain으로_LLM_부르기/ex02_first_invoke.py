# ex02_first_invoke.py : ChatOpenAI 를 직접 만들어 AI 부르기 (common.py 가 하는 일)
# 흐름: ① .env 읽기 → ② 모델 · 서버 · 키로 AI 만들기 → ③ invoke 로 질문 → ④ 답과 끝난 이유 보기
import os                                    # 환경 변수를 읽는 도구

from dotenv import find_dotenv, load_dotenv  # .env 파일 읽기
from langchain_openai import ChatOpenAI      # OpenAI 방식 대화 모델을 부르는 LangChain 도구

load_dotenv(find_dotenv())                   # ① .env 파일을 찾아서 읽기

llm = ChatOpenAI(                            # ② AI 만들기
    model=os.getenv("LLM_MODEL"),            # 어떤 모델에게
    base_url=os.getenv("LLM_BASE_URL"),      # 어느 서버를 거쳐 (OpenRouter)
    api_key=os.getenv("LLM_API_KEY"),        # 누구의 키로
)

answer = llm.invoke("LangChain 을 한 문장으로 설명해 줘.")   # ③ 질문 보내기 → 답(AIMessage)
print("답:", answer.content)                                   # ④ 답 글자
print("끝난 이유:", answer.response_metadata["finish_reason"])  # stop = 스스로 끝냄
