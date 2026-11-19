# step2_try_agent.py : [2단계] 웹을 만들기 전에 콘솔에서 도우미를 먼저 시험해요
# 흐름: 여러 종류의 질문(규정 · 날짜 · 예약 · 중복 예약 · 현황 · 모르는 것)을 차례로 보내고
#       답과 쓴 도구를 보며 에이전트가 도구를 제대로 골라 쓰는지 확인
from assistant import answer                  # 사내 도우미 함수

questions = [
    "출장 가서 2박 했는데 숙박비는 서울 기준으로 모두 얼마까지 돼?",   # 검색 + 계산
    "오늘 날짜가 며칠이야?",                                          # today
    "내일 오후 2시에 새싹룸 예약해 줘.",                               # today + book_room
    "같은 시간에 새싹룸 한 번 더 예약해 줘.",                          # 중복 → 막혀야 해요
    "내일 회의실 예약 현황 알려 줘.",                                  # list_bookings
    "회사 주차장은 몇 층이에요?",                                      # 안내서에 없음
]
for text in questions:
    reply, tools_used = answer("김민지", text)   # (답, 쓴 도구 목록) 두 개를 받아요
    print("🙋", text)
    print("🤖", reply)
    print("   🔧 쓴 도구:", tools_used)
