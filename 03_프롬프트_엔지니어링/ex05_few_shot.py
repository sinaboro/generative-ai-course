# ex05_few_shot.py : 예시를 보여 주고 따라 하게 하기 (Few-shot)
# 흐름: ① 질문 틀 안에 "후기 → 답" 예시 2개를 넣어 두고 → ② 새 후기를 빈칸에 넣으면
#       → AI 가 예시와 똑같은 '감정 | 이유' 모양으로 답해요
from langchain_core.output_parsers import StrOutputParser   # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate       # 질문 틀

from common import get_llm                    # AI 를 만드는 함수

# ① 큰따옴표 세 개 """ … """ 는 여러 줄 글자예요. 예시 2개 + 맨 아래에 빈칸 {review}
template = ChatPromptTemplate.from_template("""상품 후기의 감정을 분류해. 아래 예시처럼 '감정 | 이유' 한 줄로만 답해.

후기: 색이 사진이랑 똑같고 예뻐요
답: 긍정 | 색이 사진과 같음

후기: 사이즈가 너무 작아서 반품했어요
답: 부정 | 사이즈가 작음

후기: {review}
답:""")
chain = template | get_llm(temperature=0) | StrOutputParser()   # 틀 → AI → 글자

reviews = ["배송이 하루 만에 왔어요. 최고!", "포장이 찢어져서 왔네요.", "그냥 그래요. 가격만큼이에요."]
for review in reviews:                        # ② 후기를 하나씩 빈칸에 넣어 분류
    print(review, "→", chain.invoke({"review": review}))
