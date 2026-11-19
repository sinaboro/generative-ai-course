# ex08_create_agent.py : create_agent — 에이전트를 한 줄로 만들기 + RAG 를 도구로 쓰기
# ── 전체 흐름 ──────────────────────────────────────────────
# create_agent 가 ex07 의 그래프(model ↔ tools 고리)를 대신 만들어 줘요
# 질문 → model(AI) 이 search_faq 로 규정 검색 → calculator 로 계산 → 답
# 그림(images/ex08_graph.png)을 ex07 그림과 비교해 보세요 — 노드 이름만 다르고 모양은 같아요
# ────────────────────────────────────────────────────────
from langchain.agents import create_agent     # 에이전트를 한 번에 만드는 함수

from common import get_llm                    # AI 를 만드는 함수
from graph_image import save_graph            # 그래프 그림 저장 도우미
from my_tools import calculator, search_faq, show_steps   # 계산기 · 안내문 검색 · 과정 보기

agent = create_agent(
    get_llm(temperature=0),                   # 생각할 AI
    tools=[search_faq, calculator],           # 안내문 검색(RAG) + 계산기
    system_prompt="너는 새싹전자 고객센터 상담원이야. 규정은 search_faq 로 찾고, 계산은 calculator 로 해. "
                  "안내문에 없는 내용은 지어내지 마.",
)
save_graph(agent, "ex08_graph.png")           # create_agent 가 만든 그래프도 그림으로 볼 수 있어요

question = "2만 5천 원어치 사면 배송비까지 모두 얼마예요?"
result = agent.invoke({"messages": [{"role": "user", "content": question}]})   # 사전 모양으로도 메시지를 줄 수 있어요
show_steps(result["messages"])
