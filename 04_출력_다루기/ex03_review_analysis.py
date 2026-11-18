# ex03_review_analysis.py : 구조화 출력으로 리뷰 여러 개를 분석해 정리하기
from typing import Literal                    # "이 중 하나만" 을 정하는 도구

from pydantic import BaseModel, Field

from common import get_llm


class Review(BaseModel):
    feeling: Literal["긍정", "부정", "중립"] = Field(description="리뷰의 감정")   # 셋 중 하나만
    score: int = Field(description="1 ~ 5 점수. 5 가 가장 좋음")
    good_points: list[str] = Field(description="좋았던 점 목록. 없으면 빈 목록")
    bad_points: list[str] = Field(description="아쉬운 점 목록. 없으면 빈 목록")


analyzer = get_llm(temperature=0).with_structured_output(Review)

reviews = [
    "배송이 하루 만에 왔고 포장도 꼼꼼했어요. 맛도 최고!",
    "맛은 괜찮은데 양이 너무 적고 가격이 비싸요.",
    "주문한 것과 다른 상품이 왔어요. 교환도 느렸습니다.",
]

total_score = 0                               # 점수 합계
for review_text in reviews:
    result = analyzer.invoke(review_text)     # 리뷰 하나 분석
    total_score = total_score + result.score  # score 는 숫자라서 바로 더할 수 있어요
    print("리뷰:", review_text)
    print("  감정:", result.feeling, "| 점수:", result.score)
    print("  좋은 점:", result.good_points)
    print("  아쉬운 점:", result.bad_points)

print("평균 점수:", round(total_score / len(reviews), 1))
