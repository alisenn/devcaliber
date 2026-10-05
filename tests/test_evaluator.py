"""
Unit tests for the DevCaliber seniority evaluator and adaptive CAT engine.
"""

from devcaliber.models import SeniorityLevel, DimensionId, Track
from devcaliber.evaluator import SeniorityEvaluator, AdaptiveAssessmentEngine
from devcaliber.matrix import QUESTIONS


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
    backend_eval = SeniorityEvaluator(track=Track.BACKEND)
    lead_eval = SeniorityEvaluator(track=Track.TECH_LEAD)

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

    assert lead_res.overall_score > backend_res.overall_score


def test_adaptive_engine_difficulty_scaling_up():
    engine = AdaptiveAssessmentEngine()

    # Initial question
    q1, msg1 = engine.get_next_question(dimension=DimensionId.CRAFT)
    assert q1 is not None
    assert "Initial" in msg1

    # Candidate provides Staff/Principal answer (score 5.0)
    engine.record_answer(q1, 5.0)

    # Next question should adapt UP in difficulty
    q2, msg2 = engine.get_next_question(dimension=DimensionId.CRAFT)
    assert q2 is not None
    assert "Increased" in msg2
    assert q2.difficulty >= q1.difficulty


def test_adaptive_engine_difficulty_scaling_down():
    engine = AdaptiveAssessmentEngine()

    q1, _ = engine.get_next_question(dimension=DimensionId.CRAFT)
    # Candidate provides Junior answer (score 1.0)
    engine.record_answer(q1, 1.0)

    # Next question should adapt DOWN in difficulty
    q2, msg2 = engine.get_next_question(dimension=DimensionId.CRAFT)
    assert q2 is not None
    assert "Adjusted" in msg2
    assert engine.current_difficulty <= 2


def test_confidence_scales_with_questions_per_dimension():
    evaluator = SeniorityEvaluator()
    pulse = {q.id: 3.0 for q in QUESTIONS if q.is_quick}
    sprint = {q.id: 3.0 for q in QUESTIONS if q.sprint}
    assert evaluator.evaluate_answers(pulse).confidence == "low"
    assert evaluator.evaluate_answers(sprint).confidence == "medium"
    assert evaluator.evaluate_answers({q.id: 3.0 for q in QUESTIONS}).confidence == "high"


def test_all_top_answers_trigger_calibration_note():
    result = SeniorityEvaluator().evaluate_answers({q.id: 5.0 for q in QUESTIONS})
    assert any("top-tier" in n for n in result.notes)


def test_inconsistent_dimension_is_flagged():
    answers = {q.id: 3.0 for q in QUESTIONS}
    craft = [q for q in QUESTIONS if q.dimension == DimensionId.CRAFT]
    answers[craft[0].id] = 1.0
    answers[craft[1].id] = 4.5
    result = SeniorityEvaluator().evaluate_answers(answers)
    assert any("inconsistent" in n for n in result.notes)
