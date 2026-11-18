# ex04_llm_judge.py : AI 채점관 — "낱말이 들어 있나?" 대신 AI 가 뜻을 보고 채점해요
from pydantic import BaseModel, Field

from common import get_llm


class Grade(BaseModel):
    correct: bool = Field(description="챗봇 답이 모범 답안과 뜻이 같으면 True")
    reason: str = Field(description="그렇게 판단한 까닭 한 문장")


judge = get_llm(temperature=0).with_structured_output(Grade)

# Part 07 문제 1 에서 chunk_size 30 일 때 실제로 나온 답들 [질문, 모범 답안, 챗봇 답, 낱말 검사용 말]
cases = [
    ["8시 30분에 출근하면 몇 시에 퇴근해?", "오후 5시 30분", "8시 30분에 출근하면 오후 5시에 퇴근합니다.", "5시 30분"],
    ["출장비 정산을 7일 넘겨서 내면 어떻게 돼?", "정산을 받을 수 없다", "출장비 정산서를 7일이 지나서 내면 정산이 불가능합니다.", "받을 수 없"],
    ["월요일에 재택근무해도 돼?", "안 된다. 월요일은 전체 회의가 있어 재택근무를 할 수 없다",
     "월요일에 회의가 없다면 재택근무가 가능하지만, 회의가 있다면 재택근무를 할 수 없습니다.", "없"],
    ["연차는 1년에 며칠 받아?", "15일", "입사 1년이 지난 직원은 해마다 연차 휴가 15일을 받습니다.", "15"],
]

for question, reference, answer, keyword in cases:
    if keyword in answer:
        keyword_result = "O"
    else:
        keyword_result = "X"
    grade = judge.invoke("질문: " + question + "\n모범 답안: " + reference + "\n챗봇 답: " + answer +
                         "\n챗봇 답이 모범 답안과 뜻이 같은지 채점해.")
    if grade.correct:
        judge_result = "O"
    else:
        judge_result = "X"
    print("질문:", question)
    print("   낱말 검사:", keyword_result, "| AI 채점:", judge_result, "-", grade.reason)
