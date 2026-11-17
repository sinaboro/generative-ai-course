# ex02_first_call.py : openai 라이브러리로 LLM 을 직접 부르기 (OpenRouter · OpenAI 똑같은 코드)
import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())

# ① 클라이언트 만들기: 어느 서버(base_url)에 어떤 키로 요청할지
client = OpenAI(base_url=os.getenv("LLM_BASE_URL"), api_key=os.getenv("LLM_API_KEY"))

# ② 요청 보내기: 모델 이름 + 대화 목록(messages)
response = client.chat.completions.create(
    model=os.getenv("LLM_MODEL"),
    messages=[{"role": "user", "content": "LLM API 를 한 문장으로 설명해 줘."}],
)

# ③ 응답에서 답 꺼내기
print("답:", response.choices[0].message.content)
print("모델:", response.model)
print("끝난 이유:", response.choices[0].finish_reason)   # stop = 스스로 끝냄, length = 길이 제한
