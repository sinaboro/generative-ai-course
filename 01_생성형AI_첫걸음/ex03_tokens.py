# ex03_tokens.py : AI 가 글을 읽는 단위, 토큰 세어 보기
# 흐름: ① 토큰 사전 준비 → ② 글을 토큰 번호로 바꿔 개수 세기 → ③ 번호를 하나씩 글자로 되돌려 보기
import tiktoken                                    # OpenAI 가 만든 토큰 계산 도구

tokenizer = tiktoken.get_encoding("o200k_base")    # ① GPT 계열 모델이 쓰는 토큰 사전

texts = ["Hello, world!", "안녕하세요, 반가워요!", "ChatGPT"]   # 비교해 볼 글 3개
for text in texts:
    token_numbers = tokenizer.encode(text)         # ② 글 → 토큰 번호 목록
    print(text, "→ 글자", len(text), "개, 토큰", len(token_numbers), "개")

    pieces = []                                    # ③ 토큰 하나하나가 어떤 글자인지 보기
    for number in token_numbers:                   # 번호를 하나씩 꺼내서
        pieces.append(tokenizer.decode([number]))  # 번호 → 글자 조각으로 되돌리기
    print("   토큰 조각:", pieces)                  # 한글은 한 글자가 여러 조각이 되기도 해요
