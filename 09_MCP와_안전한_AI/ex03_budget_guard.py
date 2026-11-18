# ex03_budget_guard.py : 횟수 · 길이 · 토큰 제한 — 실수나 공격으로 요금 폭탄을 맞지 않게
from common import get_llm

MAX_CALLS = 3                                 # 하루 질문 횟수 한도
MAX_INPUT = 300                               # 질문 글자 수 한도
MAX_TOKENS = 400                              # 하루 토큰 한도
usage = {"calls": 0, "tokens": 0}             # 지금까지 쓴 양

llm = get_llm(temperature=0, max_tokens=100)  # 답 길이도 제한해요


def guarded_ask(question):
    """한도를 먼저 확인하고, 괜찮을 때만 AI 에게 보내요."""
    if usage["calls"] >= MAX_CALLS:
        return "⛔ 오늘 질문 횟수를 다 썼어요."
    if len(question) > MAX_INPUT:
        return "⛔ 질문이 너무 길어요 (" + str(MAX_INPUT) + "자 이내)."
    if usage["tokens"] >= MAX_TOKENS:
        return "⛔ 오늘 쓸 수 있는 토큰을 다 썼어요."
    answer = llm.invoke(question)
    usage["calls"] = usage["calls"] + 1
    usage["tokens"] = usage["tokens"] + answer.usage_metadata["total_tokens"]
    return answer.content


questions = ["1 더하기 1은? 숫자만", "하늘은 왜 파래? 한 문장", "가" * 400, "고양이 울음소리는? 한 낱말", "마지막 질문"]
for question in questions:
    print("Q(" + str(len(question)) + "자)", question[:15], "→", guarded_ask(question))
print("사용:", usage["calls"], "회,", usage["tokens"], "토큰")
