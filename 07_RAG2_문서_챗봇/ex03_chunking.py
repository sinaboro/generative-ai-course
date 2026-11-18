# ex03_chunking.py : 청킹 — 긴 쪽을 작은 조각(청크)으로 나누기
from langchain_text_splitters import RecursiveCharacterTextSplitter   # 글 나누기 도구

from doc_tools import load_pdf

docs = load_pdf("data/새싹전자_직원안내서.pdf")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,       # 조각 하나의 최대 글자 수
    chunk_overlap=50,     # 앞 조각과 겹치게 둘 글자 수 (문장이 잘려도 뜻이 이어지게)
)
chunks = splitter.split_documents(docs)        # 쪽 4개 → 조각 여러 개
print("쪽 수:", len(docs), "→ 조각 수:", len(chunks))

for i in range(3):                             # 앞의 조각 3개를 보여 줘요
    print("---- 조각", i + 1, chunks[i].metadata, len(chunks[i].page_content), "글자")
    print(chunks[i].page_content)
