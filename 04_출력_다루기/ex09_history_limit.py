# ex09_history_limit.py : 기록이 길어지면 토큰(요금)도 늘어나요 → 최근 대화만 보내기
# ── 전체 흐름 ──────────────────────────────────────────────
# 같은 6개의 말을 두 번 보내 봐요.
#   한 번째: 기록 전부를 보냄 → 질문할수록 보낸 토큰이 계속 늘어나요
#   두 번째: 규칙 + 맨 뒤 KEEP(4)개만 보냄 → 보낸 토큰이 어느 정도에서 멈춰요
# ────────────────────────────────────────────────────────
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage   # 메시지 세 종류

from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0, max_tokens=60)   # 답은 짧게
system = SystemMessage("너는 친절한 친구야. 한 문장으로 답해.")   # 규칙은 따로 보관 (늘 맨 앞에 붙여요)
my_messages = ["안녕!", "나는 축구를 좋아해.", "어제 경기 봤어?", "요즘 날씨 어때?", "점심 메뉴 추천해 줘.", "고마워!"]
KEEP = 4                                      # 최근 메시지 4개(2번 주고받기)만 보낼 거예요

for limit_on in [False, True]:                # 한 번은 그냥, 한 번은 제한해서
    if limit_on:
        print("=== 최근", KEEP, "개만 보내기 ===")
    else:
        print("=== 전부 보내기 ===")
    history = []                              # 주고받은 말 (system 은 따로 둬요)
    turn = 0                                  # 몇 번째 질문인지 세는 변수
    for my_text in my_messages:
        turn = turn + 1
        history.append(HumanMessage(my_text)) # 내 말을 기록에
        if limit_on:
            send = [system] + history[-KEEP:]   # 맨 뒤에서 KEEP 개만 잘라서 (음수 번호 = 뒤에서부터)
        else:
            send = [system] + history           # 기록 전부
        answer = llm.invoke(send)
        history.append(AIMessage(answer.content))   # 기록에는 늘 전부 저장해요
        print(turn, "번째 질문 → 보낸 토큰:", answer.usage_metadata["input_tokens"])
