# step1_build_index.py : [1단계] 직원 안내서 PDF → 조각 → 벡터 저장소 파일 (Part 07)
# 안내서 PDF 를 바꾸면 이 파일을 다시 실행해요
import os

from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader

from common import get_embeddings

PDF_PATH = "data/새싹전자_직원안내서.pdf"
STORE_PATH = "data/handbook_store.json"

# ① 읽기: 쪽마다 Document (꼬리표에 쪽 번호)
docs = []
page_number = 0
for page in PdfReader(PDF_PATH).pages:
    page_number = page_number + 1
    docs.append(Document(page_content=page.extract_text(),
                         metadata={"source": os.path.basename(PDF_PATH), "page": page_number}))

# ② 나누기: Part 07 품질 점검에서 가장 좋았던 300 글자 / 겹침 50
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# ③ 저장소 만들기 → ④ 파일로 저장
store = InMemoryVectorStore.from_documents(chunks, get_embeddings())
store.dump(STORE_PATH)
print("쪽", len(docs), "개 → 조각", len(chunks), "개 → 저장:", STORE_PATH)
