# 정답_문제2.py : ex02 의 문장을 내 문장으로 바꿔 새 문장 만들기
# 흐름: ex02 와 같아요 — ① 문장 준비 → ② 다음 낱말 적어 두기 → ③ 하나씩 뽑아 문장 만들기
import random                             # 무작위로 하나 뽑는 도구

sentences = [                             # ① 내가 바꾼 배울 문장들
    "나는 아침 에 우유 를 마셔",
    "나는 점심 에 김밥 을 먹어",
    "너는 저녁 에 우유 를 마셔",
]
next_words = {}                           # ② 낱말 → 다음에 나온 낱말 목록
for sentence in sentences:
    words = sentence.split()              # 빈칸으로 잘라 낱말 목록으로
    for i in range(len(words) - 1):       # 마지막 낱말 앞까지
        now = words[i]                    # 지금 낱말
        after = words[i + 1]              # 바로 다음 낱말
        if now not in next_words:         # 처음 보는 낱말이면 빈 목록부터
            next_words[now] = []
        next_words[now].append(after)     # 다음 낱말 적어 두기

random.seed(5)                            # 실행할 때마다 같은 결과가 나오게
for count in range(3):                    # ③ 문장 3개 만들기
    word = "나는"                          # 시작 낱말
    sentence = word
    while word in next_words:             # 다음 낱말을 아는 동안
        word = random.choice(next_words[word])   # 하나 뽑아서
        sentence = sentence + " " + word         # 이어 붙이기
    print(sentence)
