# ex04_chain.py : 체인 — 템플릿 | AI | 글자 꺼내기 를 파이프(|)로 잇기
# ── 전체 흐름 ──────────────────────────────────────────────
# {"topic": "토큰"} → [템플릿: 빈칸 채우기] → [AI: 답하기] → [StrOutputParser: 글자만 꺼내기] → "토큰은 …"
# 체인을 한 번 만들어 두면 invoke 한 번으로 세 단계가 차례로 실행돼요
# ────────────────────────────────────────────────────────
from langchain_core.output_parsers import StrOutputParser   # 답 묶음에서 글자만 꺼내는 도구
from langchain_core.prompts import ChatPromptTemplate       # 질문 틀 도구

from common import get_llm                    # AI 를 만드는 함수

template = ChatPromptTemplate.from_template("{topic} 을(를) 초보자에게 한 문장으로 설명해 줘.")
chain = template | get_llm(temperature=0) | StrOutputParser()   # 왼쪽 결과가 오른쪽으로 흘러가요

topics = ["토큰", "프롬프트", "환각"]          # 설명받을 낱말들
for topic in topics:
    answer = chain.invoke({"topic": topic})     # 빈칸 값만 넣으면 끝까지 한 번에
    print(topic, ":", answer)                   # answer 는 이미 글자예요 (.content 필요 없음)
