# ex01_env_check.py : .env 파일에서 설정 읽기 — API 키를 코드 밖에 숨겨요
import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())                   # 위쪽 폴더로 올라가며 .env 파일을 찾아서 읽어요

model = os.getenv("LLM_MODEL")               # .env 에 적은 값 꺼내기
key = os.getenv("LLM_API_KEY", "")

print("모델 이름:", model)
print("키 앞부분:", key[:8], "...")          # ⚠️ 키는 앞 8글자만! 전부 출력하지 않아요
print("키 길이:", len(key), "글자")
