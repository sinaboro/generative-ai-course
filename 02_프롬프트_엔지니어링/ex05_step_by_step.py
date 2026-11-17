# ex05_step_by_step.py : 단계적으로 생각하게 하기 — 계산 · 추론 문제의 정확도 높이기
from llm import ask

problem = ("카페에서 아메리카노는 4,500원, 케이크는 6,000원이에요. "
           "친구 3명과 나(모두 4명)가 아메리카노를 하나씩 시키고 케이크 2개를 나눠 먹었어요. "
           "10% 할인 쿠폰을 쓰면 한 사람당 얼마씩 내면 될까요?")

print("=== 답만 바로 ===")
print(ask(problem + " 숫자 하나로만 답해.", temperature=0))
print()
print("=== 단계별로 ===")
print(ask(problem + " 계산 과정을 단계별로 짧게 쓰고, 마지막 줄에 '정답: ○○원' 으로 써 줘.", temperature=0))
