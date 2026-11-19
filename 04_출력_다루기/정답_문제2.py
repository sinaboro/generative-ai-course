# 정답_문제2.py : 영어 회화 선생님 챗봇 — 최근 메시지 4개만 기억하기
# 흐름: 말마다 ① 기록에 더하기 → ② 규칙 + 최근 4개만 보내기 → ③ 답을 기록에 더하고 출력
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage   # 메시지 세 종류

from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0.3)
system = SystemMessage("너는 영어 회화 선생님이야. 학생의 영어 문장에 틀린 곳이 있으면 고쳐 주고, "
                       "짧은 영어 질문 하나로 대화를 이어 가. 전체 세 문장 이내.")
history = []                                  # 주고받은 말 (규칙은 따로)
my_messages = ["Hello! I am go to school yesterday.", "I like play soccer with my friend.", "What is your favorite sport?"]

for my_text in my_messages:
    history.append(HumanMessage(my_text))     # ① 내 말을 기록에
    answer = llm.invoke([system] + history[-4:])   # ② system + 최근 4개만
    history.append(AIMessage(answer.content)) # ③ 답도 기록에
    print("나:", my_text)
    print("선생님:", answer.content)
