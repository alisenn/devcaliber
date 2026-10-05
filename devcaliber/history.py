"""
Local result history so retakes can show progress over time.
Stored as JSON in ~/.devcaliber/history.json (override the folder with DEVCALIBER_HOME).
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional

from devcaliber.models import AssessmentResult


def history_path() -> Path:
    home = os.environ.get("DEVCALIBER_HOME")
    base = Path(home) if home else Path.home() / ".devcaliber"
    return base / "history.json"


def load_history() -> List[Dict]:
    path = history_path()
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (OSError, ValueError):
        return []


def entry_from_result(result: AssessmentResult) -> Dict:
    return {
        "name": result.candidate_name,
        "track": result.track.value,
        "mode": result.assessment_mode,
        "timestamp": result.timestamp,
        "overall_score": result.overall_score,
        "level": result.overall_level.code,
        "confidence": result.confidence,
        "dimensions": {d.value: s.score for d, s in result.dimension_scores.items()},
    }


def previous_entry(result: AssessmentResult) -> Optional[Dict]:
    """Latest earlier entry for the same name and track."""
    for entry in reversed(load_history()):
        if entry.get("name") == result.candidate_name and entry.get("track") == result.track.value:
            return entry
    return None


def save_result(result: AssessmentResult) -> None:
    path = history_path()
    history = load_history()
    history.append(entry_from_result(result))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(history, indent=1), encoding="utf-8")


def diff_dimensions(result: AssessmentResult, previous: Dict) -> Dict[str, float]:
    """Per-dimension score change versus a previous entry (dimension value -> delta)."""
    prev = previous.get("dimensions", {})
    return {
        d.value: round(s.score - prev[d.value], 2)
        for d, s in result.dimension_scores.items()
        if d.value in prev
    }
