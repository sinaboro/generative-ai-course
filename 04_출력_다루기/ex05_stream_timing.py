# ex05_stream_timing.py : invoke 와 stream 의 "첫 글자가 보이기까지 걸린 시간" 비교
# ── 전체 흐름 ──────────────────────────────────────────────
# ① invoke: 시작 시각을 적고 → 답 전체를 받은 뒤 걸린 시간 출력
# ② stream: 시작 시각을 적고 → 첫 조각이 온 순간의 시간 출력 → 다 받은 뒤 전체 시간 출력
# 결과: 전체 시간은 비슷하지만, stream 은 첫 글자를 훨씬 빨리 보여 줘요
# ────────────────────────────────────────────────────────
import time                                   # 시간을 재는 도구

from langchain_core.output_parsers import StrOutputParser   # 글자만 꺼내기
from langchain_core.prompts import ChatPromptTemplate       # 질문 틀

from common import get_llm                    # AI 를 만드는 함수

template = ChatPromptTemplate.from_template("{topic} 을(를) 초보자에게 5문장으로 설명해 줘.")
chain = template | get_llm() | StrOutputParser()   # Part 03 에서 만든 체인

# ① invoke : 답이 다 만들어져야 한꺼번에 받아요
start = time.time()                           # 시작 시각
answer = chain.invoke({"topic": "인공지능"})
print("[invoke] 첫 글자가 보이기까지:", round(time.time() - start, 1), "초")   # 지금 - 시작 = 걸린 초

# ② stream : 첫 조각이 오자마자 보여 줄 수 있어요
start = time.time()
first = True                                  # 아직 첫 조각을 안 받았다는 표시
for piece in chain.stream({"topic": "인공지능"}):   # 조각을 받기만 해요 (시간만 재려고 출력은 안 해요)
    if first:                                 # 첫 조각일 때만
        print("[stream] 첫 글자가 보이기까지:", round(time.time() - start, 1), "초")
        first = False                         # 다음부터는 출력하지 않게
print("[stream] 전부 받기까지:", round(time.time() - start, 1), "초")
