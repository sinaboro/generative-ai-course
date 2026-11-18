# ex05_llm_nodes.py : 노드 안에서 AI 쓰기 — 요약 → 번역 두 단계 흐름
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common import get_llm

llm = get_llm(temperature=0)


class State(TypedDict):
    text: str        # 처음 글
    summary: str     # 요약 노드가 채우는 칸
    english: str     # 번역 노드가 채우는 칸


def summarize(state: State):
    answer = llm.invoke("다음 글을 한 문장으로 요약해: " + state["text"])
    return {"summary": answer.content}


def translate(state: State):
    answer = llm.invoke("다음 문장을 영어로 번역해. 번역문만 써: " + state["summary"])
    return {"english": answer.content}


graph = StateGraph(State)
graph.add_node("summarize", summarize)
graph.add_node("translate", translate)
graph.add_edge(START, "summarize")
graph.add_edge("summarize", "translate")
graph.add_edge("translate", END)
app = graph.compile()

text = ("우리 팀은 드론으로 찍은 바다 사진에서 플라스틱 병과 캔을 찾는 AI 를 만들었어요. "
        "YOLO 모델로 쓰레기 위치를 찾고, 웹 화면에서 결과 지도와 개수를 보여 줘요.")
result = app.invoke({"text": text})
print("요약:", result["summary"])
print("영어:", result["english"])
