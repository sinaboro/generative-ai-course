# ex03_structured_output.py : 답을 파이썬 객체로 받기 (구조화 출력) — 형식이 틀릴 걱정이 없어요
from pydantic import BaseModel, Field

from common import get_llm


class Review(BaseModel):
    """상품 후기 분석 결과"""
    sentiment: str = Field(description="긍정, 부정, 중립 중 하나")
    score: int = Field(description="1 ~ 5 점")
    keywords: list[str] = Field(description="핵심 낱말 2 ~ 3개")


analyzer = get_llm().with_structured_output(Review)  # 답을 Review 모양으로 받게 해요

for text in ["배송이 빠르고 포장도 꼼꼼했어요. 또 살게요!", "색이 사진과 너무 달라서 실망했어요."]:
    r = analyzer.invoke(f"이 상품 후기를 분석해 줘: {text}")
    print(type(r).__name__, "|", r.sentiment, r.score, r.keywords)   # 점(.)으로 바로 꺼내요
