# ex01_env_check.py : .env 파일에서 설정 읽기 — API 키를 코드 밖에 숨겨요
# 흐름: ① .env 파일 찾아 읽기 → ② 값 꺼내기(os.getenv) → ③ 키는 앞부분만 보여 주며 확인
import os                                    # 환경 변수(컴퓨터에 저장된 설정 값)를 읽는 도구

from dotenv import find_dotenv, load_dotenv  # .env 파일을 찾고 읽는 도구

load_dotenv(find_dotenv())                   # ① 위쪽 폴더로 올라가며 .env 파일을 찾아서 읽어요

model = os.getenv("LLM_MODEL")               # ② .env 에 적은 값 꺼내기 (없으면 None)
key = os.getenv("LLM_API_KEY", "")           #    없으면 빈 글자 "" 로

print("모델 이름:", model)                    # ③ 제대로 읽혔는지 확인
print("키 앞부분:", key[:8], "...")          # ⚠️ 키는 앞 8글자만! 전부 출력하지 않아요
print("키 길이:", len(key), "글자")           # 0 이면 .env 를 못 찾았거나 키가 비어 있어요
