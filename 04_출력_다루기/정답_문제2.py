# 정답_문제2.py : 영어 회화 선생님 챗봇 — 최근 메시지 4개만 기억하기
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from common import get_llm

llm = get_llm(temperature=0.3)
system = SystemMessage("너는 영어 회화 선생님이야. 학생의 영어 문장에 틀린 곳이 있으면 고쳐 주고, "
                       "짧은 영어 질문 하나로 대화를 이어 가. 전체 세 문장 이내.")
history = []
my_messages = ["Hello! I am go to school yesterday.", "I like play soccer with my friend.", "What is your favorite sport?"]

for my_text in my_messages:
    history.append(HumanMessage(my_text))
    answer = llm.invoke([system] + history[-4:])   # system + 최근 4개만
    history.append(AIMessage(answer.content))
    print("나:", my_text)
    print("선생님:", answer.content)
