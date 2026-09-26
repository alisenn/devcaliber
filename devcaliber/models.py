"""
Data models and schemas for LevelCraft.
"""

from enum import Enum
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class SeniorityLevel(str, Enum):
    L1 = "L1 - Associate / Junior Engineer"
    L2 = "L2 - Software Engineer (Mid)"
    L3 = "L3 - Senior Software Engineer"
    L4 = "L4 - Staff Software Engineer"
    L5 = "L5 - Principal / Distinguished Engineer"

    @property
    def code(self) -> str:
        return self.value.split(" - ")[0]

    @property
    def title(self) -> str:
        return self.value.split(" - ")[1]

    @property
    def tier(self) -> int:
        return int(self.code.replace("L", ""))

    @classmethod
    def from_score(cls, score: float) -> "SeniorityLevel":
        if score < 1.8:
            return cls.L1
        elif score < 2.8:
            return cls.L2
        elif score < 3.8:
            return cls.L3
        elif score < 4.6:
            return cls.L4
        else:
            return cls.L5


class DimensionId(str, Enum):
    CRAFT = "craft"
    OWNERSHIP = "ownership"
    IMPACT = "impact"
    LEADERSHIP = "leadership"
    AUTONOMY = "autonomy"


class Track(str, Enum):
    GENERAL = "general"
    BACKEND = "backend"
    FRONTEND = "frontend"
    DEVOPS = "devops"
    TECH_LEAD = "tech_lead"


class QuestionOption(BaseModel):
    id: str
    text: str
    text_tr: Optional[str] = None
    score: float
    description: Optional[str] = None
    level_indicator: SeniorityLevel


class Question(BaseModel):
    id: str
    dimension: DimensionId
    title: str
    scenario: str
    title_tr: Optional[str] = None
    scenario_tr: Optional[str] = None
    options: List[QuestionOption]
    is_quick: bool = False
    difficulty: int = 3  # 1 (Junior) to 5 (Principal/Staff)
    question_type: str = "scenario"  # "scenario", "system_design", "architecture_tradeoff"
    interview_source: Optional[str] = None
    track: Track = Track.GENERAL


class DimensionScore(BaseModel):
    dimension_id: DimensionId
    dimension_name: str
    score: float
    level: SeniorityLevel
    percentile: int
    strengths: List[str] = Field(default_factory=list)
    growth_areas: List[str] = Field(default_factory=list)


class ActionItem(BaseModel):
    title: str
    description: str
    impact: str


class GapRecommendation(BaseModel):
    dimension_name: str
    current_score: float
    target_score: float
    action_items: List[ActionItem]
    recommended_reading: List[str]


class AssessmentResult(BaseModel):
    candidate_name: str = "Engineer"
    track: Track = Track.GENERAL
    overall_level: SeniorityLevel
    overall_score: float
    total_questions: int
    dimension_scores: Dict[DimensionId, DimensionScore]
    gap_recommendations: List[GapRecommendation]
    timestamp: str
    assessment_mode: str = "interactive"
