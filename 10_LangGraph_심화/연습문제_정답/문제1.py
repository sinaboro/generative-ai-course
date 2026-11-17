# 문제1 정답: 분류에 '칭찬' 갈림길 더하기
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from typing import TypedDict

from langgraph.graph import END, START, StateGraph

from common import get_llm

llm = get_llm()


class State(TypedDict):
    question: str
    category: str
    answer: str


def classify(state):
    r = llm.invoke("다음 글을 '칭찬', '불만' 중 하나의 낱말로만 분류해: " + state["question"])
    return {"category": r.content.strip()}


def thanks(state):
    return {"answer": "감사 인사: 좋은 말씀 감사합니다! 직원들에게 꼭 전할게요."}


def sorry(state):
    return {"answer": "사과: 불편을 드려 죄송합니다. 바로 확인해 볼게요."}


g = StateGraph(State)
g.add_node("classify", classify)
g.add_node("thanks", thanks)
g.add_node("sorry", sorry)
g.add_edge(START, "classify")
g.add_conditional_edges("classify", lambda s: "thanks" if "칭찬" in s["category"] else "sorry")
g.add_edge("thanks", END)
g.add_edge("sorry", END)
app = g.compile()
for q in ["직원분이 정말 친절했어요!", "음식이 너무 늦게 나왔어요."]:
    print(q, "→", app.invoke({"question": q})["answer"])
