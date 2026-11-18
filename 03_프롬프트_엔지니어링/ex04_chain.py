# ex04_chain.py : 체인 — 템플릿 | AI | 글자 꺼내기 를 파이프(|)로 잇기
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from common import get_llm

template = ChatPromptTemplate.from_template("{topic} 을(를) 초보자에게 한 문장으로 설명해 줘.")
chain = template | get_llm(temperature=0) | StrOutputParser()   # 왼쪽 결과가 오른쪽으로 흘러가요

topics = ["토큰", "프롬프트", "환각"]
for topic in topics:
    answer = chain.invoke({"topic": topic})     # 빈칸 값만 넣으면 끝까지 한 번에
    print(topic, ":", answer)
