# ex04_first_graph.py : LangGraph 기초 — 상태(State) · 노드(Node) · 엣지(Edge)  (AI 없이 뼈대만)
# ── 전체 흐름 ──────────────────────────────────────────────
# ① 상태: 노드들이 함께 쓰는 메모장의 칸 정하기 (name, message)
# ② 노드: 메모장을 받아 바꿀 칸만 돌려주는 함수 두 개 (greet, cheer)
# ③ 엣지: 순서 정하기  START → greet → cheer → END
# ④ compile → invoke(처음 메모장) → 노드가 차례로 메모장을 고쳐 마지막 메모장이 결과
# ⑤ 그래프 모양을 글자(Mermaid)로 보고, 그림 파일로도 저장
# ────────────────────────────────────────────────────────
from typing import TypedDict                  # 사전의 칸 이름 · 자료형을 정하는 도구

from langgraph.graph import END, START, StateGraph   # 시작 · 끝 표시와 그래프 설계도

from graph_image import save_graph            # 그래프를 그림으로 저장하는 도우미 (이 폴더의 graph_image.py)


class State(TypedDict):          # ① 노드들이 함께 보고 고치는 "공유 메모장"의 칸
    name: str
    message: str


def greet(state: State):          # ② 노드 = 메모장을 받아서, 바꿀 칸만 돌려주는 함수
    return {"message": "안녕하세요, " + state["name"] + "님"}


def cheer(state: State):          #    앞 노드가 쓴 message 뒤에 응원을 덧붙여요
    return {"message": state["message"] + "! 오늘도 화이팅!"}


graph = StateGraph(State)         # 그래프 설계도 만들기
graph.add_node("greet", greet)    # 노드 등록: 이름, 함수
graph.add_node("cheer", cheer)
graph.add_edge(START, "greet")    # ③ 엣지 = 순서. 시작 → greet
graph.add_edge("greet", "cheer")  # greet → cheer
graph.add_edge("cheer", END)      # cheer → 끝
app = graph.compile()             # ④ 실행할 수 있는 앱으로 완성

result = app.invoke({"name": "민지", "message": ""})   # 처음 메모장을 넣고 실행
print(result)                     # 노드 두 개를 지난 마지막 메모장
print(app.get_graph().draw_mermaid())    # ⑤ 그래프 모양을 글자(mermaid 문법)로 보기
save_graph(app, "ex04_graph.png")        #    같은 모양을 그림으로 → images/ex04_graph.png
