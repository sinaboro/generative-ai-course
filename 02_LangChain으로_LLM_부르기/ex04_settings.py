# ex04_settings.py : max_tokens — 답의 최대 길이 정하기
# 흐름: 답을 20토큰까지만 받는 AI 를 만들고 → 긴 답이 필요한 질문을 보내 → 잘린 답과 끝난 이유 보기
from common import get_llm                    # AI 를 만드는 함수

short_llm = get_llm(max_tokens=20)            # 답을 20토큰까지만
answer = short_llm.invoke("한국의 사계절을 자세히 설명해 줘.")   # 길게 답해야 하는 질문

print("답:", answer.content)                  # 중간에 잘린 답
print("끝난 이유:", answer.response_metadata["finish_reason"])   # length = 길이 제한에 걸려 잘림
