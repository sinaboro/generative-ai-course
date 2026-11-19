# 정답_server.py : 문제 2 의 MCP 서버 — 글자 수 세기 · 낱말 수 세기 도구
# 흐름: mcp_server.py 와 같아요 — 서버 만들기 → @server.tool() 함수 두 개 → server.run()
from mcp.server import MCPServer              # MCP 서버 도구

server = MCPServer("text-tools")              # 서버 이름


@server.tool()                                # 도구 1
def count_chars(text: str) -> int:
    """글자 수를 세요 (빈칸 포함)."""
    return len(text)


@server.tool()                                # 도구 2
def count_words(text: str) -> int:
    """빈칸으로 나눈 낱말 수를 세요."""
    return len(text.split())                  # 빈칸으로 잘라 몇 조각인지


if __name__ == "__main__":                    # 클라이언트가 켰을 때
    server.run()
