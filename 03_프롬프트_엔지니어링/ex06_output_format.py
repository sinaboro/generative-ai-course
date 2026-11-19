# ex06_output_format.py : 답의 모양 정하기 — 번호 목록 · 표 · JSON
# 흐름: 같은 주제 뒤에 "어떤 모양으로 답해" 만 바꿔 붙여서 세 번 물어보기
from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0)
topic = "초보자를 위한 파이썬 공부 순서"        # 세 번 다 같은 주제

print("[번호 목록]")
print(llm.invoke(topic + ". 번호 목록 4줄로만 답해. 다른 말은 쓰지 마.").content)
print()
print("[표]")                                 # 마크다운 표: | 칸 | 칸 | 모양
print(llm.invoke(topic + ". '| 단계 | 배울 것 | 기간 |' 열을 가진 마크다운 표로만 답해. 3줄.").content)
print()
print("[JSON]")                               # JSON: 프로그램이 읽기 좋은 모양 (Part 04 에서 자세히)
print(llm.invoke(topic + '. {"steps": ["...", "..."]} 모양의 JSON 으로만 답해. 3단계. 설명과 ``` 표시는 쓰지 마.').content)
