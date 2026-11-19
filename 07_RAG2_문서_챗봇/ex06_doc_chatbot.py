# ex06_doc_chatbot.py : 직원 안내서 챗봇 — 무엇이든 물어보세요
# 흐름: 저장소 불러오기 → 반복: 질문 입력('끝' 이면 멈춤) → ask() 로 답 · 쪽 목록 받기 → 출력
from doc_tools import ask, load_store                    # 문서 챗봇 함수 · 저장소 불러오기

store = load_store()                                     # ex04 에서 만든 저장소
print("새싹전자 안내서 챗봇이에요. 끝내려면 '끝' 을 입력하세요.")
while True:                                              # '끝' 을 입력할 때까지
    question = input("질문: ")                           # 키보드로 질문 받기
    if question == "끝":
        break                                            # 반복 멈추기
    answer, pages = ask(store, question)                 # 답과 검색한 쪽 목록
    print("답:", answer)
    print("   (찾아본 쪽:", ", ".join(pages) + ")")      # ["2쪽", "3쪽"] → "2쪽, 3쪽"
