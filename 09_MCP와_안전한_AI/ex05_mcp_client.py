# ex05_mcp_client.py : MCP 클라이언트 — 서버의 도구 목록을 보고, 도구를 직접 불러 보기
from mcp_helper import call_mcp_tool, list_mcp_tools

SERVER = "mcp_server.py"

for tool in list_mcp_tools(SERVER):           # ① 서버에 어떤 도구가 있나?
    print("도구:", tool.name, "-", tool.description, "| 받는 값:", list(tool.input_schema["properties"]))

print("add_memo →", call_mcp_tool(SERVER, "add_memo", {"text": "MCP 실습 시작"}))   # ② 도구 부르기
print("list_memos →", call_mcp_tool(SERVER, "list_memos", {}))
print("today →", call_mcp_tool(SERVER, "today", {}))
