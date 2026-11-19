# ex06_cafe_bot.py : 미니 프로젝트 — 대화를 기억하는 카페 주문 도우미 웹 앱
# 실행 후 브라우저에서: http://127.0.0.1:8000
# ── 전체 흐름 ──────────────────────────────────────────────
# 서버는 대화를 저장하지 않아요. 대신 화면(JavaScript)이 지난 대화를 모아 두었다가 매번 함께 보내요.
# ① 화면 → POST /chat {"message": 이번 말, "history": [지난 대화…]}
# ② 서버: [가게 규칙] + [지난 대화를 메시지로 바꾼 것] + [이번 말] 을 차례로 목록에 담아 AI 에게 보내기
# ③ 답을 돌려주면 → 화면이 말풍선을 그리고, 이번 대화 두 개를 자기 기록에 더해요
# ────────────────────────────────────────────────────────
import uvicorn                                              # 서버 실행 프로그램
from fastapi import FastAPI                                 # 웹 서버 도구
from fastapi.responses import FileResponse                  # HTML 파일 보내기
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage   # 메시지 세 종류
from pydantic import BaseModel                              # 받을 데이터 모양

from common import get_llm                                  # AI 를 만드는 함수

app = FastAPI()
llm = get_llm(temperature=0.3, max_tokens=300)

# 서비스의 성격을 정하는 system 메시지 (사용자에게는 보이지 않아요)
CAFE_RULES = """너는 '새싹 카페' 의 주문 도우미야. 손님에게 존댓말로 두세 문장 이내로 답해.
메뉴: 아메리카노 3,000원, 카페라테 3,500원, 딸기 스무디 4,500원, 치즈 케이크 5,000원.
메뉴에 없는 것은 없다고 말하고, 주문이 끝나면 주문 내용과 합계 금액을 알려 줘."""


class ChatRequest(BaseModel):
    message: str                  # 이번에 손님이 한 말
    history: list[dict] = []      # 지금까지의 대화 [{"role": "human" 또는 "ai", "text": "..."}]


@app.get("/")                     # 주문 화면 보내기
def home():
    return FileResponse("static/ex06_cafe.html")


@app.post("/chat")
def chat(request: ChatRequest):
    messages = [SystemMessage(CAFE_RULES)]          # ① 규칙부터
    for turn in request.history:                    # ② 화면이 보내 준 지난 대화를 메시지로
        if turn["role"] == "human":                 #    손님이 한 말이면
            messages.append(HumanMessage(turn["text"]))
        else:                                       #    도우미(AI)가 한 말이면
            messages.append(AIMessage(turn["text"]))
    messages.append(HumanMessage(request.message))  # ③ 이번 말
    answer = llm.invoke(messages)                   # 목록 전체를 보내 답 받기
    return {"answer": answer.content}


uvicorn.run(app, host="127.0.0.1", port=8000)   # 서버 켜기
