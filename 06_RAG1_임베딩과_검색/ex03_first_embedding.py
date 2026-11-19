# ex03_first_embedding.py : 임베딩 — 글을 숫자 목록(벡터)으로 바꾸기
# 흐름: ① 임베딩 모델 준비 → ② 문장 하나를 숫자 목록으로 → ③ 숫자가 몇 개인지, 앞의 몇 개는 어떤지 보기
from common import get_embeddings                     # 임베딩 모델을 만드는 함수

embeddings = get_embeddings()                         # ① 임베딩 모델 준비
vector = embeddings.embed_query("강아지가 공원에서 뛰어놀아요.")   # ② 글 → 숫자 목록

print("숫자 개수:", len(vector))                      # ③ 벡터의 길이 (모델마다 정해져 있어요)
print("앞의 숫자 5개:", vector[:5])                   # [:5] 는 앞에서 5개만
