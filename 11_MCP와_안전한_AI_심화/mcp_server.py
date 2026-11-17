# mcp_server.py : 나만의 MCP 서버 — AI 가 쓸 수 있는 "도구" 를 표준 방식으로 내놓아요
# 실행은 보통 클라이언트(ex05, ex06 또는 Claude Desktop 같은 앱)가 대신 해 줘요
from datetime import date

from mcp.server import MCPServer

app = MCPServer("memo-server")
NOTES = ["9시 30분 수업 시작", "금요일 프로젝트 발표"]


@app.tool()
def list_notes() -> list[str]:
    """저장된 메모를 모두 보여 줘요."""
    return NOTES


@app.tool()
def add_note(text: str) -> str:
    """새 메모를 저장해요."""
    NOTES.append(text)
    return f"저장했어요 (모두 {len(NOTES)}개)"


@app.tool()
def today() -> str:
    """오늘 날짜를 알려 줘요."""
    return date.today().isoformat()


if __name__ == "__main__":
    app.run()          # 표준 입출력(stdio)으로 클라이언트와 대화해요
