# ex08_meeting_notes.py : 잘 만든 프롬프트를 함수로 만들어 계속 쓰기 — 회의록 정리기
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from common import get_llm

template = ChatPromptTemplate.from_messages([
    ("system", "너는 회의록을 정리하는 비서야. 정해진 형식만 써."),
    ("human", "아래 회의 내용을 정리해.\n형식:\n- 결정된 것: (한 줄)\n- 할 일: (누가 · 무엇을 · 언제까지)\n\n회의 내용:\n{text}"),
])
chain = template | get_llm(temperature=0) | StrOutputParser()


def summarize_meeting(text):
    """회의 내용을 받아 정해진 형식으로 정리해요."""
    return chain.invoke({"text": text})


meeting = ("민지: 다음 주 금요일까지 발표 자료를 만들어야 해요. "
           "준호: 제가 화면 디자인을 수요일까지 할게요. "
           "지수: 저는 AI 기능 설명을 목요일까지 쓸게요. "
           "민지: 좋아요, 발표는 제가 할게요. 주제는 '사진 속 쓰레기 찾기' 로 해요.")
print(summarize_meeting(meeting))
