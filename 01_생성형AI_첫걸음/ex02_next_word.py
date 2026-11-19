# ex02_next_word.py : 생성형 AI 의 원리 — "다음에 올 낱말 맞히기" 를 아주 작게 흉내 내기
# ── 전체 흐름 ──────────────────────────────────────────────
# ① 배울 문장 준비 → ② 낱말마다 "다음에 나온 낱말" 을 적어 두기(배우기)
# → ③ "나는" 에서 시작해 적어 둔 것 중 하나씩 뽑아 이어 붙이기(만들기)
# 진짜 AI 도 이것처럼 "다음 낱말" 을 하나씩 골라 글을 만들어요 (훨씬 많이 배울 뿐)
# ────────────────────────────────────────────────────────
import random                         # 무작위로 하나 뽑을 때 쓰는 도구

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
for sentence in sentences:            # 문장을 하나씩 꺼내서
    words = sentence.split()          # 문장을 빈칸으로 잘라 낱말 목록으로
    for i in range(len(words) - 1):   # 마지막 낱말 앞까지 하나씩
        now = words[i]                # 지금 낱말
        after = words[i + 1]          # 바로 다음 낱말
        if now not in next_words:     # 처음 보는 낱말이면
            next_words[now] = []      # 빈 목록부터 만들고
        next_words[now].append(after) # 다음 낱말을 목록에 추가

print("'나는' 다음에 나온 낱말:", next_words["나는"])   # 사과가 여러 번 → 뽑힐 확률이 높아요
print("'를' 다음에 나온 낱말:", next_words["를"])

# ③ 만들기: "나는" 에서 시작해 다음 낱말을 하나씩 골라 이어 붙여요
random.seed(3)                        # 실행할 때마다 같은 결과가 나오게 고정
for count in range(3):                # 문장을 3개 만들어 봐요
    word = "나는"                      # 시작 낱말
    sentence = word                   # 만들고 있는 문장
    while word in next_words:         # 다음 낱말을 알고 있는 동안 계속
        word = random.choice(next_words[word])   # 적어 둔 것 중 하나를 뽑기
        sentence = sentence + " " + word         # 뽑은 낱말을 문장 뒤에 붙이기
    print("만든 문장:", sentence)       # 더 이을 낱말이 없으면 문장 완성
