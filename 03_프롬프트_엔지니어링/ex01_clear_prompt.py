# ex01_clear_prompt.py : 막연한 질문 vs 구체적인 질문
# 흐름: 같은 주제를 ① 막연하게 ② 대상 · 개수 · 모양 · 길이를 정해 구체적으로 물어보고 답을 비교
from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0.3, max_tokens=300)   # 답이 너무 길지 않게 300토큰까지

vague = "운동에 대해 알려 줘."                  # ① 누구에게 · 무엇을 · 어떤 모양으로? 정보가 없어요
clear = "운동을 처음 하는 20대 직장인에게, 집에서 할 운동 3가지를 '이름 - 방법 - 시간' 목록으로, 5줄 이내로 추천해 줘."
#        ② 대상(20대 직장인) · 조건(집) · 개수(3가지) · 모양(목록) · 길이(5줄) 를 모두 적었어요

print("[막연한 질문]")
print(llm.invoke(vague).content)              # 일반적이고 긴 설명이 나와요
print()                                       # 빈 줄
print("[구체적인 질문]")
print(llm.invoke(clear).content)              # 바로 쓸 수 있는 답이 나와요
