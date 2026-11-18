# ex07_compare_models.py : 모델 이름만 바꿔 여러 회사의 AI 비교하기
import time

from common import get_llm

models = ["openai/gpt-4o-mini", "anthropic/claude-haiku-5.5", "google/gemini-3.5-flash-lite"]
question = "AI 가 사람의 일자리를 모두 대신할까? 한 문장으로 의견을 말해 줘."

for model_name in models:
    llm = get_llm(temperature=0, model=model_name)
    start = time.time()                         # 시작 시각
    answer = llm.invoke(question)
    seconds = round(time.time() - start, 1)     # 걸린 시간 (초)
    print(model_name, "(", seconds, "초 )")
    print("   ", answer.content)
