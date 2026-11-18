# 정답_문제1.py : 질문과 비슷한 순서대로 문장 줄 세우기
from common import get_embeddings, similarity

embeddings = get_embeddings()
query = "배고파서 뭐 좀 먹고 싶어"
sentences = [
    "근처에 맛있는 국밥집이 있어요.",
    "내일 비가 온대요.",
    "냉장고에 김밥이 남아 있어요.",
    "파이썬 공부는 재미있어요.",
    "점심시간이 다가와요.",
]

query_vector = embeddings.embed_query(query)
sentence_vectors = embeddings.embed_documents(sentences)
results = []
for i in range(len(sentences)):
    score = similarity(query_vector, sentence_vectors[i])
    results.append([score, sentences[i]])       # [점수, 문장]
results.sort(reverse=True)                      # 점수가 큰 순서로

print("질문:", query)
rank = 0
for score, sentence in results:
    rank = rank + 1
    print(rank, "등", round(score, 3), sentence)
