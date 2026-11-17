# ex02_prompt_chain.py : 프롬프트 템플릿 | 모델 | 출력 파서 — 파이프(|)로 잇는 체인
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from common import get_llm

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 {level} 학생에게 설명하는 선생님이야. 한 문장으로 답해."),
    ("user", "{topic} 이(가) 뭐야?"),
])
chain = prompt | get_llm() | StrOutputParser()      # 왼쪽 결과가 오른쪽으로 흘러가요

# invoke: 빈칸에 들어갈 값을 사전으로 넣어요
print(chain.invoke({"level": "초등학생", "topic": "인공지능"}))

# batch: 여러 입력을 한 번에 (같은 체인을 여러 번 쓰기)
answers = chain.batch([
    {"level": "중학생", "topic": "토큰"},
    {"level": "대학생", "topic": "임베딩"},
])
for a in answers:
    print("-", a)
