# ex08_first_rag.py : 첫 RAG — ① 검색 → ② 찾은 자료를 프롬프트에 넣기 → ③ AI 가 답하기
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore

from common import get_embeddings, get_llm
from faq_data import FAQ

store = InMemoryVectorStore.from_texts(FAQ, get_embeddings())
retriever = store.as_retriever(search_kwargs={"k": 2})        # 검색기: 질문을 넣으면 문서 2개를 찾아 줘요

template = ChatPromptTemplate.from_template("""너는 새싹전자 고객센터 상담원이야.
아래 [자료] 에 있는 내용으로만 짧게 답해.
자료에 없는 내용이면 "죄송하지만 그 내용은 안내 자료에 없어요." 라고만 답해.

[자료]
{context}

[질문]
{question}""")
chain = template | get_llm(temperature=0) | StrOutputParser()


def ask(question):
    found = retriever.invoke(question)                # ① 검색
    context = ""
    for doc in found:                                 # ② 찾은 문서를 한 덩어리 글로
        context = context + "- " + doc.page_content + "\n"
    return chain.invoke({"context": context, "question": question})   # ③ 답하기


for question in ["돈 돌려받으려면 언제까지 신청해야 해?", "2만 원어치 사면 배송비 있어?", "매장은 어디에 있어?"]:
    print("질문:", question)
    print("답:", ask(question))
