# ex01_first_tool.py : 도구(tool) 만들기 — 평범한 함수에 @tool 만 붙이면 돼요
# 흐름: ① 함수 위에 @tool → ② 이름 · 설명 · 받는 값이 자동으로 정리돼요 → ③ invoke(사전)로 실행
from langchain_core.tools import tool         # 함수를 "AI 가 쓸 수 있는 도구" 로 바꾸는 표시


@tool                                         # ① 바로 아래 함수를 도구로
def add(a: int, b: int) -> int:               # a: int → "a 는 정수" (AI 가 보고 값을 넣어요)
    """두 수를 더해요."""                         # AI 는 이 설명을 보고 언제 쓸지 정해요
    return a + b


print("이름:", add.name)                    # ② 함수 이름이 도구 이름이 돼요
print("설명:", add.description)             # 큰따옴표 세 개 안의 설명이 도구 설명이 돼요
print("받는 값:", add.args)                  # a, b 와 자료형
print("실행:", add.invoke({"a": 3, "b": 4}))   # ③ 사전으로 값을 넣어 실행
