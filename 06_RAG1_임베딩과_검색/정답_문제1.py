# 정답_문제1.py : 질문과 비슷한 순서대로 문장 줄 세우기
# 흐름: ① 질문 · 문장들을 숫자로 → ② 문장마다 [점수, 문장] 모으기 → ③ 점수 큰 순 정렬 → ④ 등수 매겨 출력
from common import get_embeddings, similarity          # 임베딩 모델 · 유사도 계산

embeddings = get_embeddings()
query = "배고파서 뭐 좀 먹고 싶어"
sentences = [
    "근처에 맛있는 국밥집이 있어요.",
    "내일 비가 온대요.",
    "냉장고에 김밥이 남아 있어요.",
    "파이썬 공부는 재미있어요.",
    "점심시간이 다가와요.",
]

query_vector = embeddings.embed_query(query)            # ① 질문 → 숫자
sentence_vectors = embeddings.embed_documents(sentences)   # 문장 여러 개 → 숫자 목록 여러 개
results = []
for i in range(len(sentences)):                         # ② 문장마다
    score = similarity(query_vector, sentence_vectors[i])
    results.append([score, sentences[i]])       # [점수, 문장]
results.sort(reverse=True)                      # ③ 점수가 큰 순서로

print("질문:", query)
rank = 0                                        # 등수
for score, sentence in results:                 # ④ 위에서부터 차례로
    rank = rank + 1
    print(rank, "등", round(score, 3), sentence)
