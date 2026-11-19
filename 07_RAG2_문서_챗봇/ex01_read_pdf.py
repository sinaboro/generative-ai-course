# ex01_read_pdf.py : PDF 파일에서 쪽마다 글자 꺼내기
# 흐름: ① PDF 열기 → ② 전체 쪽수 보기 → ③ 한 쪽의 글자를 꺼내 길이와 앞부분 보기
from pypdf import PdfReader                   # PDF 를 읽는 라이브러리

reader = PdfReader("data/새싹전자_직원안내서.pdf")   # ① PDF 열기 (이 폴더에서 실행해요)
print("전체 쪽수:", len(reader.pages))        # ② reader.pages = 쪽 목록

text = reader.pages[1].extract_text()         # ③ 두 번째 쪽(번호는 0부터 세요)의 글자
print("2쪽 글자 수:", len(text))
print(text[:200])                             # 앞에서 200글자만
