# ex03_tokens.py : AI 가 글을 읽는 단위, 토큰 세어 보기
import tiktoken

tokenizer = tiktoken.get_encoding("o200k_base")    # GPT 계열 모델이 쓰는 토큰 사전

texts = ["Hello, world!", "안녕하세요, 반가워요!", "ChatGPT"]
for text in texts:
    token_numbers = tokenizer.encode(text)         # 글 → 토큰 번호 목록
    print(text, "→ 글자", len(text), "개, 토큰", len(token_numbers), "개")

    pieces = []                                    # 토큰 하나하나가 어떤 글자인지 보기
    for number in token_numbers:
        pieces.append(tokenizer.decode([number]))
    print("   토큰 조각:", pieces)
