# ex01_hello_ai.py : AI 에게 처음으로 말 걸기
# 흐름: ① AI 준비(get_llm) → ② 질문 보내기(invoke) → ③ 답 글자 보여 주기(content)
from common import get_llm          # 같은 폴더의 common.py 에서 AI 를 만드는 함수를 가져와요

llm = get_llm()                     # ① AI(LLM) 준비
answer = llm.invoke("안녕? 너는 누구야? 한 문장으로 소개해 줘.")   # ② 질문 보내기 → 답 묶음이 와요
print(answer.content)               # ③ 답 묶음에서 글자(content)만 꺼내 보여 주기
