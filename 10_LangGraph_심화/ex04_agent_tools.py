# ex04_agent_tools.py : 도구를 쓰는 에이전트 — LLM 이 도구를 고르고, 결과를 보고 다시 생각하기
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from common import get_llm


@tool
def calculator(expression: str) -> str:
    """사칙연산 식을 계산해요. 예: '4500*4 + 6000*2'"""
    allowed = set("0123456789+-*/(). ")
    if not set(expression) <= allowed:          # 숫자 · 기호만 허용 (안전)
        return "계산할 수 없는 식이에요"
    return str(eval(expression))


@tool
def exchange_rate(currency: str) -> str:
    """1 단위 외화가 몇 원인지 알려 줘요. currency: USD, JPY, EUR 중 하나"""
    rates = {"USD": 1380, "JPY": 9.2, "EUR": 1495}   # 연습용 고정 환율
    return f"1 {currency} = {rates.get(currency.upper(), '알 수 없음')} 원"


tools = [calculator, exchange_rate]
llm = get_llm().bind_tools(tools)               # ⭐ LLM 에게 쓸 수 있는 도구 목록을 알려 줘요


def agent(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}


g = StateGraph(MessagesState)                   # 대화 메시지 목록을 상태로 쓰는 그래프
g.add_node("agent", agent)
g.add_node("tools", ToolNode(tools))            # 도구를 실제로 실행하는 노드
g.add_edge(START, "agent")
g.add_conditional_edges("agent", tools_condition)   # 도구를 부르려 하면 tools 로, 아니면 끝
g.add_edge("tools", "agent")                    # 도구 결과를 들고 다시 agent 로 (반복)
app = g.compile()

q = "아메리카노 4잔(4,500원)과 케이크 2개(6,000원)의 합계를 달러로 바꾸면 얼마야?"
system = SystemMessage("계산은 반드시 도구로 해. 답은 수식 기호 없이 한국어 두 문장 이내로.")
out = app.invoke({"messages": [system, HumanMessage(q)]})
for m in out["messages"][1:]:                   # system 은 빼고 보여 줘요                       # 어떤 순서로 생각하고 도구를 썼는지 보기
    if m.type == "ai" and m.tool_calls:
        print("AI → 도구 호출:", [(c["name"], c["args"]) for c in m.tool_calls])
    elif m.type == "tool":
        print("도구 결과:", m.content)
    else:
        print(f"{m.type}:", m.content)
