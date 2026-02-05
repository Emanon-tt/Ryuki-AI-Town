class Event:
    def __init__(self, name, description, priority_weights):
        self.name = name
        self.description = description
        self.priority_weights = priority_weights


EVENTS = {
    "OFFICE_PEACE": Event(
        "The afternoon tea of the office",
        "Kitaoka is concentrating on handling the documents, Goro is doing the cleaning.",
        {"北冈秀一": 6, "由良吾郎": 5}
    ),
    "KITAOKA_ILLNESS": Event(
        "Suddenly feeling unwell, the cancer has worsened",
        "Kitaoka suddenly began to cough uncontrollably and his face turned pale.",
        {"北冈秀一": 2, "由良吾郎": 9}
    ),
    "MIRROR_MONSTER_ALERT": Event(
        "Mirror Monster Attack",
        "A shrill screech suddenly pierced the air. The mirror shattered,"
        "and the monster emerged from the mirror.",
        {"北冈秀一": 8, "由良吾郎": 1}
    )
}


class EventManager:
    def __init__(self):
        self.current_event = EVENTS["OFFICE_PEACE"]
        self.history = []

    def scan_content_for_event(self, text):
        text = text.lower()
        if "monster" in text or "war" in text or "battle" in text:
            self.current_event = EVENTS["MIRROR_MONSTER_ALERT"]
            return True
        if "Feeling unwell" in text or "Coughing" in text or "Medicine" in text:
            self.current_event = EVENTS["KITAOKA_ILLNESS"]
            return False

    def event_prompt(self):
        return f"\ncurrent event: {self.current_event.name}({self.current_event.description})"
