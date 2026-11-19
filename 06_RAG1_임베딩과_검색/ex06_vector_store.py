# ex06_vector_store.py : 벡터 저장소 — 숫자로 바꾸기 · 저장 · 검색을 LangChain 이 한 번에
# 흐름: ① from_texts 로 안내문을 숫자로 바꿔 저장소에 넣기 (ex05 의 ① 을 대신해 줘요)
#       → ② similarity_search_with_score 로 질문과 비슷한 2개를 점수와 함께 찾기 (ex05 의 ②~④)
from langchain_core.vectorstores import InMemoryVectorStore   # 메모리에 두는 벡터 저장소

from common import get_embeddings                     # 임베딩 모델
from faq_data import FAQ                              # 안내문 목록

store = InMemoryVectorStore.from_texts(FAQ, get_embeddings())  # ① 글 목록을 숫자로 바꿔 저장

for query in ["돈을 돌려받고 싶어요", "고장 나면 공짜로 고쳐 주나요?"]:
    print("질문:", query)
    results = store.similarity_search_with_score(query, k=2)   # ② 가장 비슷한 2개 찾기
    for doc, score in results:                                 # (문서, 점수) 짝을 하나씩
        print("  ", round(score, 3), doc.page_content)         # page_content = 문서의 글
