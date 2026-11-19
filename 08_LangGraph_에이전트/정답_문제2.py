# 정답_문제2.py : 단위 바꾸기 도구를 더한 에이전트
# 흐름: ① 새 도구 convert_unit 만들기 → ② 계산기와 함께 에이전트에 주기
#       → ③ "5피트 9인치" 질문에 AI 가 단위 바꾸기를 두 번 부탁하고, 계산기로 더해서 답해요
from langchain.agents import create_agent     # 에이전트 만들기
from langchain_core.tools import tool         # 함수를 도구로 바꾸는 표시

from common import get_llm                    # AI 를 만드는 함수
from my_tools import calculator, show_steps   # 계산기 · 과정 보기


@tool                                         # ① 새 도구
def convert_unit(value: float, unit: str) -> str:
    """길이 · 무게 단위를 미터법으로 바꿔요. unit 은 inch, feet, mile, pound 중 하나."""
    rates = {"inch": [2.54, "cm"], "feet": [30.48, "cm"], "mile": [1.609, "km"], "pound": [0.4536, "kg"]}   # 단위: [곱할 수, 새 단위]
    if unit not in rates:
        return "모르는 단위예요: " + unit
    number, new_unit = rates[unit]            # [2.54, "cm"] 을 두 변수로 나눠 받기
    return str(value) + " " + unit + " = " + str(round(value * number, 2)) + " " + new_unit


agent = create_agent(                         # ② 도구 두 개를 가진 에이전트
    get_llm(temperature=0),
    tools=[convert_unit, calculator],
    system_prompt="단위 바꾸기는 convert_unit, 계산은 calculator 로 해. 한국어 두 문장 이내로 답해.",
)

question = "키가 5피트 9인치면 몇 cm 야?"
result = agent.invoke({"messages": [{"role": "user", "content": question}]})   # ③
show_steps(result["messages"])                # 도구를 어떤 순서로 썼는지 보기
