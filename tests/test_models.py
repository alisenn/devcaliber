"""
Unit tests for LevelCraft models and schemas.
"""

from levelcraft.models import SeniorityLevel, DimensionId, Track


def test_seniority_level_properties():
    lvl = SeniorityLevel.L3
    assert lvl.code == "L3"
    assert "Senior Software Engineer" in lvl.title
    assert lvl.tier == 3


def test_seniority_level_from_score():
    assert SeniorityLevel.from_score(1.2) == SeniorityLevel.L1
    assert SeniorityLevel.from_score(2.3) == SeniorityLevel.L2
    assert SeniorityLevel.from_score(3.4) == SeniorityLevel.L3
    assert SeniorityLevel.from_score(4.2) == SeniorityLevel.L4
    assert SeniorityLevel.from_score(4.9) == SeniorityLevel.L5


def test_dimension_ids_exist():
    dims = [d.value for d in DimensionId]
    assert "craft" in dims
    assert "ownership" in dims
    assert "impact" in dims
    assert "leadership" in dims
    assert "autonomy" in dims


def test_track_enums():
    tracks = [t.value for t in Track]
    assert "general" in tracks
    assert "backend" in tracks
    assert "frontend" in tracks
    assert "devops" in tracks
    assert "tech_lead" in tracks
