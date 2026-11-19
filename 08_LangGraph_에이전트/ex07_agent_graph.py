# ex07_agent_graph.py : 에이전트를 그래프로 — agent 노드 ↔ tools 노드를 오가며 반복
# ── 전체 흐름 ──────────────────────────────────────────────
# 메모장 = 대화 메시지 목록 (MessagesState)
# START → agent(AI 가 생각) → tools_condition 이 확인:
#           도구 부탁이 있으면 → tools(도구 실행, 결과를 메시지에 붙임) → 다시 agent 로 (반복)
#           부탁이 없으면     → END (마지막 AI 메시지가 답)
# ex03 의 while 반복을 그래프의 "고리(agent ↔ tools)" 로 바꾼 거예요. 그림에서 고리를 찾아보세요
# ────────────────────────────────────────────────────────
from langchain_core.messages import HumanMessage, SystemMessage   # 사람 · 규칙 메시지
from langgraph.graph import START, MessagesState, StateGraph       # 그래프 도구 · 메시지 메모장
from langgraph.prebuilt import ToolNode, tools_condition           # 도구 실행 노드 · 갈림길 함수

from common import get_llm                    # AI 를 만드는 함수
from graph_image import save_graph            # 그래프 그림 저장 도우미
from my_tools import calculator, exchange_rate, show_steps   # 도구 · 과정 보여 주기

tools = [calculator, exchange_rate]
llm_with_tools = get_llm(temperature=0).bind_tools(tools)   # 도구 목록을 아는 AI


def agent(state: MessagesState):              # AI 가 생각하는 노드
    answer = llm_with_tools.invoke(state["messages"])   # 지금까지의 대화를 보고 답 또는 도구 부탁
    return {"messages": [answer]}             # 메시지 목록에 AI 의 답을 더해요


graph = StateGraph(MessagesState)             # 상태 = 대화 메시지 목록
graph.add_node("agent", agent)
graph.add_node("tools", ToolNode(tools))      # ⭐ 도구를 실제로 실행해 주는 노드 (ex03 의 for 문)
graph.add_edge(START, "agent")
graph.add_conditional_edges("agent", tools_condition)   # ⭐ 도구 부탁이 있으면 tools 로, 없으면 끝
graph.add_edge("tools", "agent")              # 도구 결과를 들고 다시 agent 로 (반복)
app = graph.compile()

print(app.get_graph().draw_mermaid())         # 그래프 모양을 글자로
save_graph(app, "ex07_graph.png")             # 같은 모양을 그림으로 → images/ex07_graph.png
system = SystemMessage("계산은 반드시 calculator 도구로 해. 답은 한국어 두 문장 이내로.")
question = HumanMessage("일본 여행에서 3만 엔을 쓰고, 미국 여행에서 200달러를 썼어. 우리 돈으로 모두 얼마야?")
result = app.invoke({"messages": [system, question]})   # 처음 메모장 = 규칙 + 질문
show_steps(result["messages"])                # 생각 → 도구 → 결과 → 답 을 차례로 보여 주기
