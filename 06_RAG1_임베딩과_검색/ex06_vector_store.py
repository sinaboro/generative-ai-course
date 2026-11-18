# ex06_vector_store.py : 벡터 저장소 — 숫자로 바꾸기 · 저장 · 검색을 LangChain 이 한 번에
from langchain_core.vectorstores import InMemoryVectorStore   # 메모리에 두는 벡터 저장소

from common import get_embeddings
from faq_data import FAQ

store = InMemoryVectorStore.from_texts(FAQ, get_embeddings())  # 글 목록을 숫자로 바꿔 저장

for query in ["돈을 돌려받고 싶어요", "고장 나면 공짜로 고쳐 주나요?"]:
    print("질문:", query)
    results = store.similarity_search_with_score(query, k=2)   # 가장 비슷한 2개 찾기
    for doc, score in results:                                 # (문서, 점수) 짝을 하나씩
        print("  ", round(score, 3), doc.page_content)
