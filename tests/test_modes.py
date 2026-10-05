"""
Tests for assessment modes, option shuffling and web/question-bank sync.
"""

import subprocess
import sys
from pathlib import Path

from devcaliber.matrix import QUESTIONS
from devcaliber.models import DimensionId
from devcaliber.modes import MODES

ROOT = Path(__file__).resolve().parent.parent


def test_mode_sizes():
    assert len(MODES["pulse"].pool(QUESTIONS)) == 5
    assert len(MODES["sprint"].pool(QUESTIONS)) == 15
    assert len(MODES["deep"].pool(QUESTIONS)) == 60


def test_every_mode_covers_every_dimension_evenly():
    for key, per_dim in (("pulse", 1), ("sprint", 3), ("deep", 12)):
        pool = MODES[key].pool(QUESTIONS)
        for dim in DimensionId:
            assert sum(q.dimension == dim for q in pool) == per_dim, (key, dim)


def test_mode_budgets_grow():
    assert MODES["pulse"].minutes < MODES["sprint"].minutes < MODES["deep"].minutes == 120
    assert MODES["sprint"].minutes == 30


def test_web_app_is_in_sync_with_question_bank():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_web.py"), "--check"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
