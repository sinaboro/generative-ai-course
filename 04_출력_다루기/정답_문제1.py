# 정답_문제1.py : 구조화 출력으로 문장에서 일정 정보 뽑기
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from common import get_llm


class Schedule(BaseModel):
    event: str = Field(description="무슨 일정인지 짧게. 예: 스터디 모임")
    date: str = Field(description="날짜")
    time: str = Field(description="시각")
    place: str = Field(description="장소")


template = ChatPromptTemplate.from_messages([
    ("system", "문장에서 일정 정보를 뽑아. 날짜는 문장에 쓰인 말 그대로 쓰고, "
               "문장에 없는 정보는 지어내지 말고 '미정' 이라고 써."),
    ("human", "{sentence}"),
])
chain = template | get_llm(temperature=0).with_structured_output(Schedule)   # 템플릿 | 구조화 AI

sentences = [
    "5월 3일 오후 2시에 강남역 스터디카페에서 파이썬 스터디 모임이 있어.",
    "다음 주 금요일 저녁 7시, 엄마 생신 저녁 식사는 집 앞 한식당에서 해요.",
    "치과 예약은 6월 10일이에요.",
]

for sentence in sentences:
    plan = chain.invoke({"sentence": sentence})
    print(plan.date, "|", plan.time, "|", plan.place, "|", plan.event)
