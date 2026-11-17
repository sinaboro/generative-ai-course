# 문제1 정답: ex01 의 학습 문장을 바꿔 "나는" 으로 시작하는 새 문장 만들기
import random
from collections import Counter, defaultdict

sentences = [
    "나는 아침 에 우유 를 마셔",
    "나는 점심 에 김밥 을 먹어",
    "나는 저녁 에 우유 를 마셔",
    "너는 아침 에 빵 을 먹어",
]
next_count = defaultdict(Counter)
for s in sentences:
    w = s.split()
    for a, b in zip(w, w[1:]):
        next_count[a][b] += 1

def generate(start, length=5, seed=0):
    random.seed(seed)
    words = [start]
    for _ in range(length):
        options = next_count[words[-1]]
        if not options:
            break
        words.append(random.choices(list(options), weights=list(options.values()))[0])
    return " ".join(words)

for seed in range(4):
    print(generate("나는", seed=seed))
