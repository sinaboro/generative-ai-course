# ex07_compare_models.py : 같은 질문을 여러 회사 모델에 보내 비교하기 (OpenRouter 의 장점)
import time

from llm import client

models = ["openai/gpt-4o-mini", "anthropic/claude-haiku-5.5", "google/gemini-3.5-flash-lite"]
question = "AI 가 사람의 일자리를 모두 대신할까? 찬성 · 반대 의견을 한 문장씩만 말해 줘."

for m in models:
    start = time.time()
    r = client().chat.completions.create(
        model=m, messages=[{"role": "user", "content": question}], max_tokens=200, temperature=0)
    sec = time.time() - start
    print(f"=== {m}  ({sec:.1f}초, 출력 {r.usage.completion_tokens}토큰) ===")
    print(r.choices[0].message.content.strip())
    print()
