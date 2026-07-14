from ultralytics import YOLO

model = YOLO("../models/weights/weapon.pt")

results = model(
    "../videos/input/nmv1.mp4",
    conf=0.4,
    save=True
)

print(results[0].boxes)