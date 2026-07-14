import json
from pathlib import Path


class EventManager:

    def __init__(self):

        self.events = []

        self.base_dir = Path(__file__).resolve().parent.parent.parent

        self.output_file = (
            self.base_dir
            / "results"
            / "json"
            / "detections.json"
        )

    def add_event(
        self,
        frame_number,
        timestamp,
        detected_object,
        confidence
    ):

        event = {

            "frame": frame_number,

            "timestamp": timestamp,

            "object": detected_object,

            "confidence": confidence

        }

        self.events.append(event)

    def save(self):

        with open(self.output_file, "w") as file:

            json.dump(
                self.events,
                file,
                indent=4
            )

        print(f"\nSaved {len(self.events)} event(s).")