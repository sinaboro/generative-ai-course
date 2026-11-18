# ex05_semantic_search.py : 뜻으로 찾는 "의미 검색" — 질문과 가장 비슷한 안내문 고르기
from common import get_embeddings, similarity
from faq_data import FAQ

embeddings = get_embeddings()
faq_vectors = embeddings.embed_documents(FAQ)         # ① 안내문 전부를 미리 숫자로 (한 번만)

for query in ["돈을 돌려받고 싶어요", "물건이 언제 와요?"]:
    query_vector = embeddings.embed_query(query)      # ② 질문도 숫자로
    results = []
    for i in range(len(FAQ)):                         # ③ 안내문마다 비슷한 정도 계산
        score = similarity(query_vector, faq_vectors[i])
        results.append([score, FAQ[i]])               # [점수, 문장] 을 모아요
    results.sort(reverse=True)                        # ④ 첫 칸(점수)이 큰 순서로 정렬

    print("질문:", query)
    for score, sentence in results[:2]:               # 위에서 2개만, [점수, 문장] 을 두 변수로
        print("  ", round(score, 3), sentence)
