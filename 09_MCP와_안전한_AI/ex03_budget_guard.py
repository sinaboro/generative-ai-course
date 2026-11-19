# ex03_budget_guard.py : 횟수 · 길이 · 토큰 제한 — 실수나 공격으로 요금 폭탄을 맞지 않게
# ── 전체 흐름 ──────────────────────────────────────────────
# guarded_ask(질문): AI 에게 보내기 "전에" 세 가지 한도를 먼저 확인해요
#   횟수를 다 썼나? → 질문이 너무 긴가? → 토큰을 다 썼나? → 하나라도 걸리면 ⛔ 안내만 하고 끝
#   모두 괜찮으면 AI 에게 보내고, 쓴 횟수 · 토큰을 usage 에 더해요
# ────────────────────────────────────────────────────────
from common import get_llm                    # AI 를 만드는 함수

MAX_CALLS = 3                                 # 하루 질문 횟수 한도
MAX_INPUT = 300                               # 질문 글자 수 한도
MAX_TOKENS = 400                              # 하루 토큰 한도
usage = {"calls": 0, "tokens": 0}             # 지금까지 쓴 양

llm = get_llm(temperature=0, max_tokens=100)  # 답 길이도 제한해요


def guarded_ask(question):
    """한도를 먼저 확인하고, 괜찮을 때만 AI 에게 보내요."""
    if usage["calls"] >= MAX_CALLS:           # 한도 1: 횟수
        return "⛔ 오늘 질문 횟수를 다 썼어요."
    if len(question) > MAX_INPUT:             # 한도 2: 길이 (긴 글 = 많은 토큰 = 많은 요금)
        return "⛔ 질문이 너무 길어요 (" + str(MAX_INPUT) + "자 이내)."
    if usage["tokens"] >= MAX_TOKENS:         # 한도 3: 토큰
        return "⛔ 오늘 쓸 수 있는 토큰을 다 썼어요."
    answer = llm.invoke(question)             # 모두 통과했을 때만 AI 에게
    usage["calls"] = usage["calls"] + 1       # 쓴 양 기록
    usage["tokens"] = usage["tokens"] + answer.usage_metadata["total_tokens"]
    return answer.content


questions = ["1 더하기 1은? 숫자만", "하늘은 왜 파래? 한 문장", "가" * 400, "고양이 울음소리는? 한 낱말", "마지막 질문"]
#                                                          ↑ "가" 를 400번 = 너무 긴 질문
for question in questions:
    print("Q(" + str(len(question)) + "자)", question[:15], "→", guarded_ask(question))   # 앞 15글자만
print("사용:", usage["calls"], "회,", usage["tokens"], "토큰")
