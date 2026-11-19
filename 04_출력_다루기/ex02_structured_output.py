# ex02_structured_output.py : 구조화 출력 — 답을 "정해진 모양" 으로 반드시 받기
# ── 전체 흐름 ──────────────────────────────────────────────
# ① 받고 싶은 답의 모양을 class 로 정하기 (칸 이름 · 자료형 · 설명)
# ② llm.with_structured_output(모양) → "이 모양으로만 답하는 AI" 만들기
# ③ 질문하면 글자가 아니라 Movie 객체가 와요 → movie.title 처럼 바로 꺼내 쓰기
# ────────────────────────────────────────────────────────
from pydantic import BaseModel, Field         # 데이터의 모양(설계도)을 정하는 도구

from common import get_llm                    # AI 를 만드는 함수


# ① 받고 싶은 답의 모양을 class 로 정해요 (칸 이름 : 자료형 = 설명)
class Movie(BaseModel):
    title: str = Field(description="영화 제목")     # 글자
    year: int = Field(description="개봉 연도")      # 정수 → 계산할 수 있어요
    director: str = Field(description="감독 이름")  # description 은 AI 가 읽는 설명이에요


llm = get_llm(temperature=0)
structured_llm = llm.with_structured_output(Movie)   # ② "답은 Movie 모양으로만!"

movie = structured_llm.invoke("영화 '기생충' 의 정보를 알려 줘.")   # ③ 질문
print(movie)                                  # Movie 객체 전체
print("제목:", movie.title)                   # 점(.)으로 칸을 바로 꺼내요
print("감독:", movie.director)
print("개봉 후 지난 해:", 2026 - movie.year, "년")   # year 는 숫자라서 바로 계산돼요
