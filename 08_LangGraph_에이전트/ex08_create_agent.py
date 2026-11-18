# ex08_create_agent.py : create_agent — 에이전트를 한 줄로 만들기 + RAG 를 도구로 쓰기
from langchain.agents import create_agent

from common import get_llm
from my_tools import calculator, search_faq, show_steps

agent = create_agent(
    get_llm(temperature=0),                   # 생각할 AI
    tools=[search_faq, calculator],           # 안내문 검색(RAG) + 계산기
    system_prompt="너는 새싹전자 고객센터 상담원이야. 규정은 search_faq 로 찾고, 계산은 calculator 로 해. "
                  "안내문에 없는 내용은 지어내지 마.",
)

question = "2만 5천 원어치 사면 배송비까지 모두 얼마예요?"
result = agent.invoke({"messages": [{"role": "user", "content": question}]})
show_steps(result["messages"])
