# ex06_conditional.py : 갈림길 — 문의를 분류해서 담당 노드로 보내기
# ── 전체 흐름 ──────────────────────────────────────────────
# START → classify(AI 가 문의를 환불 · 배송 · 기타 중 하나로 분류)
#       → route 함수가 분류 결과를 보고 갈 길을 하나 고름 (갈림길 = 조건 엣지)
#           ├ 환불 → refund 노드 (정해 둔 안내)
#           ├ 배송 → delivery 노드 (정해 둔 안내)
#           └ 기타 → other 노드 (AI 가 답을 씀)
#       → 어느 길이든 END
# 그림(images/ex06_graph.png)에서 classify 에서 나가는 점선 화살표 3개가 갈림길이에요
# ────────────────────────────────────────────────────────
from typing import Literal, TypedDict         # "이 중 하나" · 메모장 칸

from langgraph.graph import END, START, StateGraph   # 그래프 도구
from pydantic import BaseModel                # 분류 결과 모양

from common import get_llm                    # AI 를 만드는 함수
from graph_image import save_graph            # 그래프 그림 저장 도우미

llm = get_llm(temperature=0)


class Category(BaseModel):                    # 분류 결과 양식 (Part 04 의 구조화 출력)
    category: Literal["환불", "배송", "기타"]  # 셋 중 하나만


classifier = llm.with_structured_output(Category)   # Category 모양으로만 답하는 분류기


class State(TypedDict):                       # 메모장 칸
    question: str                             # 고객 문의
    category: str                             # classify 가 채움
    answer: str                               # 담당 노드가 채움


def classify(state: State):                   # 노드: 분류하기
    result = classifier.invoke("고객 문의를 분류해: " + state["question"])
    return {"category": result.category}


def refund(state: State):                     # 노드: 환불 담당
    return {"answer": "환불 담당: 주문 번호를 알려 주시면 3일 안에 처리해 드려요."}


def delivery(state: State):                   # 노드: 배송 담당
    return {"answer": "배송 담당: 운송장 번호로 배송 위치를 확인해 드릴게요."}


def other(state: State):                      # 노드: 그 밖의 문의는 AI 가 답해요
    answer = llm.invoke("고객센터 상담원으로서 친절하게 한 문장으로 답해: " + state["question"])
    return {"answer": "상담원: " + answer.content}


def route(state: State):
    """분류 결과를 보고 다음에 갈 노드 이름을 돌려줘요 (갈림길 표지판)."""
    if state["category"] == "환불":
        return "refund"
    if state["category"] == "배송":
        return "delivery"
    return "other"                            # 나머지는 모두 other 로


graph = StateGraph(State)
graph.add_node("classify", classify)          # 노드 4개 등록
graph.add_node("refund", refund)
graph.add_node("delivery", delivery)
graph.add_node("other", other)
graph.add_edge(START, "classify")             # 시작하면 먼저 분류
graph.add_conditional_edges("classify", route,   # ⭐ classify 다음은 route 함수가 정해요
                            ["refund", "delivery", "other"])   # 갈 수 있는 노드 목록 (그림에도 갈림길이 그려져요)
graph.add_edge("refund", END)                 # 담당 노드는 모두 끝으로
graph.add_edge("delivery", END)
graph.add_edge("other", END)
app = graph.compile()
save_graph(app, "ex06_graph.png")             # 갈림길 그림 → images/ex06_graph.png

for question in ["어제 산 신발 환불하고 싶어요", "주문한 책이 아직 안 왔어요", "매장 영업시간이 언제예요?"]:
    result = app.invoke({"question": question})   # 처음 메모장에는 question 만
    print("[" + result["category"] + "]", question)
    print("   →", result["answer"])
