# ex06_mcp_agent.py : AI 에이전트가 MCP 서버의 도구를 골라 쓰게 하기
# ── 전체 흐름 ──────────────────────────────────────────────
# ① MCP 서버의 도구들을 LangChain 도구로 바꾸기 (make_langchain_tools)
# ② Part 08 과 똑같이 create_agent 로 에이전트 만들기 (+ 같은 대화방 기억)
# ③ 질문마다 실행 → 결과에는 앞 대화까지 다 들어 있어서, 이번 질문부터의 메시지만 골라 보여 주기
# ────────────────────────────────────────────────────────
from langchain.agents import create_agent     # 에이전트 만들기
from langgraph.checkpoint.memory import InMemorySaver   # 대화 기록 보관함

from common import get_llm                    # AI 를 만드는 함수
from mcp_helper import make_langchain_tools   # MCP 도구 → LangChain 도구
from my_tools import show_steps               # 과정 보여 주기

tools = make_langchain_tools("mcp_server.py")   # ⭐ ① MCP 도구 → LangChain 도구 (이것만 다르고 나머지는 Part 08 과 같아요)
agent = create_agent(                         # ②
    get_llm(temperature=0),
    tools=tools,
    system_prompt="너는 메모 비서야. 메모 · 날짜는 도구로 확인하고 짧게 답해.",
    checkpointer=InMemorySaver(),
)
config = {"configurable": {"thread_id": "me"}}   # 늘 같은 대화방

for text in ["오늘 날짜가 며칠이야?", "'금요일 3시 팀 회의' 를 메모해 줘.", "지금까지 메모를 모두 보여 줘."]:
    result = agent.invoke({"messages": [{"role": "user", "content": text}]}, config)
    new_messages = []                         # ③ 이번 질문부터 생긴 메시지만 모아요
    for message in result["messages"]:        # 앞 대화까지 모두 들어 있어서
        if message.type == "human":           # 사람 질문이 나올 때마다 처음부터 다시 모으면
            new_messages = []                 # 마지막에는 이번 질문 뒤의 메시지만 남아요
        new_messages.append(message)
    show_steps(new_messages)
    print("-" * 40)                           # 구분선
