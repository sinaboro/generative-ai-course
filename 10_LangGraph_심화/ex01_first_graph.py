# ex01_first_graph.py : LangGraph 기초 — State(상태) · Node(할 일) · Edge(순서)
# LLM 없이 그래프의 뼈대만 먼저 익혀요
from typing import TypedDict

from langgraph.graph import END, START, StateGraph


class State(TypedDict):          # ① 노드들이 함께 보고 고치는 "공유 메모장"
    name: str
    message: str


def greet(state: State):          # ② 노드 = 상태를 받아 바꿀 부분만 돌려주는 함수
    return {"message": f"안녕하세요, {state['name']}님"}


def cheer(state: State):
    return {"message": state["message"] + "! 오늘도 화이팅!"}


g = StateGraph(State)
g.add_node("greet", greet)
g.add_node("cheer", cheer)
g.add_edge(START, "greet")        # ③ 엣지 = 다음에 갈 노드
g.add_edge("greet", "cheer")
g.add_edge("cheer", END)
app = g.compile()                 # ④ 실행할 수 있는 그래프로 만들기

result = app.invoke({"name": "민지", "message": ""})
print(result)
print(app.get_graph().draw_mermaid())    # 그래프 모양을 글자(mermaid)로 보기
