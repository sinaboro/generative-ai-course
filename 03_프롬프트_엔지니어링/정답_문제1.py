# 정답_문제1.py : 이메일 작성 체인 — 역할(system) + 형식 + 길이
# 흐름: ① 역할과 형식을 정한 틀 → ② 틀 | AI | 글자 체인 → ③ 받는 사람 · 내용을 넣어 실행
from langchain_core.output_parsers import StrOutputParser   # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate       # 질문 틀

from common import get_llm                    # AI 를 만드는 함수

template = ChatPromptTemplate.from_messages([   # ① 빈칸 두 개: {to}, {content}
    ("system", "너는 신입사원의 이메일을 다듬어 주는 비서야. 공손하지만 짧게 써."),
    ("human", "{to}께 보낼 이메일을 써 줘. 내용: {content}. 형식: 제목 한 줄, 본문 3 ~ 4문장, 마지막에 이름 '홍길동'."),
])
chain = template | get_llm(temperature=0.3) | StrOutputParser()   # ② 조금만 다양하게 0.3

print(chain.invoke({"to": "팀장님", "content": "내일 오전 병원 진료 때문에 11시에 출근하겠다"}))   # ③
