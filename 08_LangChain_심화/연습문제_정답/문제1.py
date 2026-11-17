# 문제1 정답: 언어를 빈칸으로 둔 번역 체인 + batch
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))   # 위 폴더의 common.py
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from common import get_llm

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 번역기야. {lang}로 번역한 문장만 출력해."),
    ("user", "{text}"),
])
chain = prompt | get_llm() | StrOutputParser()
for r in chain.batch([{"lang": "영어", "text": "오늘 수업은 6시에 끝나요."},
                      {"lang": "일본어", "text": "오늘 수업은 6시에 끝나요."}]):
    print(r)
