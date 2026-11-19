# mcp_server.py : 나만의 MCP 서버 — AI 가 쓸 수 있는 도구를 "표준 방식" 으로 내놓아요
# 이 파일은 직접 실행하지 않아요. 클라이언트(ex05 · ex06, 또는 Claude 같은 AI 앱)가 켜서 써요.
# 흐름: ① 서버 만들기 → ② @server.tool() 을 붙인 함수 3개가 도구가 돼요 (함수 설명 = 도구 설명)
#       → ③ server.run() 으로 켜지면 클라이언트의 "목록 줘 · 실행해 줘" 요청에 답해요
import os                                     # 파일 경로 · 파일이 있는지 확인
from datetime import date                     # 날짜 도구

from mcp.server import MCPServer              # MCP 서버를 쉽게 만드는 도구

server = MCPServer("memo-server")             # ① 서버 이름
MEMO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "memos.txt")   # 메모를 저장할 파일
# ↑ __file__ = 이 파일의 경로 → 그 폴더 안의 memos.txt (어느 폴더에서 켜도 같은 파일을 써요)


def read_memos():
    """메모 파일을 읽어 줄 목록으로 돌려줘요. 파일이 없으면 빈 목록."""
    if not os.path.exists(MEMO_FILE):
        return []
    with open(MEMO_FILE, encoding="utf-8") as file:
        return file.read().splitlines()      # 파일 전체 → 줄 목록


@server.tool()                                # ⭐ ② 이 함수를 MCP 도구로 내놓아요
def list_memos() -> list[str]:
    """저장된 메모를 모두 보여 줘요."""
    return read_memos()


@server.tool()
def add_memo(text: str) -> str:
    """새 메모를 저장해요."""
    with open(MEMO_FILE, "a", encoding="utf-8") as file:   # "a" = 파일 끝에 덧붙이기
        file.write(text + "\n")                             # 메모 한 줄
    return "저장했어요. 메모가 모두 " + str(len(read_memos())) + "개예요."


@server.tool()
def today() -> str:
    """오늘 날짜를 알려 줘요."""
    return date.today().isoformat()           # 예: "2026-11-20"


if __name__ == "__main__":                    # 이 파일이 직접 켜졌을 때만
    server.run()                              # ③ 표준 입출력(stdio)으로 클라이언트와 이야기해요
