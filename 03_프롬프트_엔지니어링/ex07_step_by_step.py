# ex07_step_by_step.py : 단계별로 생각하게 하면 계산 실수가 줄어요
from common import get_llm

llm = get_llm(temperature=0)
problem = ("카페에서 아메리카노는 4,500원, 케이크는 6,000원이에요. 4명이 아메리카노를 하나씩 시키고 "
           "케이크 2개를 나눠 먹었어요. 10% 할인 쿠폰을 쓰면 한 사람당 얼마씩 내면 될까요?")

print("[답만 바로]")
print(llm.invoke(problem + " 숫자 하나로만 답해.").content)
print()
print("[단계별로]")
print(llm.invoke(problem + " 계산 과정을 단계별로 짧게 쓰고, 마지막 줄에 '정답: ○○원' 으로 써 줘.").content)
