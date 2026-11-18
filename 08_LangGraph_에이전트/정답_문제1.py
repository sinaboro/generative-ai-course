# 정답_문제1.py : 분류 그래프에 '칭찬' 갈림길 더하기
from typing import Literal, TypedDict

from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel

from common import get_llm

llm = get_llm(temperature=0)


class Category(BaseModel):
    category: Literal["환불", "배송", "칭찬", "기타"]      # ① 분류에 칭찬 추가


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


def praise(state: State):                    # ② 칭찬 노드: AI 가 감사 인사를 써요
    answer = llm.invoke("고객의 칭찬에 고객센터로서 감사 인사를 한 문장으로 써: " + state["question"])
    return {"answer": "감사 담당: " + answer.content}


def other(state: State):
    answer = llm.invoke("고객센터 상담원으로서 친절하게 한 문장으로 답해: " + state["question"])
    return {"answer": "상담원: " + answer.content}


def route(state: State):
    if state["category"] == "환불":
        return "refund"
    if state["category"] == "배송":
        return "delivery"
    if state["category"] == "칭찬":            # ③ 갈림길에 칭찬 추가
        return "praise"
    return "other"


graph = StateGraph(State)
graph.add_node("classify", classify)
graph.add_node("refund", refund)
graph.add_node("delivery", delivery)
graph.add_node("praise", praise)
graph.add_node("other", other)
graph.add_edge(START, "classify")
graph.add_conditional_edges("classify", route)
graph.add_edge("refund", END)
graph.add_edge("delivery", END)
graph.add_edge("praise", END)                 # ④ 칭찬 노드도 끝으로
graph.add_edge("other", END)
app = graph.compile()

for question in ["직원분이 정말 친절했어요. 감사합니다!", "환불 신청은 어떻게 해요?", "포장이 예뻐서 선물하기 좋았어요"]:
    result = app.invoke({"question": question})
    print("[" + result["category"] + "]", question)
    print("   →", result["answer"])
