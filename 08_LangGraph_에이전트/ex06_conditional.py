# ex06_conditional.py : 갈림길 — 문의를 분류해서 담당 노드로 보내기
from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel

from common import get_llm

llm = get_llm(temperature=0)


class Category(BaseModel):                    # 분류 결과 양식 (Part 04 의 구조화 출력)
    category: Literal["환불", "배송", "기타"]


classifier = llm.with_structured_output(Category)


class State(TypedDict):
    question: str
    category: str
    answer: str


def classify(state: State):
    result = classifier.invoke("고객 문의를 분류해: " + state["question"])
    return {"category": result.category}


def refund(state: State):
    return {"answer": "환불 담당: 주문 번호를 알려 주시면 3일 안에 처리해 드려요."}


def delivery(state: State):
    return {"answer": "배송 담당: 운송장 번호로 배송 위치를 확인해 드릴게요."}


def other(state: State):
    answer = llm.invoke("고객센터 상담원으로서 친절하게 한 문장으로 답해: " + state["question"])
    return {"answer": "상담원: " + answer.content}


def route(state: State):
    """분류 결과를 보고 다음에 갈 노드 이름을 돌려줘요 (갈림길 표지판)."""
    if state["category"] == "환불":
        return "refund"
    if state["category"] == "배송":
        return "delivery"
    return "other"


graph = StateGraph(State)
graph.add_node("classify", classify)
graph.add_node("refund", refund)
graph.add_node("delivery", delivery)
graph.add_node("other", other)
graph.add_edge(START, "classify")
graph.add_conditional_edges("classify", route)   # ⭐ classify 다음은 route 함수가 정해요
graph.add_edge("refund", END)
graph.add_edge("delivery", END)
graph.add_edge("other", END)
app = graph.compile()

for question in ["어제 산 신발 환불하고 싶어요", "주문한 책이 아직 안 왔어요", "매장 영업시간이 언제예요?"]:
    result = app.invoke({"question": question})
    print("[" + result["category"] + "]", question)
    print("   →", result["answer"])
