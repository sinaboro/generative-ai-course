# 정답_문제2.py : 텍스트(.txt) 문서로 만드는 도서관 안내 챗봇
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore

from common import get_embeddings, get_llm
from doc_tools import make_context, split_docs

# ① txt 파일 읽기 → Document 하나로 (txt 에는 쪽이 없어서 page 를 1 로 둬요)
with open("data/도서관_이용안내.txt", encoding="utf-8") as file:
    text = file.read()
docs = [Document(page_content=text, metadata={"source": "도서관_이용안내.txt", "page": 1})]

# ② 나누기 → ③ 저장소
chunks = split_docs(docs, chunk_size=200, chunk_overlap=40)
store = InMemoryVectorStore.from_documents(chunks, get_embeddings())
print("조각 수:", len(chunks))

# ④ 도서관에 맞는 프롬프트 (doc_tools 의 RAG_TEMPLATE 은 새싹전자용이라 새로 만들어요)
template = ChatPromptTemplate.from_template("""너는 새싹 도서관 안내 도우미야. [자료] 에 있는 내용으로만 짧게 답해.
자료로 알 수 있는 내용이면(예: 쉬는 날이라 갈 수 없음) 그 근거와 함께 답해.
자료로 전혀 알 수 없으면 "안내 자료에 없는 내용이에요. 1층 안내 데스크에 문의해 주세요." 라고만 답해.

[자료]
{context}

[질문]
{question}""")
chain = template | get_llm(temperature=0) | StrOutputParser()

for question in ["새 책은 며칠 빌릴 수 있어?", "월요일에 가도 돼?", "도서관에 주차할 수 있어?"]:
    found = store.similarity_search(question, k=2)
    print("질문:", question)
    print("답:", chain.invoke({"context": make_context(found), "question": question}))
