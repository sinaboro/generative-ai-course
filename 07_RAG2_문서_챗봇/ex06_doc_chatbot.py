# ex06_doc_chatbot.py : 직원 안내서 챗봇 — 무엇이든 물어보세요
from doc_tools import ask, load_store

store = load_store()
print("새싹전자 안내서 챗봇이에요. 끝내려면 '끝' 을 입력하세요.")
while True:
    question = input("질문: ")
    if question == "끝":
        break
    answer, pages = ask(store, question)                 # 답과 검색한 쪽 목록
    print("답:", answer)
    print("   (찾아본 쪽:", ", ".join(pages) + ")")      # ["2쪽", "3쪽"] → "2쪽, 3쪽"
