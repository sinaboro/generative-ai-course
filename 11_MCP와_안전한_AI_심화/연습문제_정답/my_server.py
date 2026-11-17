# my_server.py : 문제2 정답의 MCP 서버 — 글자 수 세기 도구 하나
from mcp.server import MCPServer

app = MCPServer("count-server")


@app.tool()
def count_chars(text: str) -> int:
    """빈칸을 빼고 글자 수를 세요."""
    return len(text.replace(" ", ""))


if __name__ == "__main__":
    app.run()
