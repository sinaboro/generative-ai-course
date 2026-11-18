# ex03_first_embedding.py : 임베딩 — 글을 숫자 목록(벡터)으로 바꾸기
from common import get_embeddings

embeddings = get_embeddings()                         # 임베딩 모델 준비
vector = embeddings.embed_query("강아지가 공원에서 뛰어놀아요.")   # 글 → 숫자 목록

print("숫자 개수:", len(vector))                      # 벡터의 길이
print("앞의 숫자 5개:", vector[:5])                   # [:5] 는 앞에서 5개만
