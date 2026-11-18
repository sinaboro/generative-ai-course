# 정답_문제2.py : 새 MCP 서버(글자 수 · 낱말 수)를 클라이언트와 에이전트로 써 보기
from langchain.agents import create_agent

from common import get_llm
from mcp_helper import call_mcp_tool, list_mcp_tools, make_langchain_tools
from my_tools import show_steps

SERVER = "정답_server.py"
for tool in list_mcp_tools(SERVER):
    print("도구:", tool.name, "-", tool.description)
print("count_chars →", call_mcp_tool(SERVER, "count_chars", {"text": "안녕하세요 반가워요"}))

agent = create_agent(get_llm(temperature=0), tools=make_langchain_tools(SERVER),
                     system_prompt="글자 수 · 낱말 수는 반드시 도구로 세. 짧게 답해.")
question = "'나는 오늘 생성형 AI 과정을 끝까지 공부했다' 는 몇 글자이고 낱말은 몇 개야?"
result = agent.invoke({"messages": [{"role": "user", "content": question}]})
show_steps(result["messages"])
