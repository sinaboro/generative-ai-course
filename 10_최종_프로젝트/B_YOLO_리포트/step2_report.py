# step2_report.py : [B-2단계] YOLO 결과(숫자) → LLM 이 사람이 읽는 리포트로 (구조화 출력)
# ── 전체 흐름 ──────────────────────────────────────────────
# ① 리포트 모양 Report(요약 · 주의할 점 목록) 정하기
# ② detect(): YOLO 로 물체를 찾아 확신 0.5 이상만 종류별 개수 사전으로 → 예: {"person": 4, "bus": 1}
# ③ 그 개수 사전을 글자로 바꿔 LLM 에게 주고 "이 숫자만 근거로" 리포트를 Report 모양으로 받기
# YOLO = 눈(무엇이 몇 개), LLM = 입(사람이 읽는 말로) 으로 역할을 나눴어요
# ────────────────────────────────────────────────────────
from pydantic import BaseModel, Field         # 리포트 모양 도구
from ultralytics import YOLO                  # YOLO

from common import get_llm                    # AI 를 만드는 함수


class Report(BaseModel):                      # ① 리포트 모양
    summary: str = Field(description="사진 속 장면을 한 문장으로 요약")
    safety_notes: list[str] = Field(description="보행자 안전을 위해 주의할 점 2 ~ 3개")


def detect(image_path):
    """YOLO 로 물체를 찾아 종류별 개수 사전을 돌려줘요 (확신 0.5 이상만)."""
    result = YOLO("yolov8n.pt")(image_path, verbose=False)[0]   # 모델 만들기 + 찾기 + 첫 사진 결과를 한 줄에
    counts = {}
    for box in result.boxes:
        if float(box.conf) >= 0.5:            # 확신이 낮은 것은 빼요 (잘못 찾았을 수 있어서)
            name = result.names[int(box.cls)]
            counts[name] = counts.get(name, 0) + 1
    return counts


counts = detect("https://ultralytics.com/images/bus.jpg")   # ② step1 과 같은 예시 사진
print("YOLO 결과:", counts)

reporter = get_llm(temperature=0).with_structured_output(Report)   # ③ Report 모양으로만 답하는 AI
report = reporter.invoke("거리 사진을 YOLO 로 분석한 결과야. 물체 종류(영어)와 개수: " + str(counts) +   # str(): 사전 → 글자
                         "\n이 숫자에 있는 것만 근거로 한국어 리포트를 써. 숫자에 없는 물체는 지어내지 마. "
                         "summary 는 장면을 30자 안팎의 한 문장으로, safety_notes 는 이 거리를 걷는 사람이 조심할 점만 써 (AI 모델 이야기는 쓰지 마).")
print("요약:", report.summary)
for note in report.safety_notes:              # 주의할 점 목록
    print("주의:", note)
