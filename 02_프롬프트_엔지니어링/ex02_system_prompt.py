# ex02_system_prompt.py : System Prompt — AI 에게 역할과 규칙을 정해 주기
# 같은 질문이라도 system 에 적은 역할에 따라 말투 · 내용이 달라져요
from llm import ask

question = "파이썬에서 리스트가 뭐야?"
roles = {
    "초등학생 선생님": "너는 초등학생을 가르치는 친절한 선생님이야. 쉬운 비유를 하나 들고, 3문장 이내로 답해.",
    "엄격한 면접관": "너는 개발자 면접관이야. 답 대신 지원자의 이해도를 확인하는 질문 2개만 던져.",
}
for name, system in roles.items():
    print(f"=== 역할: {name} ===")
    print(ask(question, system=system, temperature=0.3))
    print()
