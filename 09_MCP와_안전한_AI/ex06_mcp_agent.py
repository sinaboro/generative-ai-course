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
    show_steps(result["messages"][-4:])        # 이번 질문에서 새로 생긴 메시지 위주로 보여 줘요
    print("-" * 40)
