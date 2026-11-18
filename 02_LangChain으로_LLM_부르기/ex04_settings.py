# ex04_settings.py : max_tokens — 답의 최대 길이 정하기
from common import get_llm

short_llm = get_llm(max_tokens=20)            # 답을 20토큰까지만
answer = short_llm.invoke("한국의 사계절을 자세히 설명해 줘.")

print("답:", answer.content)
print("끝난 이유:", answer.response_metadata["finish_reason"])   # length = 길이 제한에 걸려 잘림
