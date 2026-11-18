# ex05_stream_timing.py : invoke 와 stream 의 "첫 글자가 보이기까지 걸린 시간" 비교
import time                                   # 시간을 재는 도구

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from common import get_llm

template = ChatPromptTemplate.from_template("{topic} 을(를) 초보자에게 5문장으로 설명해 줘.")
chain = template | get_llm() | StrOutputParser()   # Part 03 에서 만든 체인

# ① invoke : 답이 다 만들어져야 한꺼번에 받아요
start = time.time()                           # 시작 시각
answer = chain.invoke({"topic": "인공지능"})
print("[invoke] 첫 글자가 보이기까지:", round(time.time() - start, 1), "초")

# ② stream : 첫 조각이 오자마자 보여 줄 수 있어요
start = time.time()
first = True                                  # 아직 첫 조각을 안 받았다는 표시
for piece in chain.stream({"topic": "인공지능"}):   # 체인도 stream 을 쓸 수 있어요
    if first:
        print("[stream] 첫 글자가 보이기까지:", round(time.time() - start, 1), "초")
        first = False
print("[stream] 전부 받기까지:", round(time.time() - start, 1), "초")
