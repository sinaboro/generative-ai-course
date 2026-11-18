# ex07_chat_history.py : 대화 기록(history) 목록에 주고받은 말을 모아서 함께 보내기
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from common import get_llm

llm = get_llm(temperature=0)
history = [SystemMessage("너는 친절한 친구야. 두 문장 이내로 답해.")]   # 대화 기록 목록

my_messages = [                               # 내가 차례로 할 말 (input() 대신 미리 적어 둠)
    "내 이름은 민수야. 나는 고양이를 키워.",
    "고양이 이름은 나비야. 좋은 장난감 하나만 추천해 줘.",
    "내 이름이 뭐고, 우리 고양이 이름은 뭐라고 했지?",
]

for my_text in my_messages:
    history.append(HumanMessage(my_text))     # ① 내 말을 기록에 더하고
    answer = llm.invoke(history)              # ② 기록 전체를 보내요
    history.append(AIMessage(answer.content)) # ③ AI 의 답도 기록에 더해요
    print("나:", my_text)
    print("AI:", answer.content)

print("기록에 쌓인 메시지 수:", len(history))
