# 문제2 정답: 단위 변환 도구를 더한 에이전트
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from common import get_llm


@tool
def cm_to_inch(cm: float) -> str:
    """센티미터를 인치로 바꿔요."""
    return f"{cm} cm = {cm / 2.54:.2f} inch"


tools = [cm_to_inch]
llm = get_llm().bind_tools(tools)
g = StateGraph(MessagesState)
g.add_node("agent", lambda s: {"messages": [llm.invoke(s["messages"])]})
g.add_node("tools", ToolNode(tools))
g.add_edge(START, "agent")
g.add_conditional_edges("agent", tools_condition)
g.add_edge("tools", "agent")
app = g.compile()
out = app.invoke({"messages": [HumanMessage("모니터 화면 대각선이 68.6cm 면 몇 인치야?")]})
print(out["messages"][-1].content)
