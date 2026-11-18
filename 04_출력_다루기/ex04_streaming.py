# ex04_streaming.py : 스트리밍 — 답을 다 기다리지 않고 만들어지는 대로 조금씩 보여 주기
from common import get_llm

llm = get_llm()
for chunk in llm.stream("봄 소풍에 대한 짧은 시를 4줄로 써 줘."):   # 조각(chunk)이 올 때마다
    print(chunk.content, end="", flush=True)  # 줄을 바꾸지 않고 바로바로 이어서 출력
print()                                       # 마지막에 줄바꿈 한 번
