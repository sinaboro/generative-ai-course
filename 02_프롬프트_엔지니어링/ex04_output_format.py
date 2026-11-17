# ex04_output_format.py : 출력 형식 정하기 — 표 · 목록 · JSON
# 프로그램이 답을 이어서 쓰려면 "모양" 이 늘 같아야 해요 (Part 04 에서 더 자세히)
from llm import ask

topic = "초보자를 위한 파이썬 공부 순서"
formats = {
    "번호 목록": "번호 목록 5줄로만 답해. 다른 말은 쓰지 마.",
    "표": "| 단계 | 배울 것 | 기간 | 열을 가진 마크다운 표로만 답해. 4줄.",
    "JSON": '다음 모양의 JSON 으로만 답해. 설명 · 코드 블록 표시(```)는 쓰지 마: {"steps": [{"step": 1, "topic": "..."}]} (3단계)',
}
for name, rule in formats.items():
    print(f"=== {name} ===")
    print(ask(f"{topic}. {rule}", temperature=0))
    print()
