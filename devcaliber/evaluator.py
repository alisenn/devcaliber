"""
Seniority Evaluator and Scoring Engine.
Computes multi-dimensional competencies, industry benchmark percentiles, and gap analysis roadmaps.
"""

from datetime import datetime
from typing import Dict, List, Optional
from devcaliber.models import (
    AssessmentResult,
    DimensionId,
    DimensionScore,
    GapRecommendation,
    ActionItem,
    SeniorityLevel,
    Track,
    Question,
)
from devcaliber.matrix import (
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
        """Map a score (1.0 - 5.0) to an *estimated* percentile.

        NOTE: this is a hand-tuned curve, not calibrated against collected response
        data. Treat it as a rough indication only.
        """
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
        confidence, notes = self._assess_reliability(dim_scores_accumulator)
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
            confidence=confidence,
            notes=notes,
        )

    @staticmethod
    def _assess_reliability(
        per_dim: Dict[DimensionId, List[float]],
    ) -> tuple:
        """Derive result confidence and calibration notes from the raw answers."""
        counts = [len(v) for v in per_dim.values()]
        min_n = min(counts)
        confidence = "low" if min_n <= 1 else "medium" if min_n <= 4 else "high"

        notes: List[str] = []
        all_scores = [s for v in per_dim.values() for s in v]
        if len(all_scores) >= 10 and all(s >= 4.5 for s in all_scores):
            notes.append(
                "Every answer was top-tier. Self-assessment tends to run high; "
                "validate with peer or manager feedback."
            )
        for dim_id, scores in per_dim.items():
            if len(scores) >= 3 and max(scores) - min(scores) >= 3.0:
                name = DIMENSION_METADATA[dim_id]["name"]
                notes.append(
                    f"{name}: answers were inconsistent (range {min(scores):.1f}-{max(scores):.1f}); "
                    "the dimension score is less reliable."
                )
        return confidence, notes

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


class AdaptiveAssessmentEngine:
    """
    Computerized Adaptive Testing (CAT) Engine for Software Engineering Seniority.
    Dynamically adjusts question difficulty on a step-by-step basis depending on the
    candidate's answer to the immediate previous question.
    """

    def __init__(self, track: Track = Track.GENERAL, questions: Optional[List[Question]] = None):
        self.track = track
        self.questions = questions or QUESTIONS
        self.answered: Dict[str, float] = {}
        self.history: List[Dict[str, any]] = []
        self.current_difficulty: int = 2  # Baseline starting difficulty

    def record_answer(self, question: Question, score: float):
        """Records an answer and logs it in the progression history."""
        self.answered[question.id] = score
        self.history.append({
            "question_id": question.id,
            "dimension": question.dimension,
            "difficulty": question.difficulty,
            "score": score,
        })

    def get_next_question(
        self,
        dimension: Optional[DimensionId] = None,
        is_quick: bool = False,
    ) -> Optional[tuple]:
        """
        Determines the next question based on the previous question's performance:
        - If previous score >= 4.0: Difficulty scales UP (+1, max 5).
        - If previous score <= 2.0: Difficulty scales DOWN (-1, min 1).
        - If previous score between 2.1 and 3.9: Difficulty remains balanced.
        Returns: (Question, adaptation_message) or None if no questions left.
        """
        candidates = [
            q for q in self.questions
            if q.id not in self.answered and (dimension is None or q.dimension == dimension) and (not is_quick or q.is_quick)
        ]
        if not candidates:
            return None

        # Check last answer to dynamically adjust difficulty
        if not self.history:
            self.current_difficulty = 2
            adaptation_msg = "Initial Baseline Calibration (Difficulty: Tier 2 - Mid)"
        else:
            last_entry = self.history[-1]
            last_score = last_entry["score"]

            if last_score >= 4.0:
                self.current_difficulty = min(5, self.current_difficulty + 1)
                adaptation_msg = f"📈 Difficulty Increased to Tier {self.current_difficulty} (Previous answer demonstrated Staff+ competency)"
            elif last_score <= 2.0:
                self.current_difficulty = max(1, self.current_difficulty - 1)
                adaptation_msg = f"📉 Difficulty Adjusted to Tier {self.current_difficulty} (Previous answer indicated foundational tier; probing baseline)"
            else:
                adaptation_msg = f"⚖️ Maintained at Tier {self.current_difficulty} (Previous answer showed solid Senior proficiency)"

        # Sort available candidates by proximity to current adapted difficulty
        candidates.sort(key=lambda q: (abs(q.difficulty - self.current_difficulty), -q.difficulty))
        chosen = candidates[0]
        return chosen, adaptation_msg
