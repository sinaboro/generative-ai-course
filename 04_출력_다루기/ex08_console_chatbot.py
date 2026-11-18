# ex08_console_chatbot.py : 기억하는 챗봇 — 대화 기록 + 스트리밍 + input()
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from common import get_llm

llm = get_llm()
history = [SystemMessage("너는 여행 계획을 도와주는 친절한 도우미야. 세 문장 이내로 답해.")]
print("여행 도우미 챗봇이에요. 끝내려면 '끝' 을 입력하세요.")

while True:                                   # '끝' 을 입력할 때까지 계속 반복
    my_text = input("나: ")                   # 키보드로 내 말 입력받기
    if my_text == "끝":
        print("챗봇을 끝낼게요. 즐거운 여행 되세요!")
        break                                 # 반복을 멈춰요
    history.append(HumanMessage(my_text))

    print("AI: ", end="")
    full_answer = ""                          # 조각들을 이어 붙여 답 전체를 모을 곳
    for chunk in llm.stream(history):         # 스트리밍으로 조금씩 출력
        print(chunk.content, end="", flush=True)
        full_answer = full_answer + chunk.content
    print()
    history.append(AIMessage(full_answer))    # 모은 답 전체를 기록에 더해요
