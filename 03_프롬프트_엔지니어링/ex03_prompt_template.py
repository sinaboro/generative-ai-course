# ex03_prompt_template.py : 프롬프트 템플릿 — 빈칸 { } 이 있는 질문 틀
# 흐름: ① 빈칸이 있는 틀 만들기 → ② 사전으로 빈칸 채우기 → ③ 완성된 질문을 AI 에게 보내기
from langchain_core.prompts import ChatPromptTemplate   # 질문 틀 도구

from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0)
template = ChatPromptTemplate.from_template("{topic} 을(를) {who} 도 알 수 있게 한 문장으로 설명해 줘.")   # ① 틀

prompt = template.invoke({"topic": "인공지능", "who": "초등학생"})   # ② 빈칸 이름: 넣을 값
print("완성된 질문:", prompt.to_string())      # 빈칸이 채워진 글 확인

answer = llm.invoke(prompt)                   # ③ 완성된 질문 보내기
print("답:", answer.content)
