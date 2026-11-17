# ex03_temperature.py : temperature(온도) — 답을 "늘 같게" 할지 "다양하게" 할지 정하는 손잡이
# 진짜 LLM 이 다음 단어를 고르는 모습을 흉내 내요 (계산은 외우지 않아도 돼요)
import random
from collections import Counter

# "오늘 점심은 ___" 다음 단어 후보와 모델이 매긴 점수(클수록 그럴듯함)
candidates = {"김밥": 50, "라면": 30, "비빔밥": 15, "우주선": 5}

def pick(temperature, times=100, seed=1):
    """temperature 로 점수 차이를 키우거나 줄인 뒤, times 번 뽑아 결과를 세어요."""
    random.seed(seed)
    # 온도가 낮으면 점수 차이가 더 커지고(1등만 나옴), 높으면 차이가 줄어요(골고루 나옴)
    weights = [score ** (1 / temperature) for score in candidates.values()]
    picks = random.choices(list(candidates), weights=weights, k=times)
    return Counter(picks)

for t in [0.2, 1.0, 2.0]:
    result = pick(t)
    print(f"temperature {t}: ", {w: result.get(w, 0) for w in candidates})
