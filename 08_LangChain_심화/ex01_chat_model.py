# ex01_chat_model.py : LangChain 으로 LLM 부르기 — Part 03 코드와 비교해 보기
from langchain_core.messages import HumanMessage, SystemMessage

from common import MODEL, get_llm

llm = get_llm()                                    # ChatOpenAI 모델 객체
print("모델:", MODEL)

# ① 글자 하나만 넣어도 돼요
r = llm.invoke("LangChain 을 한 문장으로 소개해 줘.")
print("① ", r.content)

# ② 메시지 목록: system · user 를 객체로 써요 (Part 03 의 {"role": ...} 와 같은 뜻)
r = llm.invoke([
    SystemMessage("너는 초보자에게 설명하는 선생님이야. 비유 하나로 두 문장 이내."),
    HumanMessage("체인(chain)이 뭐야?"),
])
print("② ", r.content)
print("토큰 합계:", r.usage_metadata["total_tokens"])   # 사용량도 함께 들어 있어요
