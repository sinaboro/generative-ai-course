# ex02_tokens.py : LLM 이 글을 읽는 단위, 토큰 — 글자 · 단어와 무엇이 다를까?
# 실행 전: pip install tiktoken (처음 실행할 때 토큰 사전 파일을 한 번 내려받아요)
import tiktoken

enc = tiktoken.get_encoding("o200k_base")       # GPT 계열 모델이 쓰는 토큰 사전

texts = [
    "Hello, world!",
    "안녕하세요, 반가워요!",
    "생성형 AI 는 다음 토큰을 예측해요.",
    "ChatGPT",
]
for t in texts:
    ids = enc.encode(t)                           # 글 → 토큰 번호 목록
    pieces = [enc.decode([i]) for i in ids]       # 번호 하나씩 다시 글자로
    print(f"{t!r}")
    print(f"  글자 {len(t)}개 → 토큰 {len(ids)}개: {pieces}")

# 요금은 토큰 수로 매겨요. 긴 글일수록 토큰이 많아져요
long_text = "생성형 AI 수업 " * 100
print("긴 글:", len(long_text), "글자 →", len(enc.encode(long_text)), "토큰")
