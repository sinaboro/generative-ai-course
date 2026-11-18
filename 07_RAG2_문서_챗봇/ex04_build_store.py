# ex04_build_store.py : 읽기 → 나누기 → 숫자로 바꿔 저장 — 한 번만 해 두면 돼요
from langchain_core.vectorstores import InMemoryVectorStore

from common import get_embeddings
from doc_tools import STORE_PATH, load_pdf, split_docs

docs = load_pdf("data/새싹전자_직원안내서.pdf")          # ① 읽기
chunks = split_docs(docs, chunk_size=300, chunk_overlap=50)   # ② 나누기
store = InMemoryVectorStore.from_documents(chunks, get_embeddings())   # ③ 숫자로 바꿔 저장소에
store.dump(STORE_PATH)                                   # ④ 파일로 저장 (다음부터는 불러오기만)
print("조각", len(chunks), "개를 저장했어요 →", STORE_PATH)

for doc in store.similarity_search("연차는 며칠이야?", k=2):   # 잘 찾는지 시험
    print("[" + str(doc.metadata["page"]) + "쪽]", doc.page_content[:60], "...")
