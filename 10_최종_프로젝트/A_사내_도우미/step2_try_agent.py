# step2_try_agent.py : [2단계] 웹을 만들기 전에 콘솔에서 도우미를 먼저 시험해요
from assistant import answer

questions = [
    "출장 가서 2박 했는데 숙박비는 서울 기준으로 모두 얼마까지 돼?",
    "오늘 날짜가 며칠이야?",
    "내일 오후 2시에 새싹룸 예약해 줘.",
    "같은 시간에 새싹룸 한 번 더 예약해 줘.",
    "내일 회의실 예약 현황 알려 줘.",
    "회사 주차장은 몇 층이에요?",
]
for text in questions:
    reply, tools_used = answer("김민지", text)
    print("🙋", text)
    print("🤖", reply)
    print("   🔧 쓴 도구:", tools_used)
