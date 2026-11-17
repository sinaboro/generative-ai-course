# 문제2 정답: 내 이름 · 자기소개 문장의 토큰 수 세어 보기
import tiktoken

enc = tiktoken.get_encoding("o200k_base")
for t in ["홍길동", "Hong Gildong", "저는 AI 서비스를 만드는 개발자가 되고 싶어요."]:
    ids = enc.encode(t)
    print(f"{t} → 글자 {len(t)}개, 토큰 {len(ids)}개")
