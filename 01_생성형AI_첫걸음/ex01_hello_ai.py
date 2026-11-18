# ex01_hello_ai.py : AI 에게 처음으로 말 걸기
from common import get_llm          # 같은 폴더의 common.py 에서 AI 를 만드는 함수를 가져와요

llm = get_llm()                     # AI(LLM) 준비
answer = llm.invoke("안녕? 너는 누구야? 한 문장으로 소개해 줘.")   # 질문 보내기
print(answer.content)               # 답 글자만 보여 주기
