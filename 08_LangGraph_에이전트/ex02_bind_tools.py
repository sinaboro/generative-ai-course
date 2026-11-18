# ex02_bind_tools.py : Tool Calling — AI 에게 도구 목록을 알려 주면 "이 도구를 써 줘" 라고 부탁해요
from common import get_llm
from my_tools import calculator, exchange_rate

llm = get_llm(temperature=0)
llm_with_tools = llm.bind_tools([calculator, exchange_rate])   # ⭐ 쓸 수 있는 도구 목록 알려 주기

for question in ["123456 곱하기 789 는?", "1달러는 몇 원이야?", "안녕? 반가워!"]:
    answer = llm_with_tools.invoke(question)
    print("질문:", question)
    print("   도구 부탁:", answer.tool_calls)        # AI 가 부탁한 도구 (없으면 빈 목록)
    print("   글자 답:", answer.content)            # 도구가 필요 없으면 바로 답해요
