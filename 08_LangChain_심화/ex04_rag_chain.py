# ex04_rag_chain.py : LangChain 으로 작은 RAG — 자료에서 찾아 그 안에서만 답하기
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore

from common import get_embeddings, get_llm

# ① 자료: 가상의 "AI 서비스 개발 과정" 안내문 (실제로는 PDF · 웹 문서를 잘라서 넣어요, Part 07)
docs = [
    Document("수업은 평일 오전 9시 30분에 시작해서 오후 6시 30분에 끝나요.", metadata={"source": "시간표"}),
    Document("점심시간은 12시 30분부터 1시 30분까지예요.", metadata={"source": "시간표"}),
    Document("결석하면 당일 오전 9시까지 담임에게 메신저로 알려야 해요.", metadata={"source": "출결 규정"}),
    Document("최종 프로젝트 발표는 과정 마지막 주 금요일에 팀별로 15분씩 해요.", metadata={"source": "프로젝트 안내"}),
    Document("실습 PC 에는 개인 프로그램을 설치하지 말고, 필요하면 강사에게 먼저 물어봐요.", metadata={"source": "실습실 규칙"}),
]

# ② 자료를 벡터로 바꿔 저장소에 넣고, 질문과 가까운 자료 2개를 찾는 검색기 만들기
store = InMemoryVectorStore.from_documents(docs, get_embeddings())
retriever = store.as_retriever(search_kwargs={"k": 2})

prompt = ChatPromptTemplate.from_messages([
    ("system", "아래 [자료] 안의 내용으로만 답해. 자료에 없으면 '자료에 없어요' 라고 답해.\n[자료]\n{context}"),
    ("user", "{question}"),
])
chain = prompt | get_llm() | StrOutputParser()


def ask(question):
    found = retriever.invoke(question)                         # ③ 검색
    context = "\n".join(f"- {d.page_content}" for d in found)
    answer = chain.invoke({"context": context, "question": question})   # ④ 자료와 함께 질문
    sources = sorted({d.metadata["source"] for d in found})
    print(f"Q: {question}")
    print(f"A: {answer}")
    print(f"   (참고한 자료: {', '.join(sources)})")


ask("아파서 못 가면 어떻게 해야 해?")
ask("발표는 언제 해요?")
ask("수강료는 얼마예요?")
