# ex02_llm_nodes.py : 노드 안에서 LLM 쓰기 — 요약 → 번역 두 단계 흐름
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common import get_llm

llm = get_llm()


class State(TypedDict):
    text: str
    summary: str
    english: str


def summarize(state: State):
    r = llm.invoke(f"다음 글을 한 문장으로 요약해: {state['text']}")
    return {"summary": r.content}


def translate(state: State):
    r = llm.invoke(f"영어로 번역한 문장만 써: {state['summary']}")
    return {"english": r.content}


g = StateGraph(State)
g.add_node("summarize", summarize)
g.add_node("translate", translate)
g.add_edge(START, "summarize")
g.add_edge("summarize", "translate")
g.add_edge("translate", END)
app = g.compile()

text = ("우리 팀은 드론으로 찍은 바다 사진에서 플라스틱 병과 캔을 찾는 AI 를 만들었어요. "
        "YOLO 모델로 쓰레기 위치를 찾고, 웹 화면에서 결과 지도와 개수를 보여 줘요.")
out = app.invoke({"text": text})
print("요약:", out["summary"])
print("영어:", out["english"])
