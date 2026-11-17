# 문제2 정답: 대화를 기억하는 콘솔 챗봇 (입력 대신 정해 둔 질문 목록으로 시험)
# 직접 해 보려면 for 문 대신  q = input("나: ")  로 바꿔 보세요 (빈 줄이면 끝)
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))   # 위 폴더의 llm.py
from llm import chat

messages = [{"role": "system", "content": "너는 짧게 답하는 친구 같은 챗봇이야. 한 문장으로 답해."}]
for q in ["내 이름은 민지야.", "나는 고양이를 좋아해.", "내 이름이 뭐였지? 그리고 내가 좋아하는 동물은?"]:
    messages.append({"role": "user", "content": q})
    a = chat(messages, temperature=0)
    messages.append({"role": "assistant", "content": a})
    print("나:", q)
    print("봇:", a)
