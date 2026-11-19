# ex04_streaming.py : 스트리밍 — 답을 다 기다리지 않고 만들어지는 대로 조금씩 보여 주기
# 흐름: invoke 대신 stream 을 쓰면 → 답이 조각(chunk)으로 여러 번 와요 → 올 때마다 이어서 출력
from common import get_llm                    # AI 를 만드는 함수

llm = get_llm()
for chunk in llm.stream("봄 소풍에 대한 짧은 시를 4줄로 써 줘."):   # 조각(chunk)이 올 때마다
    print(chunk.content, end="", flush=True)  # end="": 줄 안 바꿈, flush=True: 바로 화면에 내보내기
print()                                       # 마지막에 줄바꿈 한 번
