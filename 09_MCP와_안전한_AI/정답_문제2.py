# 정답_문제2.py : 새 MCP 서버(글자 수 · 낱말 수)를 클라이언트와 에이전트로 써 보기
# 흐름: ① 클라이언트로 도구 목록 보고 직접 하나 실행 (ex05 방식)
#       → ② 같은 서버 도구를 에이전트에게 주고 질문 (ex06 방식)
from langchain.agents import create_agent     # 에이전트 만들기

from common import get_llm                    # AI 를 만드는 함수
from mcp_helper import call_mcp_tool, list_mcp_tools, make_langchain_tools   # MCP 도우미
from my_tools import show_steps               # 과정 보여 주기

SERVER = "정답_server.py"                     # 새로 만든 서버
for tool in list_mcp_tools(SERVER):           # ① 도구 목록
    print("도구:", tool.name, "-", tool.description)
print("count_chars →", call_mcp_tool(SERVER, "count_chars", {"text": "안녕하세요 반가워요"}))

agent = create_agent(get_llm(temperature=0), tools=make_langchain_tools(SERVER),   # ② 에이전트
                     system_prompt="글자 수 · 낱말 수는 반드시 도구로 세. 짧게 답해.")
question = "'나는 오늘 생성형 AI 과정을 끝까지 공부했다' 는 몇 글자이고 낱말은 몇 개야?"
result = agent.invoke({"messages": [{"role": "user", "content": question}]})
show_steps(result["messages"])
