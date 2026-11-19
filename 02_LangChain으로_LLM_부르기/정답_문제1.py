# 정답_문제1.py : 번역 함수 만들기 — 규칙(System)을 정하고 temperature 0
# 흐름: ① AI 준비 → ② translate 함수: 규칙 + 번역할 글을 메시지로 보내 답 글자 돌려주기 → ③ 세 번 써 보기
from langchain_core.messages import HumanMessage, SystemMessage   # 규칙 · 사람 메시지

from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0)                  # ① 번역은 늘 같은 답이 좋아요


def translate(text, language):
    """text 를 language 로 번역해서 돌려줘요."""
    messages = [                              # ② 보낼 메시지 목록
        SystemMessage("너는 번역기야. " + language + "로 번역한 문장만 출력해."),   # 규칙
        HumanMessage(text),                   # 번역할 글
    ]
    return llm.invoke(messages).content       # 보내고 답 글자만 돌려주기


print(translate("오늘 날씨가 정말 좋네요.", "영어"))              # ③ 한국어 → 영어
print(translate("이 버튼을 누르면 사진이 올라가요.", "영어"))
print(translate("Thank you for coming today.", "한국어"))         #    영어 → 한국어
