# step3_app.py : [B-3단계] 사진을 올리면 YOLO + LLM 리포트를 보여 주는 웹 앱
# 실행: python step3_app.py → http://127.0.0.1:8000
import uvicorn
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from ultralytics import YOLO

from common import get_llm

app = FastAPI()
model = YOLO("yolov8n.pt")                    # 서버가 켜질 때 한 번만 준비


class Report(BaseModel):
    summary: str = Field(description="사진 속 장면을 한 문장으로 요약")
    safety_notes: list[str] = Field(description="보행자 안전을 위해 주의할 점 2 ~ 3개")


reporter = get_llm(temperature=0).with_structured_output(Report)


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/result.jpg")
def result_image():
    return FileResponse("images/upload_result.jpg")   # 상자를 그린 사진


@app.post("/analyze")
def analyze(file: UploadFile):               # 화면에서 올린 사진 파일
    with open("images/upload.jpg", "wb") as saved:   # ① 사진을 파일로 저장
        saved.write(file.file.read())
    result = model("images/upload.jpg", verbose=False)[0]   # ② YOLO
    result.save(filename="images/upload_result.jpg")
    counts = {}
    for box in result.boxes:
        if float(box.conf) >= 0.5:
            name = result.names[int(box.cls)]
            counts[name] = counts.get(name, 0) + 1
    report = reporter.invoke("거리 사진을 YOLO 로 분석한 결과야. 물체 종류(영어)와 개수: " + str(counts) +   # ③ LLM
                             "\n이 숫자에 있는 것만 근거로 한국어 리포트를 써. 숫자에 없는 물체는 지어내지 마. "
                             "summary 는 장면을 30자 안팎의 한 문장으로, safety_notes 는 이 거리를 걷는 사람이 조심할 점만 써 (AI 모델 이야기는 쓰지 마).")
    return {"counts": counts, "summary": report.summary, "safety_notes": report.safety_notes}


uvicorn.run(app, host="127.0.0.1", port=8000)
