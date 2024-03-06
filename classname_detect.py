from ultralytics import YOLO
import cv2


model=YOLO("/Users/sandeepanghosh/Downloads/Food_CNN/last.pt")
results=model.predict(source='img.jpg', show=True)
list=results[0].names
for r in results:
    r.names[0]
    boxes=r.boxes
    for box in boxes:
        cls=int(box.cls[0])
        print(list[cls])
