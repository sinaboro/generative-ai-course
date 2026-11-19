# ex08_without_langchain.py : 원리 엿보기 — LangChain 없이 openai 라이브러리로 직접 부르면?
# 흐름: ① 클라이언트(서버와 연결하는 도구) 만들기 → ② messages 를 사전 목록으로 보내기
# → ③ 답은 response.choices[0].message.content 처럼 깊이 들어가서 꺼내요 (LangChain 은 .content 하나)
import os                                    # 환경 변수 읽기

from dotenv import find_dotenv, load_dotenv  # .env 읽기
from openai import OpenAI                    # OpenAI 공식 라이브러리

load_dotenv(find_dotenv())                   # .env 파일 읽기

client = OpenAI(base_url=os.getenv("LLM_BASE_URL"), api_key=os.getenv("LLM_API_KEY"))   # ① 연결 도구

response = client.chat.completions.create(   # ② 대화 완성 요청 보내기
    model=os.getenv("LLM_MODEL"),            # 쓸 모델
    messages=[{"role": "user", "content": "LangChain 을 한 문장으로 설명해 줘."}],   # role = 누가 한 말인지
)
print("답:", response.choices[0].message.content)   # ③ 답 후보 목록(choices)의 첫 번째 → 메시지 → 글자
print("토큰:", response.usage.total_tokens)         # 보낸 + 받은 토큰 합계
