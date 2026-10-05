"""
Tests for local result history and progress diffs.
"""

import pytest

from devcaliber import history
from devcaliber.evaluator import SeniorityEvaluator
from devcaliber.matrix import QUESTIONS


@pytest.fixture(autouse=True)
def isolated_home(tmp_path, monkeypatch):
    monkeypatch.setenv("DEVCALIBER_HOME", str(tmp_path))


def _result(score: float, name: str = "Ada"):
    return SeniorityEvaluator().evaluate_answers({q.id: score for q in QUESTIONS}, candidate_name=name)


def test_empty_history():
    assert history.load_history() == []
    assert history.previous_entry(_result(2.0)) is None


def test_save_and_diff():
    first = _result(2.0)
    history.save_result(first)
    second = _result(3.5)
    prev = history.previous_entry(second)
    assert prev is not None and prev["overall_score"] == 2.0
    deltas = history.diff_dimensions(second, prev)
    assert deltas and all(d == 1.5 for d in deltas.values())


def test_previous_entry_is_per_candidate():
    history.save_result(_result(2.0, name="Ada"))
    assert history.previous_entry(_result(3.0, name="Grace")) is None


def test_corrupt_history_file_is_ignored():
    path = history.history_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("not json", encoding="utf-8")
    assert history.load_history() == []
