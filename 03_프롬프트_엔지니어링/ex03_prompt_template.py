# ex03_prompt_template.py : 프롬프트 템플릿 — 빈칸 { } 이 있는 질문 틀
from langchain_core.prompts import ChatPromptTemplate

from common import get_llm

llm = get_llm(temperature=0)
template = ChatPromptTemplate.from_template("{topic} 을(를) {who} 도 알 수 있게 한 문장으로 설명해 줘.")

prompt = template.invoke({"topic": "인공지능", "who": "초등학생"})   # 빈칸 채우기
print("완성된 질문:", prompt.to_string())

answer = llm.invoke(prompt)
print("답:", answer.content)
