# ex04_similarity.py : 뜻이 비슷한 문장은 숫자도 비슷해요 — 코사인 유사도 비교
from common import get_embeddings, similarity

embeddings = get_embeddings()
base = "강아지가 공원에서 뛰어놀아요."                 # 기준 문장
others = [
    "개가 잔디밭에서 신나게 달려요.",                  # 낱말은 다르지만 뜻이 비슷
    "고양이가 소파에서 잠을 자요.",                    # 동물 이야기지만 하는 일이 다름
    "오늘 주식 시장이 크게 떨어졌어요.",                # 전혀 다른 이야기
    "강아지 공원 뛰어놀아요 주식",                      # 낱말은 많이 겹치지만 문장이 엉망
]

base_vector = embeddings.embed_query(base)
print("기준:", base)
for sentence in others:
    score = similarity(base_vector, embeddings.embed_query(sentence))
    print(round(score, 3), sentence)
