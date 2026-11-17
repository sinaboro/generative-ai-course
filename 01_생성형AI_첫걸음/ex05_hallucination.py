# ex05_hallucination.py : 환각(hallucination) — LLM 이 그럴듯하게 지어내는 답 확인하기
# 세상에 없는 것을 물어보면 모델에 따라 "모른다" 고 하기도, 그럴듯하게 지어내기도 해요
from llm import ask

# 실제로 없는 책 (이 교안을 위해 지어낸 제목이에요)
fake = "소설 『달빛 자판기와 일곱 개의 우산』(2019)의 줄거리를 세 줄로 알려 줘."
print("Q1:", fake)
print("A1:", ask(fake, temperature=0.7))
print()

# 같은 질문에 "모르면 모른다고 말해" 라는 규칙을 더하면?
rule = "확실히 아는 사실만 답해. 모르거나 확인할 수 없으면 '모르겠어요' 라고 말해."
print("Q2: (같은 질문 + 규칙)", rule)
print("A2:", ask(fake, system=rule, temperature=0.7))
print()

# 아주 작은 모델에게 같은 질문을 하면? (작은 모델일수록 지어낼 때가 많아요)
small = "google/gemma-3-4b-it"
print("Q3: (작은 모델", small + ")")
print("A3:", ask(fake, model=small, temperature=0.7))
