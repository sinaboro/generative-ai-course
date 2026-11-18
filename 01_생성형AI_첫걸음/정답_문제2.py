# 정답_문제2.py : ex02 의 문장을 내 문장으로 바꿔 새 문장 만들기
import random

sentences = [
    "나는 아침 에 우유 를 마셔",
    "나는 점심 에 김밥 을 먹어",
    "너는 저녁 에 우유 를 마셔",
]
next_words = {}
for sentence in sentences:
    words = sentence.split()
    for i in range(len(words) - 1):
        now = words[i]                    # 지금 낱말
        after = words[i + 1]              # 바로 다음 낱말
        if now not in next_words:
            next_words[now] = []
        next_words[now].append(after)

random.seed(5)
for count in range(3):
    word = "나는"
    sentence = word
    while word in next_words:
        word = random.choice(next_words[word])
        sentence = sentence + " " + word
    print(sentence)
