# 정답_문제1.py : 구조화 출력으로 문장에서 일정 정보 뽑기
# ── 전체 흐름 ──────────────────────────────────────────────
# ① Schedule 모양(일정 · 날짜 · 시각 · 장소) 정하기
# ② 규칙(system: 지어내지 말고 '미정') + 문장(human) 틀 만들기
# ③ 틀 | Schedule 모양으로 답하는 AI 체인 → ④ 문장마다 실행해 칸을 꺼내 출력
# ────────────────────────────────────────────────────────
from langchain_core.prompts import ChatPromptTemplate   # 질문 틀
from pydantic import BaseModel, Field                   # 모양(설계도) 도구

from common import get_llm                    # AI 를 만드는 함수


class Schedule(BaseModel):                    # ① 칸 이름을 title 로 하면 'Schedule' 이 들어가서 event 로 했어요
    event: str = Field(description="무슨 일정인지 짧게. 예: 스터디 모임")
    date: str = Field(description="날짜")
    time: str = Field(description="시각")
    place: str = Field(description="장소")


template = ChatPromptTemplate.from_messages([   # ② 규칙 + 빈칸 {sentence}
    ("system", "문장에서 일정 정보를 뽑아. 날짜는 문장에 쓰인 말 그대로 쓰고, "
               "문장에 없는 정보는 지어내지 말고 '미정' 이라고 써."),
    ("human", "{sentence}"),
])
chain = template | get_llm(temperature=0).with_structured_output(Schedule)   # ③ 템플릿 | 구조화 AI

sentences = [
    "5월 3일 오후 2시에 강남역 스터디카페에서 파이썬 스터디 모임이 있어.",
    "다음 주 금요일 저녁 7시, 엄마 생신 저녁 식사는 집 앞 한식당에서 해요.",
    "치과 예약은 6월 10일이에요.",            # 시각 · 장소가 없어요 → '미정' 이 나와야 해요
]

for sentence in sentences:                    # ④ 문장마다
    plan = chain.invoke({"sentence": sentence})   # Schedule 객체로 받기
    print(plan.date, "|", plan.time, "|", plan.place, "|", plan.event)
