# ex04_first_graph.py : LangGraph 기초 — 상태(State) · 노드(Node) · 엣지(Edge)  (AI 없이 뼈대만)
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class State(TypedDict):          # ① 노드들이 함께 보고 고치는 "공유 메모장"의 칸
    name: str
    message: str


def greet(state: State):          # ② 노드 = 메모장을 받아서, 바꿀 칸만 돌려주는 함수
    return {"message": "안녕하세요, " + state["name"] + "님"}


def cheer(state: State):
    return {"message": state["message"] + "! 오늘도 화이팅!"}


graph = StateGraph(State)         # 그래프 설계도 만들기
graph.add_node("greet", greet)    # 노드 등록: 이름, 함수
graph.add_node("cheer", cheer)
graph.add_edge(START, "greet")    # ③ 엣지 = 순서. 시작 → greet
graph.add_edge("greet", "cheer")  # greet → cheer
graph.add_edge("cheer", END)      # cheer → 끝
app = graph.compile()             # ④ 실행할 수 있는 앱으로 완성

result = app.invoke({"name": "민지", "message": ""})   # 처음 메모장을 넣고 실행
print(result)
print(app.get_graph().draw_mermaid())    # 그래프 모양을 글자(mermaid 문법)로 보기
