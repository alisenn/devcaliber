"""
Assessment modes: how many questions, how long, and how much confidence to expect.
"""

from dataclasses import dataclass
from typing import Callable, Dict, List

from devcaliber.models import Question


@dataclass(frozen=True)
class AssessmentMode:
    key: str
    label: str
    label_tr: str
    minutes: int
    confidence: str  # "low" | "medium" | "high"
    select: Callable[[Question], bool]

    def pool(self, questions: List[Question]) -> List[Question]:
        return [q for q in questions if self.select(q)]


MODES: Dict[str, AssessmentMode] = {
    "pulse": AssessmentMode(
        "pulse", "Pulse Check", "Hızlı Nabız Ölçümü", 5, "low", lambda q: q.is_quick
    ),
    "sprint": AssessmentMode(
        "sprint", "Sprint Assessment", "Sprint Değerlendirme", 30, "medium", lambda q: q.sprint
    ),
    "deep": AssessmentMode(
        "deep", "Deep Assessment", "Derin Değerlendirme", 120, "high", lambda q: True
    ),
}
