"""
LevelCraft: The Open Source Seniority & Competency Benchmark Engine for Software Engineers.
"""

__version__ = "1.0.0"
__author__ = "LevelCraft Contributors"

from levelcraft.models import SeniorityLevel, DimensionId, AssessmentResult
from levelcraft.evaluator import SeniorityEvaluator

__all__ = [
    "SeniorityLevel",
    "DimensionId",
    "AssessmentResult",
    "SeniorityEvaluator",
    "__version__",
]
