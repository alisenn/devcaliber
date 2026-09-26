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
    assert len(QUESTIONS) == 30  # 30 comprehensive scenario questions (6 per dimension)
    for q in QUESTIONS:
        assert q.id
        assert q.dimension in DimensionId
        assert len(q.options) >= 3
        # Ensure scores are ordered or within 1.0 - 5.0
        for opt in q.options:
            assert 1.0 <= opt.score <= 5.0
            assert opt.level_indicator in SeniorityLevel


def test_each_dimension_has_six_questions():
    dim_counts = {d: 0 for d in DimensionId}
    for q in QUESTIONS:
        dim_counts[q.dimension] += 1
    for dim, count in dim_counts.items():
        assert count == 6, f"Dimension {dim} should have 6 questions, got {count}"


def test_growth_roadmap_entries():
    for dim in DimensionId:
        assert dim in GROWTH_ROADMAP
        for target_lvl in [SeniorityLevel.L2, SeniorityLevel.L3, SeniorityLevel.L4, SeniorityLevel.L5]:
            assert target_lvl in GROWTH_ROADMAP[dim]
            assert len(GROWTH_ROADMAP[dim][target_lvl]) > 0
