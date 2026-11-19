# ex02_bind_tools.py : Tool Calling — AI 에게 도구 목록을 알려 주면 "이 도구를 써 줘" 라고 부탁해요
# 흐름: ① bind_tools 로 도구 목록 알려 주기 → ② 질문하기
#       → ③ 도구가 필요하면 tool_calls 에 "도구 이름 + 넣을 값" 부탁이 담겨 와요 (실행은 아직 안 해요!)
from common import get_llm                    # AI 를 만드는 함수
from my_tools import calculator, exchange_rate   # 계산기 · 환율 도구

llm = get_llm(temperature=0)
llm_with_tools = llm.bind_tools([calculator, exchange_rate])   # ⭐ ① 쓸 수 있는 도구 목록 알려 주기

for question in ["123456 곱하기 789 는?", "1달러는 몇 원이야?", "안녕? 반가워!"]:
    answer = llm_with_tools.invoke(question)      # ② 질문
    print("질문:", question)
    print("   도구 부탁:", answer.tool_calls)        # ③ AI 가 부탁한 도구 (없으면 빈 목록)
    print("   글자 답:", answer.content)            # 도구가 필요 없으면 바로 답해요
