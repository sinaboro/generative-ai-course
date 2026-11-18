# 정답_문제2.py : 단위 바꾸기 도구를 더한 에이전트
from langchain.agents import create_agent
from langchain_core.tools import tool

from common import get_llm
from my_tools import calculator, show_steps


@tool
def convert_unit(value: float, unit: str) -> str:
    """길이 · 무게 단위를 미터법으로 바꿔요. unit 은 inch, feet, mile, pound 중 하나."""
    rates = {"inch": [2.54, "cm"], "feet": [30.48, "cm"], "mile": [1.609, "km"], "pound": [0.4536, "kg"]}
    if unit not in rates:
        return "모르는 단위예요: " + unit
    number = rates[unit][0]
    new_unit = rates[unit][1]
    return str(value) + " " + unit + " = " + str(round(value * number, 2)) + " " + new_unit


agent = create_agent(
    get_llm(temperature=0),
    tools=[convert_unit, calculator],
    system_prompt="단위 바꾸기는 convert_unit, 계산은 calculator 로 해. 한국어 두 문장 이내로 답해.",
)

question = "키가 5피트 9인치면 몇 cm 야?"
result = agent.invoke({"messages": [{"role": "user", "content": question}]})
show_steps(result["messages"])
