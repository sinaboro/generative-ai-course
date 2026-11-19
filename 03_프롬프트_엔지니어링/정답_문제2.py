# 정답_문제2.py : few-shot 으로 고객 문의를 '주제 / 중요도' 로 분류하기
# 흐름: ① 예시 2개를 넣은 틀 → ② 체인 → ③ 문의를 하나씩 넣어 '주제 / 중요도' 받기
from langchain_core.output_parsers import StrOutputParser   # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate       # 질문 틀

from common import get_llm                    # AI 를 만드는 함수

# ① 예시(문의 → 답) 2개 + 빈칸 {question}
template = ChatPromptTemplate.from_template("""고객 문의를 분류해. 예시처럼 '주제 / 중요도(높음·보통·낮음)' 한 줄로만 답해.

문의: 결제가 두 번 됐어요. 빨리 환불해 주세요.
답: 결제 / 높음

문의: 영업시간이 어떻게 되나요?
답: 안내 / 낮음

문의: {question}
답:""")
chain = template | get_llm(temperature=0) | StrOutputParser()   # ② 분류는 늘 같게 0

questions = ["비밀번호를 잊어버려서 로그인이 안 돼요.", "다음 달 신제품은 언제 나오나요?", "주문한 물건이 일주일째 안 와요."]
for question in questions:                    # ③ 하나씩 분류
    print(question, "→", chain.invoke({"question": question}))
