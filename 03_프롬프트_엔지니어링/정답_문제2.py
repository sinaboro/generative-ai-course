# 정답_문제2.py : few-shot 으로 고객 문의를 '주제 / 중요도' 로 분류하기
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from common import get_llm

template = ChatPromptTemplate.from_template("""고객 문의를 분류해. 예시처럼 '주제 / 중요도(높음·보통·낮음)' 한 줄로만 답해.

문의: 결제가 두 번 됐어요. 빨리 환불해 주세요.
답: 결제 / 높음

문의: 영업시간이 어떻게 되나요?
답: 안내 / 낮음

문의: {question}
답:""")
chain = template | get_llm(temperature=0) | StrOutputParser()

questions = ["비밀번호를 잊어버려서 로그인이 안 돼요.", "다음 달 신제품은 언제 나오나요?", "주문한 물건이 일주일째 안 와요."]
for question in questions:
    print(question, "→", chain.invoke({"question": question}))
