# ex04_first_llm.py : 진짜 LLM 에게 처음으로 물어보기 (자세한 원리는 Part 03)
# 실행 전: 저장소 맨 위의 .env.example 을 복사해 .env 로 만들고 키를 넣어요. 키가 없으면 연습 모드로 돌아가요
from llm import MODEL, MOCK, ask

print("사용하는 모델:", MODEL, "| 연습 모드:", MOCK)

question = "생성형 AI 가 무엇인지 초등학생도 알 수 있게 두 문장으로 설명해 줘."
answer = ask(question)
print("질문:", question)
print("답:", answer)
