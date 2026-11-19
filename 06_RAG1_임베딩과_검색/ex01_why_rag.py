# ex01_why_rag.py : AI 가 모르는 우리 회사 정보 — 자료를 건네주면 답할 수 있어요
# 흐름: ① 회사 규정을 그냥 물어보기 (모르거나 지어내요) → ② 규정 자료를 질문에 붙여 다시 묻기 (정확히 답해요)
#       → 이 "자료를 찾아 붙여 주기" 를 자동으로 하는 것이 RAG 예요
from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0)
question = "새싹전자 제품은 산 지 며칠 안에 환불할 수 있어?"
print("① 그냥 물어보기:", llm.invoke(question).content)        # 가상의 회사라 AI 는 몰라요

note = "새싹전자 환불 규정: 제품을 산 날부터 14일 안에, 포장을 뜯지 않았다면 환불할 수 있어요."
print("② 자료와 함께:", llm.invoke("다음 자료를 보고 답해.\n자료: " + note + "\n질문: " + question).content)
