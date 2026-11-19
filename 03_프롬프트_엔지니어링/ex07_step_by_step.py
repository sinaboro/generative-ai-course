# ex07_step_by_step.py : 단계별로 생각하게 하면 계산 실수가 줄어요
# 흐름: 같은 문제를 ① 숫자만 바로 답하게 ② 계산 과정을 단계별로 쓰게 해서 → 정답률 비교
from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0)
problem = ("카페에서 아메리카노는 4,500원, 케이크는 6,000원이에요. 4명이 아메리카노를 하나씩 시키고 "
           "케이크 2개를 나눠 먹었어요. 10% 할인 쿠폰을 쓰면 한 사람당 얼마씩 내면 될까요?")
# ↑ 괄호 ( ) 로 감싸면 긴 글자를 두 줄로 나눠 쓸 수 있어요 (정답: 30000 × 0.9 ÷ 4 = 6,750원)

print("[답만 바로]")
print(llm.invoke(problem + " 숫자 하나로만 답해.").content)         # ① 틀리기 쉬워요
print()
print("[단계별로]")
print(llm.invoke(problem + " 계산 과정을 단계별로 짧게 쓰고, 마지막 줄에 '정답: ○○원' 으로 써 줘.").content)   # ②
