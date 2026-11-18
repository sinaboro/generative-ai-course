# ex02_pdf_documents.py : PDF 의 쪽마다 Document 로 만들기 — 쪽 번호를 꼬리표로
from doc_tools import load_pdf

docs = load_pdf("data/새싹전자_직원안내서.pdf")
print("Document 수:", len(docs))
for doc in docs:
    first_line = doc.page_content.split("\n")[1]       # 쪽 번호 줄 다음 줄 (보통 제목)
    print(doc.metadata, "|", len(doc.page_content), "글자 |", first_line)
