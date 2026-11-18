# ex08_without_langchain.py : 원리 엿보기 — LangChain 없이 openai 라이브러리로 직접 부르면?
import os

from dotenv import find_dotenv, load_dotenv
from openai import OpenAI

load_dotenv(find_dotenv())

client = OpenAI(base_url=os.getenv("LLM_BASE_URL"), api_key=os.getenv("LLM_API_KEY"))

response = client.chat.completions.create(
    model=os.getenv("LLM_MODEL"),
    messages=[{"role": "user", "content": "LangChain 을 한 문장으로 설명해 줘."}],
)
print("답:", response.choices[0].message.content)
print("토큰:", response.usage.total_tokens)
