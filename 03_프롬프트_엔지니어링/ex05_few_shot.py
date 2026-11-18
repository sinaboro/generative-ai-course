# ex05_few_shot.py : 예시를 보여 주고 따라 하게 하기 (Few-shot)
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from common import get_llm

template = ChatPromptTemplate.from_template("""상품 후기의 감정을 분류해. 아래 예시처럼 '감정 | 이유' 한 줄로만 답해.

후기: 색이 사진이랑 똑같고 예뻐요
답: 긍정 | 색이 사진과 같음

후기: 사이즈가 너무 작아서 반품했어요
답: 부정 | 사이즈가 작음

후기: {review}
답:""")
chain = template | get_llm(temperature=0) | StrOutputParser()

reviews = ["배송이 하루 만에 왔어요. 최고!", "포장이 찢어져서 왔네요.", "그냥 그래요. 가격만큼이에요."]
for review in reviews:
    print(review, "→", chain.invoke({"review": review}))
