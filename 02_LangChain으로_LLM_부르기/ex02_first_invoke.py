# ex02_first_invoke.py : ChatOpenAI 를 직접 만들어 AI 부르기 (common.py 가 하는 일)
import os

from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv())

llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL"),            # 어떤 모델에게
    base_url=os.getenv("LLM_BASE_URL"),      # 어느 서버를 거쳐 (OpenRouter)
    api_key=os.getenv("LLM_API_KEY"),        # 누구의 키로
)

answer = llm.invoke("LangChain 을 한 문장으로 설명해 줘.")
print("답:", answer.content)                                   # 답 글자
print("끝난 이유:", answer.response_metadata["finish_reason"])  # stop = 스스로 끝냄
