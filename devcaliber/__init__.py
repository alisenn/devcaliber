"""
DevCaliber: The Open Source Seniority & Competency Benchmark Suite for Software Engineers.
Adaptive 1-Hour Diagnostic Examination & System Design Evaluator.
"""

__version__ = "2.0.0"
__author__ = "DevCaliber Contributors"

from devcaliber.models import SeniorityLevel, DimensionId, AssessmentResult
from devcaliber.evaluator import SeniorityEvaluator, AdaptiveAssessmentEngine

__all__ = [
    "SeniorityLevel",
    "DimensionId",
    "AssessmentResult",
    "SeniorityEvaluator",
    "AdaptiveAssessmentEngine",
    "__version__",
]
