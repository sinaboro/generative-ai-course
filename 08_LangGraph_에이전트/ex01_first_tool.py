# ex01_first_tool.py : 도구(tool) 만들기 — 평범한 함수에 @tool 만 붙이면 돼요
from langchain_core.tools import tool


@tool
def add(a: int, b: int) -> int:
    """두 수를 더해요."""
    return a + b


print("이름:", add.name)                    # 함수 이름이 도구 이름이 돼요
print("설명:", add.description)             # 큰따옴표 세 개 안의 설명이 도구 설명이 돼요
print("받는 값:", add.args)                  # a, b 와 자료형
print("실행:", add.invoke({"a": 3, "b": 4}))   # 사전으로 값을 넣어 실행
