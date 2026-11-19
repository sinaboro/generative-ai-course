# ex01_json_problem.py : "JSON 으로만 답해" 라고 해도 프로그램이 읽지 못할 때가 있어요
# 흐름: ① JSON 으로 답하라고 부탁 → ② 답 글자를 json.loads 로 사전으로 바꿔 보기
#       → ③ AI 가 ```json 표시나 설명을 붙이면 실패! (그래서 ex02 의 구조화 출력이 필요해요)
import json                                   # JSON 글자를 Python 사전으로 바꾸는 도구

from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0)
question = "영화 '기생충' 의 정보를 JSON 으로 알려 줘. 키는 title, year, director."
text = llm.invoke(question).content           # ① AI 의 답 (그냥 글자예요)
print("AI 의 답 ↓")
print(text)

try:                                          # ② 실패할 수 있으니 try 안에서
    movie = json.loads(text)                  # 글자 → 사전으로 바꾸기 시도
    print("성공! 감독:", movie["director"])    # 사전이 되면 키로 값을 꺼낼 수 있어요
except json.JSONDecodeError:                  # ③ JSON 모양이 아니면 이 오류가 나요
    print("실패! 답이 순수한 JSON 이 아니라서 읽을 수 없어요.")
