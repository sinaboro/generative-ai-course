# 정답_문제1.py : 질문 목록을 만들어 AI 에게 차례로 물어보기
from common import get_llm

llm = get_llm(temperature=0)

questions = [
    "인공지능을 한 문장으로 설명해 줘.",
    "토큰이 뭐야? 한 문장으로.",
    "환각을 줄이는 방법 하나만 알려 줘.",
]
for question in questions:
    answer = llm.invoke(question)
    print("Q:", question)
    print("A:", answer.content)
