# ex01_json_problem.py : "JSON 으로만 답해" 라고 해도 프로그램이 읽지 못할 때가 있어요
import json                                   # JSON 글자를 Python 사전으로 바꾸는 도구

from common import get_llm

llm = get_llm(temperature=0)
question = "영화 '기생충' 의 정보를 JSON 으로 알려 줘. 키는 title, year, director."
text = llm.invoke(question).content           # AI 의 답 (글자)
print("AI 의 답 ↓")
print(text)

try:
    movie = json.loads(text)                  # 글자 → 사전으로 바꾸기 시도
    print("성공! 감독:", movie["director"])
except json.JSONDecodeError:
    print("실패! 답이 순수한 JSON 이 아니라서 읽을 수 없어요.")
