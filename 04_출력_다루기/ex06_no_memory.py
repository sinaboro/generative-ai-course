# ex06_no_memory.py : AI 는 앞에서 한 말을 기억하지 못해요
from common import get_llm

llm = get_llm(temperature=0)
print("나: 내 이름은 민수야. 나는 고양이를 키워.")
print("AI:", llm.invoke("내 이름은 민수야. 나는 고양이를 키워.").content)
print("나: 내 이름이 뭐고, 무슨 동물을 키운다고 했지?")
print("AI:", llm.invoke("내 이름이 뭐고, 무슨 동물을 키운다고 했지?").content)
