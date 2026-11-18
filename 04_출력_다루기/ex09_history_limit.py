# ex09_history_limit.py : 기록이 길어지면 토큰(요금)도 늘어나요 → 최근 대화만 보내기
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from common import get_llm

llm = get_llm(temperature=0, max_tokens=60)
system = SystemMessage("너는 친절한 친구야. 한 문장으로 답해.")
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
        history.append(HumanMessage(my_text))
        if limit_on:
            send = [system] + history[-KEEP:]   # 맨 뒤에서 KEEP 개만 잘라서
        else:
            send = [system] + history           # 기록 전부
        answer = llm.invoke(send)
        history.append(AIMessage(answer.content))
        print(turn, "번째 질문 → 보낸 토큰:", answer.usage_metadata["input_tokens"])
