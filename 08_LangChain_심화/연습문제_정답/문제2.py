# 문제2 정답: 구조화 출력으로 할 일 문장을 객체로 바꾸기
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from pydantic import BaseModel, Field

from common import get_llm


class Todo(BaseModel):
    task: str = Field(description="할 일")
    who: str = Field(description="담당자 이름")
    due: str = Field(description="마감. 글에 적힌 표현 그대로 (예: 목요일). 날짜로 바꾸지 마")


extract = get_llm().with_structured_output(Todo)
t = extract.invoke("지수가 목요일까지 AI 기능 설명 자료를 만들기로 했어요.")
print(t)
print(t.who, "/", t.task, "/", t.due)
