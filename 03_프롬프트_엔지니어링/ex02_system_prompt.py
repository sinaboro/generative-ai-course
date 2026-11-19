# ex02_system_prompt.py : System 메시지로 AI 의 역할 정하기
# 흐름: 같은 질문에 ① 선생님 역할 ② 면접관 역할 규칙을 각각 붙여 보내고 → 답이 어떻게 달라지는지 비교
from langchain_core.messages import HumanMessage, SystemMessage   # 사람 · 규칙 메시지

from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0.3)
question = HumanMessage("파이썬에서 리스트가 뭐야?")              # 두 번 다 같은 질문

teacher = SystemMessage("너는 초등학생을 가르치는 친절한 선생님이야. 쉬운 비유를 하나 들고, 3문장 이내로 답해.")
interviewer = SystemMessage("너는 개발자 면접관이야. 답 대신 지원자의 이해도를 확인하는 질문 2개만 해.")

print("[선생님]")
print(llm.invoke([teacher, question]).content)       # ① [규칙, 질문] 순서로 보내요
print()
print("[면접관]")
print(llm.invoke([interviewer, question]).content)   # ② 규칙만 바꿔서 같은 질문
