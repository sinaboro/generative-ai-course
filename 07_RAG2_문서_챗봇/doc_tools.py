# doc_tools.py : 이 Part 의 예제가 함께 쓰는 도구 모음
# (각 함수는 ex02 ~ ex05 에서 한 단계씩 배운 코드를 모아 둔 거예요)
# ── 문서 챗봇의 전체 흐름 ─────────────────────────────────────
# [준비 · 한 번만]  load_pdf(PDF → 쪽마다 Document) → split_docs(작은 조각으로)
#                   → 숫자로 바꿔 저장소에 넣고 파일로 저장 (ex04) → 다음부터는 load_store() 로 불러오기
# [질문마다]        ask(): 비슷한 조각 찾기 → make_context(자료 글 만들기) → AI 가 답 + page_list(출처 쪽)
# ────────────────────────────────────────────────────────
import os                                     # 파일이 있는지 확인 · 파일 이름 꺼내기
import sys                                    # 프로그램을 멈출 때 (sys.exit)

from langchain_core.documents import Document                  # 글 + 꼬리표 묶음
from langchain_core.output_parsers import StrOutputParser      # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate          # 질문 틀
from langchain_core.vectorstores import InMemoryVectorStore    # 벡터 저장소
from langchain_text_splitters import RecursiveCharacterTextSplitter   # 긴 글 나누기 도구
from pypdf import PdfReader                   # PDF 읽기 도구

from common import get_embeddings, get_llm    # 임베딩 모델 · AI

STORE_PATH = "data/vector_store.json"         # ex04 가 만들어 저장하는 벡터 저장소 파일


def load_pdf(path):
    """PDF 를 쪽마다 Document 로 만들어요. 꼬리표에 파일 이름과 쪽 번호(1부터)를 적어요. (ex02)"""
    reader = PdfReader(path)                  # PDF 열기
    docs = []                                 # 쪽마다 만든 Document 를 모을 목록
    page_number = 0                           # 쪽 번호 (1부터 세려고 0 에서 시작)
    for page in reader.pages:                 # 쪽을 하나씩
        page_number = page_number + 1
        doc = Document(page_content=page.extract_text(),                       # 그 쪽의 글자
                       metadata={"source": os.path.basename(path), "page": page_number})   # 꼬리표
        docs.append(doc)
    return docs


def split_docs(docs, chunk_size=300, chunk_overlap=50):
    """긴 글을 chunk_size 글자 안팎의 조각(청크)으로 나눠요. 꼬리표는 조각마다 그대로 따라가요. (ex03)"""
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)     # Document 목록 → 더 작은 Document 목록


def load_store():
    """ex04 에서 저장해 둔 벡터 저장소를 불러와요."""
    if not os.path.exists(STORE_PATH):        # 저장 파일이 없으면 안내하고 멈춰요
        sys.exit("먼저 ex04_build_store.py 를 실행해서 벡터 저장소를 만들어 주세요.")
    return InMemoryVectorStore.load(STORE_PATH, get_embeddings())   # 파일 → 저장소


def make_context(docs):
    """찾은 조각들을 [쪽 번호] 를 붙여 한 덩어리 글로 만들어요. (ex05)"""
    context = ""
    for doc in docs:                          # 예: "[2쪽] 연차는 1년에 15일 …"
        context = context + "[" + str(doc.metadata["page"]) + "쪽] " + doc.page_content + "\n\n"
    return context


def page_list(docs):
    """찾은 조각들의 쪽 번호를 겹치지 않게 모아요. 예: ["2쪽", "3쪽"]"""
    pages = []
    for doc in docs:
        label = str(doc.metadata["page"]) + "쪽"
        if label not in pages:                # 같은 쪽이 두 번 나와도 한 번만
            pages.append(label)
    return pages


# 문서 챗봇의 규칙: 자료로만 답하고 (출처: N쪽) 을 붙이기, 모르면 인사팀 안내
RAG_TEMPLATE = ChatPromptTemplate.from_template("""너는 새싹전자 직원의 질문에 답하는 안내 도우미야.
아래 [자료] 에 있는 내용으로만 답하고, 답 끝에 근거가 된 쪽을 (출처: N쪽) 처럼 적어.
자료로 알 수 없으면 "안내서에 없는 내용이에요. 인사팀(내선 200)에 문의해 주세요." 라고만 답해.

[자료]
{context}

[질문]
{question}""")


def ask(store, question, k=3):
    """문서 챗봇: 검색 → 자료 만들기 → 답하기. 답과 출처 쪽 목록을 함께 돌려줘요. (ex05)"""
    found = store.similarity_search(question, k=k)                          # ① 비슷한 조각 k 개
    chain = RAG_TEMPLATE | get_llm(temperature=0) | StrOutputParser()       # 틀 → AI → 글자
    answer = chain.invoke({"context": make_context(found), "question": question})   # ② 자료 + 질문 → 답
    return answer, page_list(found)                                         # ③ (답, 쪽 목록) 두 개를 돌려줘요
