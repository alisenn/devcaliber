"""
Seniority Evaluator and Scoring Engine.
Computes multi-dimensional competencies, industry benchmark percentiles, and gap analysis roadmaps.
"""

from datetime import datetime
from typing import Dict, List, Optional
from seniormeter.models import (
    AssessmentResult,
    DimensionId,
    DimensionScore,
    GapRecommendation,
    ActionItem,
    SeniorityLevel,
    Track,
)
from seniormeter.matrix import (
    DIMENSION_METADATA,
    GROWTH_ROADMAP,
    QUESTIONS,
)

# Track-specific dimension weighting
TRACK_WEIGHTS: Dict[Track, Dict[DimensionId, float]] = {
    Track.GENERAL: {
        DimensionId.CRAFT: 0.25,
        DimensionId.OWNERSHIP: 0.20,
        DimensionId.IMPACT: 0.20,
        DimensionId.LEADERSHIP: 0.15,
        DimensionId.AUTONOMY: 0.20,
    },
    Track.BACKEND: {
        DimensionId.CRAFT: 0.30,
        DimensionId.OWNERSHIP: 0.25,
        DimensionId.IMPACT: 0.15,
        DimensionId.LEADERSHIP: 0.10,
        DimensionId.AUTONOMY: 0.20,
    },
    Track.FRONTEND: {
        DimensionId.CRAFT: 0.30,
        DimensionId.IMPACT: 0.25,
        DimensionId.AUTONOMY: 0.20,
        DimensionId.OWNERSHIP: 0.15,
        DimensionId.LEADERSHIP: 0.10,
    },
    Track.DEVOPS: {
        DimensionId.OWNERSHIP: 0.35,
        DimensionId.CRAFT: 0.25,
        DimensionId.AUTONOMY: 0.20,
        DimensionId.IMPACT: 0.10,
        DimensionId.LEADERSHIP: 0.10,
    },
    Track.TECH_LEAD: {
        DimensionId.LEADERSHIP: 0.30,
        DimensionId.IMPACT: 0.25,
        DimensionId.AUTONOMY: 0.20,
        DimensionId.CRAFT: 0.15,
        DimensionId.OWNERSHIP: 0.10,
    },
}


class SeniorityEvaluator:
    """Evaluates question answers and generates detailed seniority diagnostics."""

    def __init__(self, track: Track = Track.GENERAL):
        self.track = track
        self.weights = TRACK_WEIGHTS.get(track, TRACK_WEIGHTS[Track.GENERAL])

    @staticmethod
    def calculate_percentile(score: float) -> int:
        """Map a score (1.0 - 5.0) to an industry percentile distribution."""
        # Empirical CDF curve calibrated to tech industry demographics
        # L1 (1.0-1.8): 5-25th percentile
        # L2 (1.8-2.8): 25-60th percentile
        # L3 (2.8-3.8): 60-85th percentile
        # L4 (3.8-4.6): 85-96th percentile
        # L5 (4.6-5.0): 96-99th percentile
        if score <= 1.0:
            return 5
        elif score <= 2.0:
            return int(5 + (score - 1.0) * 30)
        elif score <= 3.0:
            return int(35 + (score - 2.0) * 35)
        elif score <= 4.0:
            return int(70 + (score - 3.0) * 18)
        elif score <= 4.8:
            return int(88 + (score - 4.0) * 10)
        else:
            return 99

    def evaluate_answers(
        self,
        answers: Dict[str, float],
        candidate_name: str = "Engineer",
        assessment_mode: str = "interactive",
    ) -> AssessmentResult:
        """
        Takes a mapping of question_id -> selected_option_score.
        Computes dimension scores, overall score, level, and gap analysis.
        """
        dim_scores_accumulator: Dict[DimensionId, List[float]] = {
            dim: [] for dim in DimensionId
        }

        # Map answers into dimensions
        for q in QUESTIONS:
            if q.id in answers:
                dim_scores_accumulator[q.dimension].append(answers[q.id])

        dimension_scores: Dict[DimensionId, DimensionScore] = {}
        weighted_sum = 0.0
        total_weight = 0.0

        for dim_id, scores in dim_scores_accumulator.items():
            if scores:
                avg_score = sum(scores) / len(scores)
            else:
                avg_score = 1.0  # default baseline

            level = SeniorityLevel.from_score(avg_score)
            percentile = self.calculate_percentile(avg_score)
            weight = self.weights.get(dim_id, 0.2)
            weighted_sum += avg_score * weight
            total_weight += weight

            # Strengths and growth areas
            strengths: List[str] = []
            growth_areas: List[str] = []
            if avg_score >= 3.5:
                strengths.append(f"Exemplary demonstration of {DIMENSION_METADATA[dim_id]['name']}.")
            else:
                growth_areas.append(f"Opportunity to advance {DIMENSION_METADATA[dim_id]['name']} to next tier.")

            dimension_scores[dim_id] = DimensionScore(
                dimension_id=dim_id,
                dimension_name=DIMENSION_METADATA[dim_id]["name"],
                score=round(avg_score, 2),
                level=level,
                percentile=percentile,
                strengths=strengths,
                growth_areas=growth_areas,
            )

        overall_score = round(weighted_sum / (total_weight or 1.0), 2)
        overall_level = SeniorityLevel.from_score(overall_score)

        # Generate Gap Analysis & Roadmap to next level
        gap_recommendations = self._generate_gap_roadmap(dimension_scores, overall_level)

        return AssessmentResult(
            candidate_name=candidate_name,
            track=self.track,
            overall_level=overall_level,
            overall_score=overall_score,
            total_questions=len(answers),
            dimension_scores=dimension_scores,
            gap_recommendations=gap_recommendations,
            timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            assessment_mode=assessment_mode,
        )

    def _generate_gap_roadmap(
        self,
        dimension_scores: Dict[DimensionId, DimensionScore],
        current_level: SeniorityLevel,
    ) -> List[GapRecommendation]:
        """Generates targeted action items and suggested books for progression."""
        target_tier = min(current_level.tier + 1, 5)
        target_level_enum = SeniorityLevel(f"L{target_tier} - " + {
            1: "Associate / Junior Engineer",
            2: "Software Engineer (Mid)",
            3: "Senior Software Engineer",
            4: "Staff Software Engineer",
            5: "Principal / Distinguished Engineer"
        }[target_tier])

        recommendations: List[GapRecommendation] = []

        for dim_id, dim_score in dimension_scores.items():
            # Get roadmap recommendations for target level
            roadmap_items = GROWTH_ROADMAP.get(dim_id, {}).get(target_level_enum, [])
            action_items: List[ActionItem] = []
            reading_list: List[str] = []

            for item in roadmap_items:
                action_items.append(
                    ActionItem(
                        title=item["title"],
                        description=item["action"],
                        impact=f"Propels {DIMENSION_METADATA[dim_id]['name']} toward {target_level_enum.code}",
                    )
                )
                if "reading" in item and item["reading"] not in reading_list:
                    reading_list.append(item["reading"])

            recommendations.append(
                GapRecommendation(
                    dimension_name=DIMENSION_METADATA[dim_id]["name"],
                    current_score=dim_score.score,
                    target_score=float(target_tier),
                    action_items=action_items,
                    recommended_reading=reading_list,
                )
            )

        return recommendations
