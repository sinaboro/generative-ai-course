# ex03_messages.py : 대화 목록(messages) — system · user · assistant 세 가지 역할
# LLM 은 지난 대화를 기억하지 못해요. 그래서 매번 지금까지의 대화를 통째로 보내요
from llm import chat

messages = [
    {"role": "system", "content": "너는 짧게 답하는 여행 도우미야. 두 문장 이내로 답해."},
    {"role": "user", "content": "부산에서 꼭 가 볼 곳 하나만 추천해 줘."},
]
answer1 = chat(messages, temperature=0)
print("1번째 답:", answer1)

# AI 의 답을 assistant 로 대화 목록에 붙이고, 다음 질문을 이어서 보내요
messages.append({"role": "assistant", "content": answer1})
messages.append({"role": "user", "content": "거기까지 부산역에서 어떻게 가?"})
answer2 = chat(messages, temperature=0)
print("2번째 답:", answer2)

# 대화 기록 없이 두 번째 질문만 보내면? "거기" 가 어디인지 몰라요
alone = chat([{"role": "user", "content": "거기까지 부산역에서 어떻게 가?"}], temperature=0)
print("기록 없이:", alone)
print("보낸 메시지 수:", len(messages))
