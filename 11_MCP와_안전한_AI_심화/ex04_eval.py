# ex04_eval.py : 자동 평가 — 질문 세트로 챗봇 답을 한 번에 점검하기
from llm import ask

SYSTEM = "너는 AI 서비스 개발 과정 안내 챗봇이야. 수업은 9시 30분 시작, 6시 30분 종료, 점심 12시 30분. 모르면 '모르겠어요'."

# (질문, 답에 꼭 있어야 할 낱말 목록)
tests = [
    ("수업은 몇 시에 시작해요?", ["9시 30분"]),
    ("점심시간은 언제예요?", ["12시 30분"]),
    ("수업 끝나는 시간은?", ["6시 30분"]),
    ("강사님 생일이 언제예요?", ["모르겠"]),        # 모르는 것은 모른다고 해야 통과
]
passed = 0
for q, must in tests:
    a = ask(q, system=SYSTEM, temperature=0)
    ok = all(m in a for m in must)
    passed += ok
    print(f"{'✔' if ok else '✘'} {q} → {a}")
print(f"통과율: {passed}/{len(tests)}")
