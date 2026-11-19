# ex08_notion_mcp.py : 외부 MCP 서버 연결 — 노션(Notion) 공식 MCP 서버로 내 노션 페이지 읽기 · 쓰기
# 준비 (교안 10절): ① Node.js 설치  ② 노션 통합(연결)을 만들고 토큰을 .env 의 NOTION_TOKEN 에 넣기
#                   ③ 노션에 '생성형 AI 실습 노트' 페이지를 만들고, 통합의 '콘텐츠 사용 권한' 에서 그 페이지를 허락
# ── 전체 흐름 ──────────────────────────────────────────────
# ① .env 에서 노션 토큰 읽기 (없으면 안내하고 멈춤)
# ② 노션 MCP 서버를 켜는 설정 만들기 — 우리 서버는 "python 파일", 노션 서버는 "npx 패키지" 로 켜요
# ③ 클라이언트로 직접: 도구가 몇 개인지 보고 → 검색 도구로 실습 페이지 찾기 (ex05 와 같은 방법)
# ④ 에이전트에게 노션 도구 3개만 골라 주고 말로 시키기: 찾기 → 읽기 → 요약, 그리고 한 줄 덧붙이기
# 우리가 만든 mcp_server.py 와 쓰는 법이 똑같아요. 서버만 바꿔 끼우면 되는 것이 MCP 의 힘이에요
# ────────────────────────────────────────────────────────
import json                                   # 노션이 돌려준 JSON 글자 → 사전
import os                                     # 환경 변수 읽기
import sys                                    # 운영체제 확인 · 프로그램 멈추기

from dotenv import find_dotenv, load_dotenv   # .env 읽기
from langchain.agents import create_agent     # 에이전트 만들기

from common import get_llm                    # AI 를 만드는 함수
from mcp_helper import call_mcp_tool, list_mcp_tools, make_langchain_tools   # MCP 도우미
from my_tools import show_steps               # 에이전트가 한 일 보여 주기

load_dotenv(find_dotenv())                    # ① .env 파일 읽기
token = os.getenv("NOTION_TOKEN", "")         # 노션 통합 토큰 (ntn_ 로 시작해요)
if token == "":
    sys.exit("먼저 .env 에 NOTION_TOKEN=ntn_... 을 넣어 주세요. (교안 10절의 준비 순서 참고)")

# ② 노션 MCP 서버를 켜는 설정 — "npx -y @notionhq/notion-mcp-server" 명령으로 켜져요
if sys.platform == "win32":                   # Windows 에서는 npx 의 진짜 이름이 npx.cmd 예요
    npx = "npx.cmd"
else:                                         # macOS · Linux
    npx = "npx"
NOTION = {
    "command": npx,                                   # 실행할 명령
    "args": ["-y", "@notionhq/notion-mcp-server"],    # -y: 처음 한 번 내려받을 때 묻지 않고 설치
    "env": {"NOTION_TOKEN": token},                   # 서버에게 토큰을 건네줘요 (코드에 적지 않기!)
}

# ③ 클라이언트로 직접 써 보기
tools = list_mcp_tools(NOTION)                # 노션 서버의 도구 목록
print("노션 서버의 도구 수:", len(tools))
for tool in tools[:5]:                        # 앞의 5개만 이름 보기
    print("   도구:", tool.name)

result_text = call_mcp_tool(NOTION, "API-post-search", {"query": "생성형 AI 실습 노트"})   # 제목으로 검색
found = json.loads(result_text)               # 노션의 답은 JSON 글자 → 사전으로
print("찾은 페이지 수:", len(found["results"]))
for page in found["results"]:                 # 찾은 페이지마다 주소 보기
    print("   ", page["url"])

# ④ 에이전트에게 노션 도구 3개만 주고 말로 시키기
notion_tools = make_langchain_tools(NOTION, only=["API-post-search", "API-retrieve-page-markdown",
                                                  "API-patch-block-children"])   # 찾기 · 읽기 · 덧붙이기
agent = create_agent(
    get_llm(temperature=0),
    tools=notion_tools,
    system_prompt="너는 내 노션을 도와주는 비서야. 페이지는 API-post-search 로 찾고, "
                  "내용은 API-retrieve-page-markdown 으로 읽어. 한국어로 짧게 답해.",
)
for text in ["노션의 '생성형 AI 실습 노트' 페이지를 찾아서 내용을 세 줄로 요약해 줘.",
             "노션의 '생성형 AI 실습 노트' 페이지 맨 아래에 '오늘 MCP 로 노션 연동 실습 완료!' 라는 문단을 한 줄 덧붙여 줘."]:
    result = agent.invoke({"messages": [{"role": "user", "content": text}]})   # 기억이 없어서 요청마다 페이지 이름을 다 적어요
    show_steps(result["messages"])            # 🙋 → 🤖 도구 부탁 → 🔧 결과 → 🤖 답
    print("-" * 40)
