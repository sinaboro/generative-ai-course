# ex03_few_shot.py : Few-shot — 예시를 몇 개 보여 주고 같은 방식으로 답하게 하기
# 설명을 길게 쓰는 것보다 예시 2 ~ 3개가 더 정확하게 형식을 맞춰 줄 때가 많아요
from llm import ask

reviews = ["배송이 하루 만에 왔어요. 최고!", "포장이 찢어져서 왔네요.", "그냥 그래요. 가격만큼이에요."]

prompt_template = """상품 후기의 감정을 분류해. 아래 예시처럼 '감정 | 이유' 한 줄로만 답해.

후기: 색이 사진이랑 똑같고 예뻐요
답: 긍정 | 색이 사진과 같음

후기: 사이즈가 너무 작아서 반품했어요
답: 부정 | 사이즈가 작음

후기: {review}
답:"""

for r in reviews:
    answer = ask(prompt_template.format(review=r), temperature=0)
    print(f"{r}  →  {answer}")
