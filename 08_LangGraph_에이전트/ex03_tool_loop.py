# ex03_tool_loop.py : 도구 부탁 → 실행 → 결과 돌려주기를 반복 — 에이전트의 원리
from langchain_core.messages import HumanMessage, ToolMessage

from common import get_llm
from my_tools import calculator, exchange_rate

tools_by_name = {"calculator": calculator, "exchange_rate": exchange_rate}   # 이름 → 도구
llm_with_tools = get_llm(temperature=0).bind_tools([calculator, exchange_rate])

messages = [HumanMessage("아메리카노 4잔(4,500원)과 케이크 2개(6,000원)를 사면 몇 달러야?")]
answer = llm_with_tools.invoke(messages)
messages.append(answer)

turn = 1
while answer.tool_calls:                      # ⭐ AI 가 도구를 부탁하는 동안 계속 반복
    for call in answer.tool_calls:
        tool = tools_by_name[call["name"]]    # 부탁한 이름의 도구를 꺼내
        result = tool.invoke(call["args"])    # 우리 코드가 실제로 실행하고
        print(turn, "번째 | 도구:", call["name"], call["args"], "→", result)
        messages.append(ToolMessage(content=result, tool_call_id=call["id"]))   # 결과를 대화에 붙여요
    answer = llm_with_tools.invoke(messages)  # 결과를 보고 AI 가 다시 생각해요
    messages.append(answer)
    turn = turn + 1

print("최종 답:", answer.content)
