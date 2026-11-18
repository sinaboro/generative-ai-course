# ex04_temperature.py : temperature(온도) — 답을 늘 같게? 다양하게?
from common import get_llm

question = "새로 연 동네 빵집 이름을 하나만 지어 줘. 이름만 써."

for temp in [0, 1.2]:                        # 온도 0 과 1.2 를 차례로
    llm = get_llm(temperature=temp)
    print("temperature", temp)
    for count in range(3):                   # 같은 질문을 3번씩
        answer = llm.invoke(question)
        print("   ", answer.content)
