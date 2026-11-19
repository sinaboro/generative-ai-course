# ex05_semantic_search.py : 뜻으로 찾는 "의미 검색" — 질문과 가장 비슷한 안내문 고르기
# ── 전체 흐름 ──────────────────────────────────────────────
# ① 안내문 전부를 미리 숫자로 바꿔 두기 (한 번만)
# ② 질문이 오면 질문도 숫자로 → ③ 안내문마다 [비슷한 점수, 문장] 을 모으기
# ④ 점수 큰 순으로 정렬해 위에서 2개 보여 주기 → "돈을 돌려받고 싶어요" 로도 환불 안내를 찾아요
# ────────────────────────────────────────────────────────
from common import get_embeddings, similarity          # 임베딩 모델 · 유사도 계산
from faq_data import FAQ                              # 고객센터 안내문 목록

embeddings = get_embeddings()
faq_vectors = embeddings.embed_documents(FAQ)         # ① 안내문 전부를 미리 숫자로 (한 번만)

for query in ["돈을 돌려받고 싶어요", "물건이 언제 와요?"]:
    query_vector = embeddings.embed_query(query)      # ② 질문도 숫자로
    results = []
    for i in range(len(FAQ)):                         # ③ 안내문마다 비슷한 정도 계산
        score = similarity(query_vector, faq_vectors[i])   # i 번째 안내문과 질문의 점수
        results.append([score, FAQ[i]])               # [점수, 문장] 을 모아요
    results.sort(reverse=True)                        # ④ 첫 칸(점수)이 큰 순서로 정렬

    print("질문:", query)
    for score, sentence in results[:2]:               # 위에서 2개만, [점수, 문장] 을 두 변수로
        print("  ", round(score, 3), sentence)
