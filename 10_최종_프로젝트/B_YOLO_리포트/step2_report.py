# step2_report.py : [B-2단계] YOLO 결과(숫자) → LLM 이 사람이 읽는 리포트로 (구조화 출력)
from pydantic import BaseModel, Field
from ultralytics import YOLO

from common import get_llm


class Report(BaseModel):
    summary: str = Field(description="사진 속 장면을 한 문장으로 요약")
    safety_notes: list[str] = Field(description="보행자 안전을 위해 주의할 점 2 ~ 3개")


def detect(image_path):
    """YOLO 로 물체를 찾아 종류별 개수 사전을 돌려줘요 (확신 0.5 이상만)."""
    result = YOLO("yolov8n.pt")(image_path, verbose=False)[0]
    counts = {}
    for box in result.boxes:
        if float(box.conf) >= 0.5:
            name = result.names[int(box.cls)]
            counts[name] = counts.get(name, 0) + 1
    return counts


counts = detect("https://ultralytics.com/images/bus.jpg")   # step1 과 같은 예시 사진
print("YOLO 결과:", counts)

reporter = get_llm(temperature=0).with_structured_output(Report)
report = reporter.invoke("거리 사진을 YOLO 로 분석한 결과야. 물체 종류(영어)와 개수: " + str(counts) +
                         "\n이 숫자에 있는 것만 근거로 한국어 리포트를 써. 숫자에 없는 물체는 지어내지 마. "
                         "summary 는 장면을 30자 안팎의 한 문장으로, safety_notes 는 이 거리를 걷는 사람이 조심할 점만 써 (AI 모델 이야기는 쓰지 마).")
print("요약:", report.summary)
for note in report.safety_notes:
    print("주의:", note)
