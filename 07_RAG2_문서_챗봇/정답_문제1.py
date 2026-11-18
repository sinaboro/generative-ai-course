# 정답_문제1.py : 조각 크기(chunk_size)를 바꾸면 점수와 AI 에게 보내는 글자 수가 어떻게 달라질까?
from langchain_core.vectorstores import InMemoryVectorStore

from common import get_embeddings
from doc_tools import ask, load_pdf, make_context, split_docs

docs = load_pdf("data/새싹전자_직원안내서.pdf")
tests = [
    ["연차는 1년에 며칠 받아?", "15"],
    ["출장 가서 밥값은 하루에 얼마까지 돼?", "3만"],
    ["재택근무는 일주일에 몇 번 할 수 있어?", "2"],
    ["월요일에 재택근무해도 돼?", "없"],
    ["컴퓨터 비밀번호는 얼마마다 바꿔야 해?", "90"],
    ["8시 30분에 출근하면 몇 시에 퇴근해?", "5시 30분"],
    ["출장비 정산을 7일 넘겨서 내면 어떻게 돼?", "받을 수 없"],
    ["회사 주차장은 몇 층에 있어?", "안내서에 없는"],
]

for size in [30, 300, 1000]:
    chunks = split_docs(docs, chunk_size=size, chunk_overlap=size // 5)   # 겹침은 크기의 5분의 1
    store = InMemoryVectorStore.from_documents(chunks, get_embeddings())
    passed = 0
    sent = 0                                  # AI 에게 보낸 자료 글자 수 합계 (많을수록 요금도 늘어요)
    for question, must_have in tests:
        answer, pages = ask(store, question, k=2)
        found = store.similarity_search(question, k=2)   # ask 가 AI 에게 건넨 것과 같은 조각 2개
        sent = sent + len(make_context(found))           # 그 자료의 글자 수를 더해요
        if must_have in answer:
            passed = passed + 1
    print("chunk_size", size, "| 조각", len(chunks), "개 | 점수", passed, "/", len(tests), "| 보낸 글자", sent)
