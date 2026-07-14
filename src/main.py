import cv2

from detectors.weapon_detector import WeaponDetector
from output.event_manager import EventManager

VIDEO_PATH = "../videos/input/nmv1.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("Error opening video.")
    exit()

detector = WeaponDetector()
event_manager = EventManager()

previous_detection = None

frame_number = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame_number += 1

    detection = detector.detect(frame)

    if detection is not None:

        timestamp_ms = cap.get(cv2.CAP_PROP_POS_MSEC)

        total_seconds = timestamp_ms / 1000

        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        milliseconds = int(timestamp_ms % 1000)

        timestamp = (
            f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"
        )

        if previous_detection != detection["object"]:

            print(
                f"{timestamp} --> {detection['object']} "
                f"({detection['confidence']:.2f})"
            )

            event_manager.add_event(
                frame_number=frame_number,
                timestamp=timestamp,
                detected_object=detection["object"],
                confidence=detection["confidence"]
            )

            previous_detection = detection["object"]

    else:

        previous_detection = None

cap.release()

event_manager.save()

print("\nVideo processing completed.")