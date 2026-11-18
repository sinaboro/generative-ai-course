# ex03_messages.py : 메시지 세 종류 — System(규칙) · Human(사람) · AI(AI 의 답)
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from common import get_llm

llm = get_llm(temperature=0)

# 대화 기록을 목록에 차례로 담아요
history = [
    SystemMessage("너는 짧게 답하는 여행 도우미야. 두 문장 이내로 답해."),
    HumanMessage("부산에서 꼭 가 볼 곳 하나만 추천해 줘."),
]
answer1 = llm.invoke(history)
print("1번째 답:", answer1.content)

history.append(AIMessage(answer1.content))                  # AI 의 답도 기록에 붙여요
history.append(HumanMessage("거기까지 부산역에서 어떻게 가?"))  # 다음 질문
answer2 = llm.invoke(history)                                # 기록 전체를 다시 보내요
print("2번째 답:", answer2.content)

alone = llm.invoke("거기까지 부산역에서 어떻게 가?")         # 기록 없이 질문만 보내면?
print("기록 없이:", alone.content)
