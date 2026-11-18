# 정답_server.py : 문제 2 의 MCP 서버 — 글자 수 세기 · 낱말 수 세기 도구
from mcp.server import MCPServer

server = MCPServer("text-tools")


@server.tool()
def count_chars(text: str) -> int:
    """글자 수를 세요 (빈칸 포함)."""
    return len(text)


@server.tool()
def count_words(text: str) -> int:
    """빈칸으로 나눈 낱말 수를 세요."""
    return len(text.split())


if __name__ == "__main__":
    server.run()
