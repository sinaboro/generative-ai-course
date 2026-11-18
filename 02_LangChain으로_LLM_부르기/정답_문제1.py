# 정답_문제1.py : 번역 함수 만들기 — 규칙(System)을 정하고 temperature 0
from langchain_core.messages import HumanMessage, SystemMessage

from common import get_llm

llm = get_llm(temperature=0)


def translate(text, language):
    """text 를 language 로 번역해서 돌려줘요."""
    messages = [
        SystemMessage("너는 번역기야. " + language + "로 번역한 문장만 출력해."),
        HumanMessage(text),
    ]
    return llm.invoke(messages).content


print(translate("오늘 날씨가 정말 좋네요.", "영어"))
print(translate("이 버튼을 누르면 사진이 올라가요.", "영어"))
print(translate("Thank you for coming today.", "한국어"))
