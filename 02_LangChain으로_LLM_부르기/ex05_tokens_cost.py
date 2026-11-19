# ex05_tokens_cost.py : 토큰 사용량과 요금 계산하기
# 흐름: ① 가격 정하기 → ② 질문 보내기 → ③ 답에 붙어 온 사용량(보낸 · 받은 토큰) 꺼내기 → ④ 요금 계산
from common import get_llm                    # AI 를 만드는 함수

PRICE_IN = 0.15     # ① 보낸 토큰 100만 개당 가격 ($, openai/gpt-4o-mini 기준)
PRICE_OUT = 0.60    #    받은 토큰 100만 개당 가격 ($)

llm = get_llm()
answer = llm.invoke("토큰이 무엇인지 세 문장으로 설명해 줘.")   # ② 질문 보내기

usage = answer.usage_metadata                 # ③ 이번에 쓴 토큰 수가 들어 있어요
sent = usage["input_tokens"]                  # 보낸 토큰
received = usage["output_tokens"]             # 받은 토큰
cost = sent / 1000000 * PRICE_IN + received / 1000000 * PRICE_OUT   # ④ (토큰 ÷ 100만) × 가격

print("보낸 토큰:", sent, "/ 받은 토큰:", received)
print(f"요금: ${cost:.6f} (약 {cost * 1400:.2f}원)")   # :.6f = 소수점 6자리까지, 1달러 = 1400원으로
