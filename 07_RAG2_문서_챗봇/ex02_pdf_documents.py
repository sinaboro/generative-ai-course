# ex02_pdf_documents.py : PDF 의 쪽마다 Document 로 만들기 — 쪽 번호를 꼬리표로
# 흐름: load_pdf(doc_tools.py) 로 쪽마다 Document 만들기 → 각 Document 의 꼬리표 · 글자 수 · 제목 줄 보기
from doc_tools import load_pdf                   # PDF → Document 목록 함수

docs = load_pdf("data/새싹전자_직원안내서.pdf")
print("Document 수:", len(docs))                 # 쪽 수와 같아요
for doc in docs:
    lines = doc.page_content.split("\n")             # 그 쪽의 글을 줄 목록으로
    title_line = lines[1]                            # 0번 줄은 쪽 번호(- 1 -), 1번 줄이 제목
    print(doc.metadata, "|", len(doc.page_content), "글자 |", title_line)
