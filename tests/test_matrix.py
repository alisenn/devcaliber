"""
Unit tests for competency matrix and question bank.
"""

from devcaliber.models import DimensionId, SeniorityLevel
from devcaliber.matrix import DIMENSION_METADATA, LEVEL_RUBRIC, QUESTIONS, GROWTH_ROADMAP


def test_matrix_covers_all_dimensions():
    for dim in DimensionId:
        assert dim in DIMENSION_METADATA
        assert "name" in DIMENSION_METADATA[dim]
        assert "description" in DIMENSION_METADATA[dim]


def test_level_rubrics_cover_all_levels():
    for dim in DimensionId:
        assert dim in LEVEL_RUBRIC
        for lvl in SeniorityLevel:
            assert lvl in LEVEL_RUBRIC[dim]
            assert len(LEVEL_RUBRIC[dim][lvl]) > 10


def test_questions_have_valid_structure():
    assert len(QUESTIONS) == 60  # 12 per dimension
    for q in QUESTIONS:
        assert q.id
        assert q.dimension in DimensionId
        assert len(q.options) >= 3
        # Ensure scores are ordered or within 1.0 - 5.0
        for opt in q.options:
            assert 1.0 <= opt.score <= 5.0
            assert opt.level_indicator in SeniorityLevel


def test_each_dimension_has_twelve_questions():
    dim_counts = {d: 0 for d in DimensionId}
    for q in QUESTIONS:
        dim_counts[q.dimension] += 1
    for dim, count in dim_counts.items():
        assert count == 12, f"Dimension {dim} should have 12 questions, got {count}"


def test_growth_roadmap_entries():
    for dim in DimensionId:
        assert dim in GROWTH_ROADMAP
        for target_lvl in [SeniorityLevel.L2, SeniorityLevel.L3, SeniorityLevel.L4, SeniorityLevel.L5]:
            assert target_lvl in GROWTH_ROADMAP[dim]
            assert len(GROWTH_ROADMAP[dim][target_lvl]) > 0


def test_question_and_option_ids_are_unique():
    q_ids = [q.id for q in QUESTIONS]
    assert len(q_ids) == len(set(q_ids))
    o_ids = [o.id for q in QUESTIONS for o in q.options]
    assert len(o_ids) == len(set(o_ids))


def test_every_question_is_translated():
    for q in QUESTIONS:
        assert q.title_tr and q.scenario_tr, f"{q.id} is missing a Turkish title/scenario"
        for o in q.options:
            assert o.text_tr, f"{o.id} is missing Turkish text"


def test_option_scores_are_distinct_and_match_level_indicator():
    for q in QUESTIONS:
        scores = [o.score for o in q.options]
        assert len(scores) == len(set(scores)), f"{q.id} has duplicate option scores"
        for o in q.options:
            assert round(o.score) >= o.level_indicator.tier - 1
            assert round(o.score) <= o.level_indicator.tier + 1


def test_each_dimension_covers_a_wide_difficulty_range():
    for dim in DimensionId:
        diffs = {q.difficulty for q in QUESTIONS if q.dimension == dim}
        assert min(diffs) <= 2 and max(diffs) >= 4, f"{dim} difficulty range too narrow: {diffs}"
