# my_tools.py : 이 Part 의 예제가 함께 쓰는 도구들과, 에이전트가 한 일을 보여 주는 함수
from langchain_core.tools import tool
from langchain_core.vectorstores import InMemoryVectorStore

from common import get_embeddings
from faq_data import FAQ


@tool
def calculator(expression: str) -> str:
    """사칙연산 식을 정확하게 계산해요. 예: '4500*4 + 6000*2'"""
    for char in expression:                   # 숫자 · 연산 기호 · 괄호 · 빈칸만 허락해요 (안전)
        if char not in "0123456789+-*/(). ":
            return "계산할 수 없는 식이에요: " + expression
    return str(eval(expression))              # eval: 글자로 된 식을 Python 이 계산


@tool
def exchange_rate(currency: str) -> str:
    """외화 1 단위가 몇 원인지 알려 줘요. currency 는 USD, JPY, EUR 중 하나."""
    rates = {"USD": 1380, "JPY": 9.2, "EUR": 1495}   # 연습용으로 정해 둔 환율
    code = currency.upper()
    if code not in rates:
        return "모르는 통화예요: " + currency
    return "1 " + code + " = " + str(rates[code]) + "원"


saved = {}                                    # 처음 쓸 때 한 번만 만든 FAQ 저장소를 넣어 둘 사전


@tool
def search_faq(question: str) -> str:
    """새싹전자 고객센터 안내문(환불 · 교환 · 배송 · 배송비 · 수리 · 회원 등급 등)에서 관련 내용을 찾아요."""
    if "faq" not in saved:                    # 아직 안 만들었으면 지금 한 번만 만들어요
        saved["faq"] = InMemoryVectorStore.from_texts(FAQ, get_embeddings())
    found = saved["faq"].similarity_search(question, k=2)
    result = ""
    for doc in found:
        result = result + doc.page_content + "\n"
    return result


def show_steps(messages):
    """에이전트가 주고받은 메시지를 차례로 보여 줘요 (생각 → 도구 → 결과 → 답)."""
    for message in messages:
        if message.type == "human":
            print("🙋 질문:", message.content)
        elif message.type == "ai" and message.tool_calls:
            for call in message.tool_calls:
                print("🤖 도구 부탁:", call["name"], call["args"])
        elif message.type == "tool":
            print("🔧 도구 결과:", message.content.strip().replace("\n", " / "))
        elif message.type == "ai":
            print("🤖 답:", message.content)
