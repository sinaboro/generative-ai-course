# ex06_output_format.py : 답의 모양 정하기 — 번호 목록 · 표 · JSON
from common import get_llm

llm = get_llm(temperature=0)
topic = "초보자를 위한 파이썬 공부 순서"

print("[번호 목록]")
print(llm.invoke(topic + ". 번호 목록 4줄로만 답해. 다른 말은 쓰지 마.").content)
print()
print("[표]")
print(llm.invoke(topic + ". '| 단계 | 배울 것 | 기간 |' 열을 가진 마크다운 표로만 답해. 3줄.").content)
print()
print("[JSON]")
print(llm.invoke(topic + '. {"steps": ["...", "..."]} 모양의 JSON 으로만 답해. 3단계. 설명과 ``` 표시는 쓰지 마.').content)
