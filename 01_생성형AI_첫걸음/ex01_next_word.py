# ex01_next_word.py : 아주 작은 "다음 단어 맞히기" 모델 — 생성형 AI 의 원리를 손으로 만들어 보기
# 생성형 AI 는 "지금까지의 글 다음에 올 단어" 를 맞히는 일을 수없이 반복해서 글을 만들어요
import random
from collections import Counter, defaultdict

# 학습 데이터: 아주 짧은 문장 몇 개 (진짜 LLM 은 인터넷 글 수천억 단어로 배워요)
sentences = [
    "나는 사과 를 좋아해",
    "나는 바나나 를 좋아해",
    "나는 사과 를 먹었어",
    "너는 사과 를 좋아해",
    "나는 학교 에 갔어",
]

# ① 학습: "이 단어 다음에 어떤 단어가 몇 번 왔나" 를 세어 둬요
next_count = defaultdict(Counter)
for s in sentences:
    words = s.split()
    for a, b in zip(words, words[1:]):       # 붙어 있는 두 단어씩 짝 짓기
        next_count[a][b] += 1

print("'나는' 다음에 온 단어:", dict(next_count["나는"]))
print("'를' 다음에 온 단어:", dict(next_count["를"]))

# ② 생성: 첫 단어에서 시작해 "다음 단어 고르기" 를 반복해요
def generate(start, length=4, seed=0):
    random.seed(seed)
    words = [start]
    for _ in range(length):
        options = next_count[words[-1]]
        if not options:                      # 다음 단어를 모르면 멈춰요
            break
        # 많이 나온 단어일수록 뽑힐 가능성이 커요 (횟수 = 뽑기 표 개수)
        nxt = random.choices(list(options), weights=list(options.values()))[0]
        words.append(nxt)
    return " ".join(words)

for seed in range(3):
    print(f"생성 {seed + 1}:", generate("나는", seed=seed))
print("생성 4:", generate("너는", seed=7))
