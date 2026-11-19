# 정답_문제2.py : 학교 도서관 안내문으로 만드는 RAG
# 흐름: ex08 과 같아요 — ① 안내문 저장 · 검색기 → ② 규칙 틀 + 체인 → ③ 질문마다 검색 → 자료 이어 붙이기 → 답
from langchain_core.output_parsers import StrOutputParser      # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate          # 질문 틀
from langchain_core.vectorstores import InMemoryVectorStore    # 벡터 저장소

from common import get_embeddings, get_llm            # 임베딩 모델 · AI

LIBRARY = [                                           # 도서관 안내문 (자료)
    "운영 시간: 도서관은 평일 오전 9시부터 오후 8시까지, 토요일은 오후 1시까지 열어요.",
    "대출: 한 사람이 책을 5권까지 14일 동안 빌릴 수 있어요.",
    "연장: 반납일 전에 한 번, 7일 더 빌릴 수 있어요.",
    "연체: 늦게 반납하면 늦은 날만큼 대출이 정지돼요.",
    "열람실: 2층 열람실은 시험 기간에 밤 10시까지 열어요.",
    "분실: 책을 잃어버리면 같은 책으로 사 오거나 책값을 내야 해요.",
]
store = InMemoryVectorStore.from_texts(LIBRARY, get_embeddings())   # ① 안내문을 숫자로 바꿔 저장
retriever = store.as_retriever(search_kwargs={"k": 2})             # 비슷한 2개를 찾는 검색기

# ② 너무 엄격하면 "토요일 저녁" 처럼 추론할 수 있는 것도 "없다" 고 해서, 근거와 함께 답하게 했어요
template = ChatPromptTemplate.from_template("""너는 학교 도서관 안내 도우미야. [자료] 에 있는 내용으로만 짧게 답해.
자료로 알 수 있는 내용이면(예: 운영 시간으로 열었는지 닫았는지) 그 근거와 함께 답해.
자료로 전혀 알 수 없으면 "도서관 안내 자료에 없는 내용이에요." 라고만 답해.

[자료]
{context}

[질문]
{question}""")
chain = template | get_llm(temperature=0) | StrOutputParser()

for question in ["책 몇 권까지 빌릴 수 있어?", "토요일 저녁에 가도 돼?", "도서관에서 음식 먹어도 돼?"]:
    context = ""                                      # ③ 찾은 자료를 이어 붙일 글
    for doc in retriever.invoke(question):            # 검색 → Document 2개
        context = context + "- " + doc.page_content + "\n"
    print("질문:", question)
    print("답:", chain.invoke({"context": context, "question": question}))
