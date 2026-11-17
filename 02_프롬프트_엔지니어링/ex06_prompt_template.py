# ex06_prompt_template.py : 프롬프트 템플릿 — 잘 만든 프롬프트를 함수로 만들어 계속 쓰기
from llm import ask

SUMMARY_SYSTEM = "너는 회의록을 정리하는 비서야. 항상 한국어로, 정해진 형식만 써."
SUMMARY_TEMPLATE = """아래 회의 내용을 정리해.
형식:
- 결정된 것: (한 줄)
- 할 일: (누가 · 무엇을 · 언제까지, 목록)

회의 내용:
{text}"""


def summarize_meeting(text):
    """회의 내용을 받아 정해진 형식으로 정리해요."""
    return ask(SUMMARY_TEMPLATE.format(text=text), system=SUMMARY_SYSTEM, temperature=0)


meeting = ("민지: 다음 주 금요일까지 발표 자료를 만들어야 해요. "
           "준호: 그럼 제가 화면 디자인을 수요일까지 할게요. "
           "지수: 저는 AI 기능 설명 부분을 목요일까지 쓸게요. "
           "민지: 좋아요, 발표는 제가 할게요. 주제는 '사진 속 쓰레기 찾기' 로 정해요.")
print(summarize_meeting(meeting))
