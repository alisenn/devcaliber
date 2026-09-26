"""
Unit tests for the seniority evaluator engine.
"""

from levelcraft.models import SeniorityLevel, DimensionId, Track
from levelcraft.evaluator import SeniorityEvaluator
from levelcraft.matrix import QUESTIONS


def test_evaluator_all_junior_answers():
    evaluator = SeniorityEvaluator(track=Track.GENERAL)
    answers = {q.id: 1.0 for q in QUESTIONS}
    result = evaluator.evaluate_answers(answers, candidate_name="Junior Dev")

    assert result.overall_level == SeniorityLevel.L1
    assert result.overall_score == 1.0
    assert result.total_questions == len(QUESTIONS)
    for dim_id, dscore in result.dimension_scores.items():
        assert dscore.level == SeniorityLevel.L1
        assert dscore.score == 1.0


def test_evaluator_all_senior_answers():
    evaluator = SeniorityEvaluator(track=Track.BACKEND)
    answers = {q.id: 3.5 for q in QUESTIONS}
    result = evaluator.evaluate_answers(answers, candidate_name="Senior Dev")

    assert result.overall_level == SeniorityLevel.L3
    assert 3.4 <= result.overall_score <= 3.6
    assert len(result.gap_recommendations) == 5


def test_percentile_calibration():
    assert SeniorityEvaluator.calculate_percentile(1.0) == 5
    assert SeniorityEvaluator.calculate_percentile(3.0) == 70
    assert SeniorityEvaluator.calculate_percentile(4.5) == 93
    assert SeniorityEvaluator.calculate_percentile(5.0) == 99


def test_track_weighting_difference():
    # In Backend track, CRAFT & OWNERSHIP weight more than in TECH_LEAD track
    backend_eval = SeniorityEvaluator(track=Track.BACKEND)
    lead_eval = SeniorityEvaluator(track=Track.TECH_LEAD)

    # High leadership (5.0), low craft (2.0)
    skewed_answers = {}
    for q in QUESTIONS:
        if q.dimension == DimensionId.LEADERSHIP:
            skewed_answers[q.id] = 5.0
        elif q.dimension == DimensionId.CRAFT:
            skewed_answers[q.id] = 2.0
        else:
            skewed_answers[q.id] = 3.0

    backend_res = backend_eval.evaluate_answers(skewed_answers)
    lead_res = lead_eval.evaluate_answers(skewed_answers)

    # Tech lead track should score higher because leadership has 30% weight vs 10%
    assert lead_res.overall_score > backend_res.overall_score
