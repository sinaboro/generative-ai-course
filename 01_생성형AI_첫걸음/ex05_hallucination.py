# ex05_hallucination.py : 환각 — AI 가 그럴듯하게 지어내는 답 확인하기
# 흐름: 세상에 없는 소설을 물어보고 → AI 가 "모른다" 고 하는지, 지어내는지 보기
from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0.7)                # 보통 정도의 다양함

# 세상에 없는 소설이에요 (이 교안을 위해 지어낸 제목)
question = "소설 『달빛 자판기와 일곱 개의 우산』(2019)의 줄거리를 세 줄로 알려 줘."
answer = llm.invoke(question)                 # 질문 보내기
print("질문:", question)
print("답:", answer.content)                  # 없는 책인데도 줄거리를 지어내면 → 환각
