# ex01_read_pdf.py : PDF 파일에서 쪽마다 글자 꺼내기
from pypdf import PdfReader                   # PDF 를 읽는 라이브러리

reader = PdfReader("data/새싹전자_직원안내서.pdf")
print("전체 쪽수:", len(reader.pages))

text = reader.pages[1].extract_text()         # 두 번째 쪽(번호는 0부터 세요)의 글자
print("2쪽 글자 수:", len(text))
print(text[:200])                             # 앞에서 200글자만
