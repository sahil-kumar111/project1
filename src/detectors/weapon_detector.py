from pathlib import Path
from ultralytics import YOLO


class WeaponDetector:

    def __init__(self):

        base_dir = Path(__file__).resolve().parent.parent.parent

        model_path = base_dir / "models" / "weights" / "weapon.pt"

        self.model = YOLO(str(model_path))

        self.weapon_classes = {
            "pistol",
            "knife"
        }

    def detect(self, frame):

        results = self.model(
            frame,
            conf=0.4,
            verbose=False
        )

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])

                class_name = self.model.names[class_id]

                confidence = float(box.conf[0])

                if class_name in self.weapon_classes:

                    return {
                        "object": class_name.capitalize(),
                        "confidence": round(confidence, 3)
                    }

        return None