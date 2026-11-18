# ex07_documents.py : Document — 글(page_content)과 꼬리표(metadata)를 함께 저장하기
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore

from common import get_embeddings
from faq_data import FAQ

docs = []
for line in FAQ:
    category, text = line.split(": ", 1)              # 첫 ": " 에서 한 번만 잘라 "환불" 과 "제품을 …" 으로
    doc = Document(page_content=text, metadata={"category": category})   # 글 + 꼬리표
    docs.append(doc)
print("첫 번째 문서:", docs[0])

store = InMemoryVectorStore.from_documents(docs, get_embeddings())
for doc in store.similarity_search("포장을 이미 뜯었는데 돌려보낼 수 있나요?", k=2):
    print("[" + doc.metadata["category"] + "]", doc.page_content)   # 꼬리표로 출처 보여 주기
