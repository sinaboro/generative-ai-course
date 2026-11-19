# ex05_rag_with_sources.py : 출처(쪽 번호)를 밝히며 답하는 문서 RAG
# 흐름: 저장소 불러오기 → ① 비슷한 조각 3개 찾기 → ② [쪽] 을 붙여 자료 글 만들기 (AI 에게 건넬 것을 먼저 출력)
#       → ③ 자료 + 질문으로 답하기 (답 끝에 "(출처: N쪽)" 이 붙어요)
from langchain_core.output_parsers import StrOutputParser   # 글자만 꺼내기

from common import get_llm                               # AI 를 만드는 함수
from doc_tools import RAG_TEMPLATE, load_store, make_context   # 규칙 틀 · 저장소 불러오기 · 자료 만들기

store = load_store()                                     # ex04 가 만든 저장소 불러오기
chain = RAG_TEMPLATE | get_llm(temperature=0) | StrOutputParser()   # 틀 → AI → 글자

question = "출장 갔다 와서 정산은 언제까지 해야 해?"
found = store.similarity_search(question, k=3)           # ① 비슷한 조각 3개 찾기
context = make_context(found)                            # ② [쪽] 을 붙여 자료 만들기
print("===== AI 에게 건넨 자료 =====")
print(context)
print("===== 답 =====")
print(chain.invoke({"context": context, "question": question}))   # ③ 답하기
