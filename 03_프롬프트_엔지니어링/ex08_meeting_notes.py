# ex08_meeting_notes.py : 잘 만든 프롬프트를 함수로 만들어 계속 쓰기 — 회의록 정리기
# ── 전체 흐름 ──────────────────────────────────────────────
# ① system(역할) + human(형식 + 빈칸 {text}) 두 메시지로 질문 틀 만들기
# ② 틀 | AI | 글자 꺼내기 로 체인 만들기
# ③ summarize_meeting(회의 내용) 함수 안에 숨겨 두기 → 다른 곳에서는 함수만 부르면 돼요
# ────────────────────────────────────────────────────────
from langchain_core.output_parsers import StrOutputParser   # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate       # 질문 틀

from common import get_llm                    # AI 를 만드는 함수

template = ChatPromptTemplate.from_messages([   # ① (누가, 내용) 짝의 목록으로 틀 만들기
    ("system", "너는 회의록을 정리하는 비서야. 정해진 형식만 써."),
    ("human", "아래 회의 내용을 정리해.\n형식:\n- 결정된 것: (한 줄)\n- 할 일: (누가 · 무엇을 · 언제까지)\n\n회의 내용:\n{text}"),
])                                              # \n 은 줄 바꿈
chain = template | get_llm(temperature=0) | StrOutputParser()   # ② 체인


def summarize_meeting(text):
    """회의 내용을 받아 정해진 형식으로 정리해요."""
    return chain.invoke({"text": text})         # ③ 빈칸 {text} 에 회의 내용을 넣어 실행


meeting = ("민지: 다음 주 금요일까지 발표 자료를 만들어야 해요. "
           "준호: 제가 화면 디자인을 수요일까지 할게요. "
           "지수: 저는 AI 기능 설명을 목요일까지 쓸게요. "
           "민지: 좋아요, 발표는 제가 할게요. 주제는 '사진 속 쓰레기 찾기' 로 해요.")
print(summarize_meeting(meeting))               # 함수 한 줄로 정리 결과 받기
