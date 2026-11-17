# ex01_env_check.py : .env 파일에서 API 키 · 주소 · 모델 이름 읽기
# 키를 코드에 직접 적으면 GitHub 에 올라가 다른 사람이 쓸 수 있어요. 그래서 .env 에 따로 둬요
import os

from dotenv import find_dotenv, load_dotenv

path = find_dotenv()                     # 위쪽 폴더로 올라가며 .env 파일 찾기
print(".env 파일:", "찾았어요" if path else "못 찾았어요 (.env.example 을 복사해 .env 를 만들어요)")
load_dotenv(path)                        # .env 의 내용을 환경 변수로 읽어 들이기

base_url = os.getenv("LLM_BASE_URL")
key = os.getenv("LLM_API_KEY", "")
model = os.getenv("LLM_MODEL")

print("LLM_BASE_URL:", base_url)
print("LLM_MODEL   :", model)
# ⚠️ 키는 절대 전부 출력하지 않아요. 앞 8글자와 길이만 확인해요
print("LLM_API_KEY :", (key[:8] + "..." + f" ({len(key)}글자)") if key else "(없음)")
