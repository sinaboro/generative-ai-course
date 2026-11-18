# 정답_문제1.py : 이메일 작성 체인 — 역할(system) + 형식 + 길이
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from common import get_llm

template = ChatPromptTemplate.from_messages([
    ("system", "너는 신입사원의 이메일을 다듬어 주는 비서야. 공손하지만 짧게 써."),
    ("human", "{to}께 보낼 이메일을 써 줘. 내용: {content}. 형식: 제목 한 줄, 본문 3 ~ 4문장, 마지막에 이름 '홍길동'."),
])
chain = template | get_llm(temperature=0.3) | StrOutputParser()

print(chain.invoke({"to": "팀장님", "content": "내일 오전 병원 진료 때문에 11시에 출근하겠다"}))
