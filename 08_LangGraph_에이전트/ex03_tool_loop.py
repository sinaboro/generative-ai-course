# ex03_tool_loop.py : 도구 부탁 → 실행 → 결과 돌려주기를 반복 — 에이전트의 원리
# ── 전체 흐름 ──────────────────────────────────────────────
# ① 질문을 보내면 AI 가 "계산기 써 줘" 처럼 도구를 부탁해요 (tool_calls)
# ② 우리 코드가 그 도구를 실제로 실행하고, 결과를 ToolMessage 로 대화에 붙여요
# ③ 결과를 본 AI 가 또 부탁할 수도 있어요 → 부탁이 없을 때까지 ①②를 반복 (while)
# ④ 부탁이 없으면 그게 최종 답이에요
# 이 반복을 대신해 주는 것이 ex07 의 그래프, ex08 의 create_agent 예요
# ────────────────────────────────────────────────────────
from langchain_core.messages import HumanMessage, ToolMessage   # 사람 말 · 도구 결과 메시지

from common import get_llm                    # AI 를 만드는 함수
from my_tools import calculator, exchange_rate   # 도구 두 개

tools_by_name = {"calculator": calculator, "exchange_rate": exchange_rate}   # 이름 → 도구
llm_with_tools = get_llm(temperature=0).bind_tools([calculator, exchange_rate])

messages = [HumanMessage("아메리카노 4잔(4,500원)과 케이크 2개(6,000원)를 사면 몇 달러야?")]
answer = llm_with_tools.invoke(messages)      # ① 첫 질문
messages.append(answer)                       # AI 의 부탁도 대화에 붙여요

turn = 1                                      # 몇 번째 반복인지
while answer.tool_calls:                      # ⭐ ③ AI 가 도구를 부탁하는 동안 계속 반복
    for call in answer.tool_calls:            # 한 번에 여러 개를 부탁할 수도 있어요
        chosen_tool = tools_by_name[call["name"]]   # ② 부탁한 이름의 도구를 꺼내
        result = chosen_tool.invoke(call["args"])   # 우리 코드가 실제로 실행하고
        print(turn, "번째 | 도구:", call["name"], call["args"], "→", result)
        messages.append(ToolMessage(content=result, tool_call_id=call["id"]))   # 결과를 대화에 붙여요
    answer = llm_with_tools.invoke(messages)  # 결과를 보고 AI 가 다시 생각해요
    messages.append(answer)
    turn = turn + 1

print("최종 답:", answer.content)             # ④ 더 부탁하지 않으면 최종 답
