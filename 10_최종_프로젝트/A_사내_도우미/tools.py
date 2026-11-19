# tools.py : [2단계] 도우미가 쓸 도구들 — 안내서 검색 · 계산기 · 오늘 날짜 · 회의실 예약
# ── 들어 있는 도구 ─────────────────────────────────────────
# search_handbook(질문)  : 직원 안내서에서 비슷한 조각 3개를 [쪽] 과 함께 찾기 (step1 이 만든 저장소)
# calculator(식)         : 사칙연산
# today()                : 오늘 날짜와 요일
# list_bookings(날짜)    : 그날의 회의실 예약 현황
# book_room(날짜, 시각, 회의실, 이름) : 회의실 예약 (값 검사 → 중복 검사 → 파일에 한 줄 쓰기)
# 예약은 data/bookings.txt 에 "날짜|시각|회의실|이름" 한 줄씩 저장해요
# ────────────────────────────────────────────────────────
import os                                     # 파일이 있는지 확인
from datetime import date                     # 날짜 도구

from langchain_core.tools import tool                          # 함수를 도구로
from langchain_core.vectorstores import InMemoryVectorStore    # 벡터 저장소

from common import get_embeddings             # 임베딩 모델

STORE_PATH = "data/handbook_store.json"
BOOKING_FILE = "data/bookings.txt"            # 예약 한 줄: 날짜|시각|회의실|이름
ROOMS = ["새싹룸", "나무룸", "열매룸"]          # 예약할 수 있는 회의실
saved = {}                                    # 저장소를 한 번만 불러와 넣어 둘 사전


@tool
def search_handbook(question: str) -> str:
    """새싹전자 직원 안내서(근무 · 휴가 · 재택 · 출장비 · 보안 · 복지 · 문의처)에서 관련 내용을 찾아요.
    결과의 [N쪽] 은 출처 쪽 번호예요."""
    if "store" not in saved:                  # 처음 한 번만 파일에서 불러와요
        saved["store"] = InMemoryVectorStore.load(STORE_PATH, get_embeddings())
    result = ""
    for doc in saved["store"].similarity_search(question, k=3):   # 비슷한 조각 3개
        result = result + "[" + str(doc.metadata["page"]) + "쪽] " + doc.page_content + "\n"
    return result


@tool
def calculator(expression: str) -> str:
    """사칙연산 식을 정확하게 계산해요. 예: '30000*2 + 80000'"""
    for char in expression:                   # 숫자 · 기호만 허락 (안전)
        if char not in "0123456789+-*/(). ":
            return "계산할 수 없는 식이에요: " + expression
    return str(eval(expression))              # 글자로 된 식을 계산


@tool
def today() -> str:
    """오늘 날짜와 요일을 알려 줘요."""
    days = ["월", "화", "수", "목", "금", "토", "일"]
    now = date.today()
    return now.isoformat() + " (" + days[now.weekday()] + "요일)"   # weekday(): 월요일 = 0


def read_bookings():
    """예약 파일을 읽어 [날짜, 시각, 회의실, 이름] 목록으로 돌려줘요."""
    if not os.path.exists(BOOKING_FILE):      # 아직 예약이 하나도 없으면
        return []
    bookings = []
    with open(BOOKING_FILE, encoding="utf-8") as file:
        for line in file.read().splitlines():  # 줄마다
            bookings.append(line.split("|"))   # "날짜|시각|회의실|이름" → 네 칸 목록
    return bookings


@tool
def list_bookings(day: str) -> str:
    """그날(YYYY-MM-DD)의 회의실 예약 현황을 보여 줘요."""
    lines = []
    for booking_day, booking_time, booking_room, booking_name in read_bookings():   # 날짜 · 시각 · 회의실 · 이름
        if booking_day == day:                # 물어본 날짜의 예약만
            lines.append(booking_time + " " + booking_room + " (" + booking_name + ")")
    if len(lines) == 0:
        return day + " 에는 예약이 없어요. 회의실: " + ", ".join(ROOMS)
    return day + " 예약: " + ", ".join(lines)


@tool
def book_room(day: str, time: str, room: str, name: str) -> str:
    """회의실을 예약해요. day 는 YYYY-MM-DD, time 은 '14:00' 처럼 정시, room 은 새싹룸 · 나무룸 · 열매룸 중 하나."""
    if name.strip() == "":                    # 도구 안에서 값을 꼭 검사해요 (AI 를 믿지 않기)
        return "예약자 이름이 비어 있어요. 이름을 알려 주세요."
    if room not in ROOMS:                     # 없는 회의실
        return "없는 회의실이에요. 고를 수 있는 곳: " + ", ".join(ROOMS)
    for booking_day, booking_time, booking_room, booking_name in read_bookings():   # 중복 검사
        if booking_day == day and booking_time == time and booking_room == room:
            return "이미 예약된 시간이에요: " + day + " " + time + " " + room + " (" + booking_name + ")"
    with open(BOOKING_FILE, "a", encoding="utf-8") as file:   # 모두 통과 → 파일 끝에 덧붙이기
        file.write(day + "|" + time + "|" + room + "|" + name + "\n")
    return "예약했어요: " + day + " " + time + " " + room + " (" + name + ")"


ALL_TOOLS = [search_handbook, calculator, today, list_bookings, book_room]   # assistant.py 가 가져가는 목록
