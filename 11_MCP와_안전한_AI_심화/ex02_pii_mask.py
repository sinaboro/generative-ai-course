# ex02_pii_mask.py : 개인정보 가리기 — LLM 에 보내기 전에 전화번호 · 이메일 · 주민번호를 지워요
import re

from llm import ask

PATTERNS = {
    "주민번호": r"\d{6}-\d{7}",
    "전화번호": r"01[016789]-?\d{3,4}-?\d{4}",
    "이메일": r"[\w.+-]+@[\w-]+\.[\w.]+",
}


def mask(text):
    """정해 둔 모양(정규식)과 같은 글자를 [종류] 로 바꿔요."""
    for name, pattern in PATTERNS.items():
        text = re.sub(pattern, f"[{name}]", text)
    return text


raw = ("안녕하세요, 김민지입니다. 환불 요청드려요. 연락처는 010-1234-5678, "
       "메일은 minji@example.com 이고 주민번호는 990101-2345678 입니다.")
safe = mask(raw)
print("원래 글 :", raw)
print("가린 글 :", safe)
print("LLM 답  :", ask("고객 문의를 한 문장으로 요약해: " + safe, temperature=0))
