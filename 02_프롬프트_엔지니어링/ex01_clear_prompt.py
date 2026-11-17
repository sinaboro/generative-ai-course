# ex01_clear_prompt.py : 막연한 프롬프트 vs 구체적인 프롬프트
# 좋은 프롬프트 = 누구에게(대상) · 무엇을(작업) · 어떤 모양으로(형식) · 얼마나(길이) 를 분명하게
from llm import ask

vague = "운동에 대해 알려 줘."
clear = (
    "운동을 처음 시작하는 20대 직장인에게, "
    "퇴근 후 집에서 할 수 있는 운동 3가지를 추천해 줘. "
    "각 운동은 '이름 - 하는 방법 한 줄 - 시간' 형식의 목록으로, 전체 5줄 이내로 써 줘."
)
for name, p in [("막연한 프롬프트", vague), ("구체적인 프롬프트", clear)]:
    print(f"=== {name} ===")
    print(ask(p, temperature=0.3, max_tokens=400))
    print()
