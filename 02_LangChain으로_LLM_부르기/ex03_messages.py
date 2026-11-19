# ex03_messages.py : 메시지 세 종류 — System(규칙) · Human(사람) · AI(AI 의 답)
# ── 전체 흐름 ──────────────────────────────────────────────
# ① 규칙 + 첫 질문을 목록(history)에 담아 보내기
# ② AI 의 답과 다음 질문을 목록에 덧붙여 "목록 전체" 를 다시 보내기 → 앞 대화를 이어서 답해요
# ③ 비교: 목록 없이 질문만 보내면 "거기" 가 어디인지 몰라요 → AI 는 스스로 기억하지 못해요
# ────────────────────────────────────────────────────────
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage   # 메시지 세 종류

from common import get_llm                   # AI 를 만드는 함수

llm = get_llm(temperature=0)                 # 늘 같은 답이 나오게

# ① 대화 기록을 목록에 차례로 담아요
history = [
    SystemMessage("너는 짧게 답하는 여행 도우미야. 두 문장 이내로 답해."),   # 규칙
    HumanMessage("부산에서 꼭 가 볼 곳 하나만 추천해 줘."),                # 첫 질문
]
answer1 = llm.invoke(history)                # 목록을 통째로 보내요
print("1번째 답:", answer1.content)

# ② 답과 다음 질문을 기록에 붙여 다시 보내기
history.append(AIMessage(answer1.content))                  # AI 의 답도 기록에 붙여요
history.append(HumanMessage("거기까지 부산역에서 어떻게 가?"))  # 다음 질문
answer2 = llm.invoke(history)                                # 기록 전체를 다시 보내요
print("2번째 답:", answer2.content)

# ③ 비교: 기록 없이 질문만
alone = llm.invoke("거기까지 부산역에서 어떻게 가?")         # 기록 없이 질문만 보내면?
print("기록 없이:", alone.content)                          # "거기" 가 어디인지 몰라요
