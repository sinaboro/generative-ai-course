# mcp_helper.py : MCP 서버를 쉽게 쓰게 해 주는 도우미 함수 모음
# MCP 라이브러리는 async(비동기) 문법을 써요. 어려운 부분은 이 파일에 숨겨 두었으니,
# 예제에서는 list_mcp_tools · call_mcp_tool · make_langchain_tools 세 함수만 쓰면 돼요.
import asyncio
import sys

from langchain_core.tools import StructuredTool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def _server(server_file):
    """'python 서버파일.py' 로 서버를 켜는 설정"""
    return StdioServerParameters(command=sys.executable, args=[server_file])


async def _list(server_file):
    async with stdio_client(_server(server_file)) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()                    # 서버와 인사 (서로 버전 확인)
            result = await session.list_tools()           # 도구 목록 받기
            return result.tools


async def _call(server_file, name, args):
    async with stdio_client(_server(server_file)) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool(name, args)  # 도구 실행
            texts = []
            for part in result.content:                   # 결과가 여러 조각이면 이어 붙여요
                texts.append(part.text)
            return ", ".join(texts)


def list_mcp_tools(server_file):
    """MCP 서버를 켜서 도구 목록을 받아 와요."""
    return asyncio.run(_list(server_file))


def call_mcp_tool(server_file, name, args):
    """MCP 서버를 켜서 도구 하나를 실행하고 결과 글자를 돌려줘요."""
    return asyncio.run(_call(server_file, name, args))


def _to_langchain(server_file, mcp_tool):
    """MCP 도구 하나를 LangChain 도구로 바꿔요 (Part 08 의 에이전트가 쓸 수 있게)."""
    def run(**kwargs):
        return call_mcp_tool(server_file, mcp_tool.name, kwargs)
    return StructuredTool.from_function(func=run, name=mcp_tool.name,
                                        description=mcp_tool.description, args_schema=mcp_tool.input_schema)


def make_langchain_tools(server_file):
    """MCP 서버의 도구를 모두 LangChain 도구 목록으로 만들어요."""
    tools = []
    for mcp_tool in list_mcp_tools(server_file):
        tools.append(_to_langchain(server_file, mcp_tool))
    return tools
