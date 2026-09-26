"""
SeniorMeter: The Open Source Seniority & Competency Benchmark Suite for Software Engineers.
Comprehensive 1-Hour Diagnostic & Career Matrix Engine.
"""

__version__ = "2.0.0"
__author__ = "SeniorMeter Contributors"

from seniormeter.models import SeniorityLevel, DimensionId, AssessmentResult
from seniormeter.evaluator import SeniorityEvaluator

__all__ = [
    "SeniorityLevel",
    "DimensionId",
    "AssessmentResult",
    "SeniorityEvaluator",
    "__version__",
]
