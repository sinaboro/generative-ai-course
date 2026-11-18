# ex06_cafe_bot.py : 미니 프로젝트 — 대화를 기억하는 카페 주문 도우미 웹 앱
# 실행 후 브라우저에서: http://127.0.0.1:8000
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from pydantic import BaseModel

from common import get_llm

app = FastAPI()
llm = get_llm(temperature=0.3, max_tokens=300)

# 서비스의 성격을 정하는 system 메시지 (사용자에게는 보이지 않아요)
CAFE_RULES = """너는 '새싹 카페' 의 주문 도우미야. 손님에게 존댓말로 두세 문장 이내로 답해.
메뉴: 아메리카노 3,000원, 카페라테 3,500원, 딸기 스무디 4,500원, 치즈 케이크 5,000원.
메뉴에 없는 것은 없다고 말하고, 주문이 끝나면 주문 내용과 합계 금액을 알려 줘."""


class ChatRequest(BaseModel):
    message: str                  # 이번에 손님이 한 말
    history: list[dict] = []      # 지금까지의 대화 [{"role": "human" 또는 "ai", "text": "..."}]


@app.get("/")
def home():
    return FileResponse("static/ex06_cafe.html")


@app.post("/chat")
def chat(request: ChatRequest):
    messages = [SystemMessage(CAFE_RULES)]          # ① 규칙부터
    for turn in request.history:                    # ② 화면이 보내 준 지난 대화를 메시지로
        if turn["role"] == "human":
            messages.append(HumanMessage(turn["text"]))
        else:
            messages.append(AIMessage(turn["text"]))
    messages.append(HumanMessage(request.message))  # ③ 이번 말
    answer = llm.invoke(messages)
    return {"answer": answer.content}


uvicorn.run(app, host="127.0.0.1", port=8000)
