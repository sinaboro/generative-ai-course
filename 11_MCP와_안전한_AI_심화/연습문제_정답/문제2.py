# 문제2 정답: MCP 서버에 글자 수 세기 도구를 더하고 클라이언트로 불러 보기
import asyncio
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_CODE = Path(__file__).resolve().parent / "my_server.py"   # 같은 폴더의 서버 파일


async def main():
    params = StdioServerParameters(command=sys.executable, args=[str(SERVER_CODE)])
    async with stdio_client(params) as (r, w):
        async with ClientSession(r, w) as s:
            await s.initialize()
            print([t.name for t in (await s.list_tools()).tools])
            res = await s.call_tool("count_chars", {"text": "생성형 AI 과정 심화"})
            print("글자 수:", res.content[0].text)


asyncio.run(main())
