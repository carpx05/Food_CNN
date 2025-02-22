from ultralytics import YOLO
import cv2


model=YOLO("backend/app/ml_models/yolov8m_best.pt")
results=model.predict(source='img.jpg', show=True)
list=results[0].names
for r in results:
    r.names[0]
    boxes=r.boxes
    for box in boxes:
        cls=int(box.cls[0])
        print(list[cls])
