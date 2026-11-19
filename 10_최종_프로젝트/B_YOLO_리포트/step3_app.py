# step3_app.py : [B-3단계] 사진을 올리면 YOLO + LLM 리포트를 보여 주는 웹 앱
# 실행: python step3_app.py → http://127.0.0.1:8000
# ── 전체 흐름 ──────────────────────────────────────────────
# 서버가 켜질 때 YOLO 모델과 리포트 AI 를 한 번만 준비해요
# 화면에서 사진을 올리면 POST /analyze:
#   ① 올린 사진을 images/upload.jpg 로 저장 → ② YOLO 로 찾고 상자 그린 사진 저장 · 종류별 개수 세기
#   → ③ LLM 이 리포트 작성 → {개수, 요약, 주의할 점} 을 돌려줘요
# 화면은 /result.jpg 로 상자 그린 사진을 받아 보여 줘요
# ────────────────────────────────────────────────────────
import uvicorn                                # 서버 실행 프로그램
from fastapi import FastAPI, UploadFile       # 웹 서버 도구 · 올린 파일
from fastapi.responses import FileResponse    # 파일 보내기
from pydantic import BaseModel, Field         # 리포트 모양
from ultralytics import YOLO                  # YOLO

from common import get_llm                    # AI 를 만드는 함수

app = FastAPI()
model = YOLO("yolov8n.pt")                    # 서버가 켜질 때 한 번만 준비


class Report(BaseModel):                      # step2 와 같은 리포트 모양
    summary: str = Field(description="사진 속 장면을 한 문장으로 요약")
    safety_notes: list[str] = Field(description="보행자 안전을 위해 주의할 점 2 ~ 3개")


reporter = get_llm(temperature=0).with_structured_output(Report)


@app.get("/")                                 # 화면 보내기
def home():
    return FileResponse("static/index.html")


@app.get("/result.jpg")                       # 상자를 그린 사진 보내기
def result_image():
    return FileResponse("images/upload_result.jpg")   # 상자를 그린 사진


@app.post("/analyze")
def analyze(file: UploadFile):               # 화면에서 올린 사진 파일
    with open("images/upload.jpg", "wb") as saved:   # ① 사진을 파일로 저장 ("wb" = 바이트로 쓰기)
        saved.write(file.file.read())                #    올린 파일의 내용을 그대로
    result = model("images/upload.jpg", verbose=False)[0]   # ② YOLO
    result.save(filename="images/upload_result.jpg")        #    상자 그린 사진 저장
    counts = {}
    for box in result.boxes:                  #    확신 0.5 이상만 종류별로 세기
        if float(box.conf) >= 0.5:
            name = result.names[int(box.cls)]
            counts[name] = counts.get(name, 0) + 1
    report = reporter.invoke("거리 사진을 YOLO 로 분석한 결과야. 물체 종류(영어)와 개수: " + str(counts) +   # ③ LLM
                             "\n이 숫자에 있는 것만 근거로 한국어 리포트를 써. 숫자에 없는 물체는 지어내지 마. "
                             "summary 는 장면을 30자 안팎의 한 문장으로, safety_notes 는 이 거리를 걷는 사람이 조심할 점만 써 (AI 모델 이야기는 쓰지 마).")
    return {"counts": counts, "summary": report.summary, "safety_notes": report.safety_notes}


uvicorn.run(app, host="127.0.0.1", port=8000)   # 서버 켜기
