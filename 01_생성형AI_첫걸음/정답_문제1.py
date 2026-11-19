# 정답_문제1.py : 질문 목록을 만들어 AI 에게 차례로 물어보기
# 흐름: ① AI 준비 → ② 질문을 리스트에 모으기 → ③ for 문으로 하나씩 묻고 Q/A 출력
from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0)                  # ① 늘 같은 답이 나오게 온도 0

questions = [                                 # ② 물어볼 질문 목록
    "인공지능을 한 문장으로 설명해 줘.",
    "토큰이 뭐야? 한 문장으로.",
    "환각을 줄이는 방법 하나만 알려 줘.",
]
for question in questions:                    # ③ 질문을 하나씩 꺼내서
    answer = llm.invoke(question)             # AI 에게 묻고
    print("Q:", question)                     # 질문과
    print("A:", answer.content)               # 답을 차례로 보여 주기
