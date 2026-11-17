# ex03_conditional.py : 조건에 따라 갈림길 — 고객 문의를 분류해서 담당 노드로 보내기
from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph

from common import get_llm

llm = get_llm()


class State(TypedDict):
    question: str
    category: str
    answer: str


def classify(state: State):
    r = llm.invoke("다음 문의를 '환불', '배송', '기타' 중 하나의 낱말로만 분류해: " + state["question"])
    return {"category": r.content.strip()}


def refund(state: State):
    return {"answer": "환불 담당: 주문 번호를 알려 주시면 3일 안에 처리해 드려요."}


def delivery(state: State):
    return {"answer": "배송 담당: 운송장 번호로 배송 위치를 확인해 드릴게요."}


def other(state: State):
    r = llm.invoke("친절하게 한 문장으로 답해: " + state["question"])
    return {"answer": "상담원: " + r.content}


def route(state: State) -> Literal["refund", "delivery", "other"]:
    """분류 결과를 보고 다음 노드 이름을 돌려줘요 (갈림길)."""
    if "환불" in state["category"]:
        return "refund"
    if "배송" in state["category"]:
        return "delivery"
    return "other"


g = StateGraph(State)
for name, fn in [("classify", classify), ("refund", refund), ("delivery", delivery), ("other", other)]:
    g.add_node(name, fn)
g.add_edge(START, "classify")
g.add_conditional_edges("classify", route)     # ⭐ classify 다음은 route 함수가 정해요
for name in ["refund", "delivery", "other"]:
    g.add_edge(name, END)
app = g.compile()

for q in ["어제 산 신발 환불하고 싶어요", "주문한 책이 아직 안 왔어요", "매장 영업시간이 언제예요?"]:
    out = app.invoke({"question": q})
    print(f"[{out['category']}] {q}")
    print("   →", out["answer"])
