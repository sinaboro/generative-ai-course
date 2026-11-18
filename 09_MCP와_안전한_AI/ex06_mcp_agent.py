# ex06_mcp_agent.py : AI 에이전트가 MCP 서버의 도구를 골라 쓰게 하기
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

from common import get_llm
from mcp_helper import make_langchain_tools
from my_tools import show_steps

tools = make_langchain_tools("mcp_server.py")   # ⭐ MCP 도구 → LangChain 도구 (이것만 다르고 나머지는 Part 08 과 같아요)
agent = create_agent(
    get_llm(temperature=0),
    tools=tools,
    system_prompt="너는 메모 비서야. 메모 · 날짜는 도구로 확인하고 짧게 답해.",
    checkpointer=InMemorySaver(),
)
config = {"configurable": {"thread_id": "me"}}

for text in ["오늘 날짜가 며칠이야?", "'금요일 3시 팀 회의' 를 메모해 줘.", "지금까지 메모를 모두 보여 줘."]:
    result = agent.invoke({"messages": [{"role": "user", "content": text}]}, config)
    new_messages = []                         # 이번 질문부터 생긴 메시지만 모아요
    for message in result["messages"]:        # 앞 대화까지 모두 들어 있어서
        if message.type == "human":           # 사람 질문이 나올 때마다 처음부터 다시 모으면
            new_messages = []                 # 마지막에는 이번 질문 뒤의 메시지만 남아요
        new_messages.append(message)
    show_steps(new_messages)
    print("-" * 40)
