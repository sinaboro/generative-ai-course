# 문제1 정답: 이메일 작성 도우미 — 역할(system) + 형식 + 길이를 정한 프롬프트
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))   # 한 단계 위 폴더의 llm.py 를 쓰기 위해
from llm import ask

system = "너는 회사 신입사원의 이메일을 다듬어 주는 비서야. 공손하지만 짧게 써."
request = ("팀장님께 보낼 이메일을 써 줘. 내용: 내일 오전 병원 진료 때문에 11시에 출근하겠다. "
           "형식: 제목 한 줄, 본문 3 ~ 4문장, 마지막에 이름 '홍길동'.")
print(ask(request, system=system, temperature=0.3))
