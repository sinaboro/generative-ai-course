# ex05_usage_cost.py : 토큰 사용량과 요금 계산하기
# 요금 = 보낸 토큰(입력) + 받은 토큰(출력). 가격표는 보통 "토큰 100만 개당 몇 달러" 로 적혀 있어요
from llm import client, MODEL

PRICE_IN = 0.15      # 입력 100만 토큰당 $ (openai/gpt-4o-mini 기준, 모델마다 달라요 → openrouter.ai/models)
PRICE_OUT = 0.60     # 출력 100만 토큰당 $

r = client().chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "토큰이 무엇인지 세 문장으로 설명해 줘."}],
    max_tokens=200,
)
u = r.usage
cost = u.prompt_tokens / 1_000_000 * PRICE_IN + u.completion_tokens / 1_000_000 * PRICE_OUT
print("입력 토큰:", u.prompt_tokens, "| 출력 토큰:", u.completion_tokens, "| 합계:", u.total_tokens)
print(f"이번 요청 요금: ${cost:.6f}  (약 {cost * 1400:.3f}원)")
print(f"같은 요청 1,000번: ${cost * 1000:.3f}")
