# ex07_compare_models.py : 모델 이름만 바꿔 여러 회사의 AI 비교하기
# 흐름: 모델 이름 목록을 돌면서 → 같은 질문을 보내고 → 걸린 시간과 답을 나란히 출력
import time                                     # 시간 재기 도구

from common import get_llm                      # AI 를 만드는 함수

models = ["openai/gpt-4o-mini", "anthropic/claude-haiku-5.5", "google/gemini-3.5-flash-lite"]
question = "AI 가 사람의 일자리를 모두 대신할까? 한 문장으로 의견을 말해 줘."

for model_name in models:                       # 모델을 하나씩
    llm = get_llm(temperature=0, model=model_name)   # 이름만 바꿔서 AI 만들기
    start = time.time()                         # 시작 시각
    answer = llm.invoke(question)               # 같은 질문 보내기
    seconds = round(time.time() - start, 1)     # 걸린 시간 (초, 소수 1자리)
    print(model_name, "(", seconds, "초 )")
    print("   ", answer.content)
