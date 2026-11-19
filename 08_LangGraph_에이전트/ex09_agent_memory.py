# ex09_agent_memory.py : 대화를 기억하는 에이전트 — checkpointer 와 thread_id
# ── 전체 흐름 ──────────────────────────────────────────────
# ① checkpointer(기록 보관함)를 붙여 에이전트 만들기
# ② chat(대화방 이름, 말): 대화방 이름(thread_id)을 config 에 담아 보내면
#    → 보관함이 그 방의 지난 대화를 꺼내 붙이고, 이번 대화도 저장해요
# ③ 같은 방("민수")은 앞의 말을 기억하고, 다른 방("지영")은 처음부터 시작해요
# ────────────────────────────────────────────────────────
from langchain.agents import create_agent     # 에이전트 만들기
from langgraph.checkpoint.memory import InMemorySaver   # 대화 기록을 메모리에 저장하는 도구

from common import get_llm                    # AI 를 만드는 함수
from my_tools import calculator               # 계산기 도구

agent = create_agent(                         # ①
    get_llm(temperature=0),
    tools=[calculator],
    system_prompt="너는 친절한 가계부 도우미야. 계산은 calculator 로 해. 두 문장 이내로 답해.",
    checkpointer=InMemorySaver(),             # ⭐ 대화방마다 기록을 저장해요
)


def chat(thread_id, text):
    """대화방(thread_id)을 정해서 말을 보내고, AI 의 마지막 답을 보여 줘요."""
    config = {"configurable": {"thread_id": thread_id}}   # ② "이 대화방에서" 라는 설정
    result = agent.invoke({"messages": [{"role": "user", "content": text}]}, config)
    print("[" + thread_id + "] 나:", text)
    print("[" + thread_id + "] AI:", result["messages"][-1].content)   # [-1] = 마지막 메시지 = 최종 답


chat("민수", "오늘 점심에 9,000원, 커피에 4,500원 썼어.")
chat("민수", "저녁에 12,000원 더 썼어. 오늘 모두 얼마 썼지?")   # ③ 같은 방 → 앞의 말을 기억
chat("지영", "오늘 모두 얼마 썼지?")                          #    다른 방 → 처음 만난 사이
