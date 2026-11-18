# ex07_agent_graph.py : 에이전트를 그래프로 — agent 노드 ↔ tools 노드를 오가며 반복
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from common import get_llm
from my_tools import calculator, exchange_rate, show_steps

tools = [calculator, exchange_rate]
llm_with_tools = get_llm(temperature=0).bind_tools(tools)


def agent(state: MessagesState):              # AI 가 생각하는 노드
    answer = llm_with_tools.invoke(state["messages"])
    return {"messages": [answer]}             # 메시지 목록에 AI 의 답을 더해요


graph = StateGraph(MessagesState)             # 상태 = 대화 메시지 목록
graph.add_node("agent", agent)
graph.add_node("tools", ToolNode(tools))      # ⭐ 도구를 실제로 실행해 주는 노드 (ex03 의 for 문)
graph.add_edge(START, "agent")
graph.add_conditional_edges("agent", tools_condition)   # ⭐ 도구 부탁이 있으면 tools 로, 없으면 끝
graph.add_edge("tools", "agent")              # 도구 결과를 들고 다시 agent 로 (반복)
app = graph.compile()

print(app.get_graph().draw_mermaid())
system = SystemMessage("계산은 반드시 calculator 도구로 해. 답은 한국어 두 문장 이내로.")
question = HumanMessage("일본 여행에서 3만 엔을 쓰고, 미국 여행에서 200달러를 썼어. 우리 돈으로 모두 얼마야?")
result = app.invoke({"messages": [system, question]})
show_steps(result["messages"])
