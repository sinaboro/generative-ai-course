# ex05_llm_nodes.py : 노드 안에서 AI 쓰기 — 요약 → 번역 두 단계 흐름
# ── 전체 흐름 ──────────────────────────────────────────────
# 메모장 칸: text(처음 글) · summary(요약) · english(번역)
# START → summarize 노드(text 를 읽고 summary 를 채움) → translate 노드(summary 를 읽고 english 를 채움) → END
# 앞 노드가 채운 칸을 다음 노드가 읽어서 쓰는 것이 핵심이에요
# ────────────────────────────────────────────────────────
from typing import TypedDict                  # 메모장 칸 정하기

from langgraph.graph import END, START, StateGraph   # 그래프 도구

from common import get_llm                    # AI 를 만드는 함수
from graph_image import save_graph            # 그래프 그림 저장 도우미

llm = get_llm(temperature=0)


class State(TypedDict):
    text: str        # 처음 글
    summary: str     # 요약 노드가 채우는 칸
    english: str     # 번역 노드가 채우는 칸


def summarize(state: State):                  # 노드 1: 요약
    answer = llm.invoke("다음 글을 한 문장으로 요약해: " + state["text"])
    return {"summary": answer.content}        # summary 칸만 채워서 돌려줘요


def translate(state: State):                  # 노드 2: 번역 (노드 1 이 채운 summary 를 읽어요)
    answer = llm.invoke("다음 문장을 영어로 번역해. 번역문만 써: " + state["summary"])
    return {"english": answer.content}


graph = StateGraph(State)                     # 설계도
graph.add_node("summarize", summarize)        # 노드 등록
graph.add_node("translate", translate)
graph.add_edge(START, "summarize")            # 순서: 시작 → 요약 → 번역 → 끝
graph.add_edge("summarize", "translate")
graph.add_edge("translate", END)
app = graph.compile()                         # 완성
save_graph(app, "ex05_graph.png")             # 노드 흐름 그림 → images/ex05_graph.png

text = ("우리 팀은 드론으로 찍은 바다 사진에서 플라스틱 병과 캔을 찾는 AI 를 만들었어요. "
        "YOLO 모델로 쓰레기 위치를 찾고, 웹 화면에서 결과 지도와 개수를 보여 줘요.")
result = app.invoke({"text": text})           # 처음 메모장에는 text 만 넣어요
print("요약:", result["summary"])
print("영어:", result["english"])
