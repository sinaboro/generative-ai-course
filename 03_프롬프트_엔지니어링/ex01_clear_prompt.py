# ex01_clear_prompt.py : 막연한 질문 vs 구체적인 질문
from common import get_llm

llm = get_llm(temperature=0.3, max_tokens=300)

vague = "운동에 대해 알려 줘."
clear = "운동을 처음 하는 20대 직장인에게, 집에서 할 운동 3가지를 '이름 - 방법 - 시간' 목록으로, 5줄 이내로 추천해 줘."

print("[막연한 질문]")
print(llm.invoke(vague).content)
print()
print("[구체적인 질문]")
print(llm.invoke(clear).content)
