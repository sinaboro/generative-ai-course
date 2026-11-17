# ex04_parameters.py : temperature(다양함) 와 max_tokens(최대 길이) 바꿔 보기
from llm import client, MODEL

prompt = "새로 연 동네 빵집 이름을 하나만 지어 줘. 이름만 써."
for t in [0.0, 1.3]:
    names = []
    for _ in range(3):                                   # 같은 질문을 3번씩
        r = client().chat.completions.create(
            model=MODEL, messages=[{"role": "user", "content": prompt}], temperature=t, max_tokens=30)
        names.append(r.choices[0].message.content.strip())
    print(f"temperature {t}: {names}")

# max_tokens 를 아주 작게 하면 답이 중간에 잘려요
r = client().chat.completions.create(
    model=MODEL, messages=[{"role": "user", "content": "한국의 사계절을 자세히 설명해 줘."}], max_tokens=20)
print("max_tokens=20 →", r.choices[0].message.content)
print("끝난 이유:", r.choices[0].finish_reason)        # length = 길이 제한에 걸려 잘림
