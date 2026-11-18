# ex02_system_prompt.py : System 메시지로 AI 의 역할 정하기
from langchain_core.messages import HumanMessage, SystemMessage

from common import get_llm

llm = get_llm(temperature=0.3)
question = HumanMessage("파이썬에서 리스트가 뭐야?")

teacher = SystemMessage("너는 초등학생을 가르치는 친절한 선생님이야. 쉬운 비유를 하나 들고, 3문장 이내로 답해.")
interviewer = SystemMessage("너는 개발자 면접관이야. 답 대신 지원자의 이해도를 확인하는 질문 2개만 해.")

print("[선생님]")
print(llm.invoke([teacher, question]).content)
print()
print("[면접관]")
print(llm.invoke([interviewer, question]).content)
