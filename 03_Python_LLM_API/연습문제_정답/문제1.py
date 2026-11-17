# 문제1 정답: 번역기 함수 — system 으로 역할을 고정하고 temperature=0 으로 늘 같은 답
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))   # 위 폴더의 llm.py
from llm import ask


def translate(text, to="영어"):
    system = f"너는 번역기야. 입력을 {to}로 자연스럽게 번역하고, 번역문만 출력해."
    return ask(text, system=system, temperature=0)


for s in ["오늘 날씨가 정말 좋네요.", "이 버튼을 누르면 사진이 업로드돼요."]:
    print(s, "→", translate(s))
print(translate("Thank you for coming today.", to="한국어"))
