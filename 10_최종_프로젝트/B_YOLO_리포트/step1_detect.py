# step1_detect.py : [B-1단계] YOLO 로 사진 속 물체 찾기 → 종류별 개수 세기
from ultralytics import YOLO                  # 물체를 찾아 주는 YOLO 라이브러리

IMAGE = "https://ultralytics.com/images/bus.jpg"   # YOLO 공식 예시 사진 (내 사진 경로로 바꿔도 돼요)

model = YOLO("yolov8n.pt")                    # 가장 작은 YOLO 모델 (처음 실행할 때 자동으로 내려받아요)
results = model(IMAGE, verbose=False)         # 사진에서 물체 찾기
result = results[0]                           # 사진 한 장의 결과

counts = {}                                   # {"person": 4, "bus": 1} 처럼 종류별 개수
for box in result.boxes:                      # 찾은 상자(물체) 하나씩
    name = result.names[int(box.cls)]         # 종류 번호 → 이름
    confidence = float(box.conf)              # 얼마나 확신하는지 (0 ~ 1)
    print(name, "(확신", round(confidence, 2), ")")
    counts[name] = counts.get(name, 0) + 1

print("종류별 개수:", counts)
result.save(filename="images/result.jpg")    # 상자를 그린 사진 저장
print("상자를 그린 사진: images/result.jpg")
