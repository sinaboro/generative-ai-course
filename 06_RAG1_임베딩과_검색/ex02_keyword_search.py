# ex02_keyword_search.py : 낱말이 똑같아야 찾는 "키워드 검색" 과 그 한계
# 흐름: 질문을 낱말로 자르고 → 안내문마다 그 낱말이 들어 있는지 확인 → 들어 있으면 찾은 목록에
#       결과: "환불" 은 찾지만, 뜻이 같은 "돈을 돌려받고 싶어요" 는 못 찾아요 (낱말이 다르니까)
from faq_data import FAQ                      # 고객센터 안내문 목록


def keyword_search(query):
    """질문의 낱말이 하나라도 들어 있는 문장을 모두 찾아요."""
    found = []                             # 찾은 문장을 모을 목록
    for sentence in FAQ:                   # 안내문을 하나씩
        for word in query.split():         # 질문을 빈칸으로 잘라 낱말마다
            if word in sentence:           # 그 낱말이 문장 안에 있으면
                found.append(sentence)
                break                      # 같은 문장을 두 번 넣지 않게 멈춰요
    return found


for query in ["환불", "돈을 돌려받고 싶어요", "물건이 언제 와요?"]:   # 시험할 질문 3개
    results = keyword_search(query)
    print("질문:", query, "→ 찾은 문장", len(results), "개")
    for sentence in results:
        print("   ", sentence)
