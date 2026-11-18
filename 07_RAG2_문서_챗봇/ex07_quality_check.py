# ex07_quality_check.py : 품질 점검 — 정답을 아는 질문으로 챗봇을 시험하기
from doc_tools import ask, load_store

store = load_store()
tests = [                                     # [질문, 답에 꼭 들어 있어야 할 말]
    ["연차는 1년에 며칠 받아?", "15"],
    ["출장 가서 밥값은 하루에 얼마까지 돼?", "3만"],
    ["재택근무는 일주일에 몇 번 할 수 있어?", "2"],
    ["월요일에 재택근무해도 돼?", "없"],
    ["컴퓨터 비밀번호는 얼마마다 바꿔야 해?", "90"],
    ["8시 30분에 출근하면 몇 시에 퇴근해?", "5시 30분"],
    ["출장비 정산을 7일 넘겨서 내면 어떻게 돼?", "받을 수 없"],
    ["회사 주차장은 몇 층에 있어?", "안내서에 없는"],   # 안내서에 없는 질문 → 모른다고 해야 정답
]

passed = 0
for question, must_have in tests:
    answer, pages = ask(store, question)
    if must_have in answer:
        result = "O"
        passed = passed + 1
    else:
        result = "X"
    print(result, question, "→", answer.replace("\n", " "))

print("점수:", passed, "/", len(tests))
