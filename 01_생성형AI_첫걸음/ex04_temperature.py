# ex04_temperature.py : temperature(온도) — 답을 늘 같게? 다양하게?
# 흐름: 온도 0 과 1.2 로 AI 를 각각 만들고 → 같은 질문을 3번씩 물어 답이 얼마나 달라지는지 비교
from common import get_llm                   # AI 를 만드는 함수

question = "새로 연 동네 빵집 이름을 하나만 지어 줘. 이름만 써."

for temp in [0, 1.2]:                        # 온도 0 과 1.2 를 차례로
    llm = get_llm(temperature=temp)          # 그 온도로 AI 만들기
    print("temperature", temp)
    for count in range(3):                   # 같은 질문을 3번씩
        answer = llm.invoke(question)        # 질문 보내기
        print("   ", answer.content)         # 0 이면 거의 같은 답, 1.2 면 매번 다른 답
