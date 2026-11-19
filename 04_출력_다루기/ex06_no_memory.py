# ex06_no_memory.py : AI 는 앞에서 한 말을 기억하지 못해요
# 흐름: ① 이름 · 동물을 알려 주고 → ② 따로 다시 물어보면 → 모른다고 답해요 (invoke 는 매번 새 대화)
from common import get_llm                    # AI 를 만드는 함수

llm = get_llm(temperature=0)
print("나: 내 이름은 민수야. 나는 고양이를 키워.")
print("AI:", llm.invoke("내 이름은 민수야. 나는 고양이를 키워.").content)      # ① 알려 주기
print("나: 내 이름이 뭐고, 무슨 동물을 키운다고 했지?")
print("AI:", llm.invoke("내 이름이 뭐고, 무슨 동물을 키운다고 했지?").content)  # ② 앞의 말은 안 보냈어요
