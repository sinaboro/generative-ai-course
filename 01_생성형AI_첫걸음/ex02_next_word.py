# ex02_next_word.py : 생성형 AI 의 원리 — "다음에 올 낱말 맞히기" 를 아주 작게 흉내 내기
import random

# ① 배울 문장들 (진짜 AI 는 인터넷 글 수천억 낱말을 배워요)
sentences = [
    "나는 사과 를 좋아해",
    "나는 바나나 를 좋아해",
    "나는 사과 를 먹었어",
    "너는 사과 를 좋아해",
    "나는 학교 에 갔어",
]

# ② 배우기: 낱말마다 "바로 다음에 나온 낱말" 을 모두 적어 둬요
next_words = {}                       # 예: {"나는": ["사과", "바나나", ...]}
for sentence in sentences:
    words = sentence.split()          # 문장을 빈칸으로 잘라 낱말 목록으로
    for i in range(len(words) - 1):   # 마지막 낱말 앞까지 하나씩
        now = words[i]                # 지금 낱말
        after = words[i + 1]          # 바로 다음 낱말
        if now not in next_words:
            next_words[now] = []
        next_words[now].append(after)

print("'나는' 다음에 나온 낱말:", next_words["나는"])
print("'를' 다음에 나온 낱말:", next_words["를"])

# ③ 만들기: "나는" 에서 시작해 다음 낱말을 하나씩 골라 이어 붙여요
random.seed(3)                        # 실행할 때마다 같은 결과가 나오게 고정
for count in range(3):                # 문장을 3개 만들어 봐요
    word = "나는"
    sentence = word
    while word in next_words:         # 다음 낱말을 알고 있는 동안 계속
        word = random.choice(next_words[word])   # 적어 둔 것 중 하나를 뽑기
        sentence = sentence + " " + word
    print("만든 문장:", sentence)
