# 정답_문제2.py : 대화를 기억하는 챗봇 (직접 입력하려면 for 문 대신 input() 을 써요)
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from common import get_llm

llm = get_llm(temperature=0)
history = [SystemMessage("너는 친구 같은 챗봇이야. 한 문장으로 짧게 답해.")]

my_messages = ["내 이름은 민지야.", "나는 고양이를 좋아해.", "내 이름이 뭐였지? 내가 좋아하는 동물은?"]
for text in my_messages:
    history.append(HumanMessage(text))        # 내 말을 기록에 붙이고
    answer = llm.invoke(history)              # 기록 전체를 보내요
    history.append(AIMessage(answer.content)) # AI 답도 기록에 붙여요
    print("나:", text)
    print("봇:", answer.content)
