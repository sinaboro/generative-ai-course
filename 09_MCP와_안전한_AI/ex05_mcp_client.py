# ex05_mcp_client.py : MCP 클라이언트 — 서버의 도구 목록을 보고, 도구를 직접 불러 보기
# 흐름: ① 서버에 "어떤 도구가 있어?" 묻기 (이름 · 설명 · 받는 값)
#       → ② 도구 이름과 넣을 값을 정해 직접 실행해 보기 (AI 없이 우리가 직접!)
from mcp_helper import call_mcp_tool, list_mcp_tools   # 어려운 async 부분을 숨긴 도우미

SERVER = "mcp_server.py"                      # 켤 서버 파일

for tool in list_mcp_tools(SERVER):           # ① 서버에 어떤 도구가 있나?
    print("도구:", tool.name, "-", tool.description, "| 받는 값:", list(tool.input_schema["properties"]))
    #                                                   ↑ 받는 값의 모양(사전)에서 칸 이름만 목록으로

print("add_memo →", call_mcp_tool(SERVER, "add_memo", {"text": "MCP 실습 시작"}))   # ② 도구 부르기
print("list_memos →", call_mcp_tool(SERVER, "list_memos", {}))   # 받는 값이 없으면 빈 사전 {}
print("today →", call_mcp_tool(SERVER, "today", {}))
