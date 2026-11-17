# ex03_budget_guard.py : 비용 · 횟수 제한 — 실수나 공격으로 요금이 폭탄이 되지 않게
from llm import client, MODEL


class BudgetGuard:
    """하루 요청 횟수와 토큰 합계에 한도를 두는 작은 문지기"""

    def __init__(self, max_calls=3, max_tokens=500):
        self.max_calls, self.max_tokens = max_calls, max_tokens
        self.calls = self.tokens = 0

    def ask(self, question, max_answer=100):
        if self.calls >= self.max_calls:
            return "⛔ 오늘 요청 횟수를 다 썼어요."
        if len(question) > 300:                 # 너무 긴 입력은 보내기 전에 거절
            return "⛔ 질문이 너무 길어요 (300자 이내)."
        r = client().chat.completions.create(model=MODEL, max_tokens=max_answer,
                                             messages=[{"role": "user", "content": question}])
        self.calls += 1
        self.tokens += r.usage.total_tokens
        if self.tokens > self.max_tokens:
            return "⛔ 토큰 한도를 넘었어요. 관리자에게 알려요."
        return r.choices[0].message.content


guard = BudgetGuard(max_calls=3)
for q in ["1 더하기 1은? 숫자만", "하늘은 왜 파래? 한 문장", "가" * 400, "고양이 울음소리는? 한 낱말", "마지막 질문"]:
    print(f"Q({len(q)}자): {q[:20]} → {guard.ask(q)}")
print(f"사용: {guard.calls}회, {guard.tokens}토큰")
