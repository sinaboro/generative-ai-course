# ex07_documents.py : Document — 글(page_content)과 꼬리표(metadata)를 함께 저장하기
# 흐름: ① "환불: …" 을 꼬리표("환불")와 글로 나눠 Document 로 만들기 → ② 저장소에 넣기
#       → ③ 검색하면 문서와 함께 꼬리표도 나와서 "어느 안내문에서 왔는지" 보여 줄 수 있어요
from langchain_core.documents import Document                  # 글 + 꼬리표 묶음
from langchain_core.vectorstores import InMemoryVectorStore    # 벡터 저장소

from common import get_embeddings                     # 임베딩 모델
from faq_data import FAQ                              # 안내문 목록

docs = []                                             # Document 를 모을 목록
for line in FAQ:
    category, text = line.split(": ", 1)              # 첫 ": " 에서 한 번만 잘라 "환불" 과 "제품을 …" 으로
    doc = Document(page_content=text, metadata={"category": category})   # ① 글 + 꼬리표
    docs.append(doc)
print("첫 번째 문서:", docs[0])

store = InMemoryVectorStore.from_documents(docs, get_embeddings())   # ② Document 목록을 저장
for doc in store.similarity_search("포장을 이미 뜯었는데 돌려보낼 수 있나요?", k=2):   # ③ 검색
    print("[" + doc.metadata["category"] + "]", doc.page_content)   # 꼬리표로 출처 보여 주기
