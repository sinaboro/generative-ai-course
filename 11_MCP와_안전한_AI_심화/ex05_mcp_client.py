# ex05_mcp_client.py : MCP 클라이언트 — 서버를 켜고, 도구 목록을 보고, 도구를 불러요
import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER = StdioServerParameters(command=sys.executable, args=["mcp_server.py"])


async def main():
    async with stdio_client(SERVER) as (read, write):        # ① 서버 프로그램 실행 + 연결
        async with ClientSession(read, write) as session:
            await session.initialize()                       # ② 인사 (서로 버전 확인)
            tools = await session.list_tools()               # ③ 어떤 도구가 있나?
            for t in tools.tools:
                print(f"도구: {t.name:10s} - {t.description}")
            r = await session.call_tool("add_note", {"text": "MCP 실습 완료"})   # ④ 도구 부르기
            print("add_note →", r.content[0].text)
            r = await session.call_tool("list_notes", {})
            print("list_notes →", r.structured_content)


asyncio.run(main())
