# ex03_chunking.py : 청킹 — 긴 쪽을 작은 조각(청크)으로 나누기
# 흐름: ① PDF → 쪽 Document → ② 300글자 안팎, 50글자씩 겹치게 자르기 → ③ 조각 수와 앞 조각 3개 보기
# 왜 나눌까? 한 쪽 통째로 찾으면 질문과 상관없는 글까지 AI 에게 보내게 돼요 (정확도 ↓, 요금 ↑)
from langchain_text_splitters import RecursiveCharacterTextSplitter   # 글 나누기 도구

from doc_tools import load_pdf                 # PDF → Document 목록

docs = load_pdf("data/새싹전자_직원안내서.pdf")  # ① 쪽 4개
splitter = RecursiveCharacterTextSplitter(     # ② 문단 → 줄 → 빈칸 순서로 자연스러운 곳에서 잘라요
    chunk_size=300,       # 조각 하나의 최대 글자 수
    chunk_overlap=50,     # 앞 조각과 겹치게 둘 글자 수 (문장이 잘려도 뜻이 이어지게)
)
chunks = splitter.split_documents(docs)        # 쪽 4개 → 조각 여러 개
print("쪽 수:", len(docs), "→ 조각 수:", len(chunks))

for i in range(3):                             # ③ 앞의 조각 3개를 보여 줘요
    print("---- 조각", i + 1, chunks[i].metadata, len(chunks[i].page_content), "글자")
    print(chunks[i].page_content)
