# mcp_helper.py : MCP 서버를 쉽게 쓰게 해 주는 도우미 함수 모음
# MCP 라이브러리는 async(비동기) 문법을 써요. 어려운 부분은 이 파일에 숨겨 두었으니,
# 예제에서는 list_mcp_tools · call_mcp_tool · make_langchain_tools 세 함수만 쓰면 돼요.
# ── 전체 흐름 (도구 하나를 부를 때) ─────────────────────────────
# ① 서버를 새로 켜요: 우리 서버는 "python 서버파일.py", 노션 같은 외부 서버는 "npx …" (_server)
# ② 켠 서버와 표준 입출력(글자 주고받는 통로)으로 연결해요 (stdio_client → read, write 통로 두 개)
# ③ 그 통로 위에 MCP 대화 세션을 열고 인사해요 (ClientSession → initialize)
# ④ "도구 목록 줘" 또는 "이 도구를 이 값으로 실행해 줘" 를 보내고 결과를 받아요
# ⑤ with 블록이 끝나면 세션 · 통로가 닫히고 서버도 자동으로 꺼져요
# ── async · await 를 아주 짧게 ─────────────────────────────────
# async def : "기다리는 일이 들어 있는 함수" 라는 표시예요 (서버의 답을 기다려야 하니까)
# await     : "이 일이 끝날 때까지 기다렸다가 다음 줄로" 라는 뜻이에요
# async with: 열고(연결) · 다 쓰면 닫는(정리) 일을 기다리면서 해 주는 with 예요
# asyncio.run(...): 보통 함수에서 async 함수를 한 번 실행하고 결과를 받아 오는 출입구예요
# ────────────────────────────────────────────────────────
import asyncio                                # async 함수를 실행하는 도구
import sys                                    # sys.executable = 지금 쓰고 있는 python 프로그램 경로

from langchain_core.tools import StructuredTool        # 함수 + 설명 + 받는 값 모양 → LangChain 도구
from mcp import ClientSession, StdioServerParameters   # MCP 대화 세션 · 서버 켜는 설정
from mcp.client.stdio import stdio_client              # 표준 입출력으로 서버와 연결하는 도구


def _server(server_file):
    """서버를 켜는 설정을 만들어요 (이름 앞 _ 는 "이 파일 안에서만 쓰는 함수" 라는 뜻)
    server_file 이 "mcp_server.py" 같은 글자면 → python 으로 그 파일을 켜요 (우리가 만든 서버)
    server_file 이 {"command": …, "args": …, "env": …} 사전이면 → 그 명령으로 켜요 (노션 같은 외부 서버)"""
    if isinstance(server_file, dict):         # 외부 MCP 서버 (ex08 의 노션)
        return StdioServerParameters(command=server_file["command"], args=server_file["args"],
                                     env=server_file.get("env"))   # env: 서버에게 넘겨줄 환경 변수 (토큰 등)
    return StdioServerParameters(command=sys.executable, args=[server_file])   # ① 명령어 + 파일 이름


async def _list(server_file):
    """서버에 도구 목록을 물어봐요 (async 버전)."""
    async with stdio_client(_server(server_file)) as (read, write):   # ② 서버를 켜고 읽기 · 쓰기 통로 받기
        async with ClientSession(read, write) as session:              # ③ 통로 위에 MCP 세션 열기
            await session.initialize()                    # 서버와 인사 (서로 버전 확인)
            result = await session.list_tools()           # ④ 도구 목록 받기
            return result.tools                           # ⑤ return 하면서 with 가 끝나 연결이 닫혀요


async def _call(server_file, name, args):
    """서버의 도구 하나를 실행해요 (async 버전)."""
    async with stdio_client(_server(server_file)) as (read, write):   # ② 연결
        async with ClientSession(read, write) as session:              # ③ 세션
            await session.initialize()
            result = await session.call_tool(name, args)  # ④ 도구 실행 (이름, 넣을 값 사전)
            texts = []
            for part in result.content:                   # 결과가 여러 조각이면 이어 붙여요
                texts.append(part.text)
            return ", ".join(texts)                       # ["a", "b"] → "a, b"


def list_mcp_tools(server_file):
    """MCP 서버를 켜서 도구 목록을 받아 와요."""
    return asyncio.run(_list(server_file))    # async 함수를 실행하고 결과를 받아 오는 출입구


def call_mcp_tool(server_file, name, args):
    """MCP 서버를 켜서 도구 하나를 실행하고 결과 글자를 돌려줘요."""
    return asyncio.run(_call(server_file, name, args))


def _to_langchain(server_file, mcp_tool):
    """MCP 도구 하나를 LangChain 도구로 바꿔요 (Part 08 의 에이전트가 쓸 수 있게)."""
    def run(**kwargs):                        # **kwargs: 이름=값 으로 받은 것을 모두 사전 하나로 모아요
        return call_mcp_tool(server_file, mcp_tool.name, kwargs)   # 에이전트가 부르면 → MCP 서버 도구 실행
    return StructuredTool.from_function(func=run, name=mcp_tool.name,          # 실행할 함수 · 도구 이름
                                        description=mcp_tool.description,     # 설명 (AI 가 읽어요)
                                        args_schema=mcp_tool.input_schema)    # 받는 값의 모양 (서버가 알려 준 것)


def make_langchain_tools(server_file, only=None):
    """MCP 서버의 도구를 LangChain 도구 목록으로 만들어요.
    only 에 도구 이름 목록을 주면 그 도구만 골라요 (도구가 너무 많으면 AI 가 헷갈리고 요금도 늘어요)."""
    tools = []
    for mcp_tool in list_mcp_tools(server_file):   # 서버의 도구를 하나씩
        if only is not None and mcp_tool.name not in only:   # 고른 목록에 없는 도구는 건너뛰기
            continue
        tools.append(_to_langchain(server_file, mcp_tool))   # LangChain 도구로 바꿔 모으기
    return tools
