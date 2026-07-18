"""
Enterprise Data Quality Engine (EDQE)

Audit Result Model
"""

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class AuditResult:
    """
    Represents the result of one audit execution.
    """

    name: str

    passed: bool

    score: float

    maximum_score: float

    duration: float = 0.0

    message: str = ""

    errors: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    recommendation: str = ""

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)

    @property
    def percentage(self) -> float:

        if self.maximum_score == 0:
            return 0.0

        return self.score / self.maximum_score * 100

    def __str__(self) -> str:

        status = "PASS" if self.passed else "FAIL"

        return (
            f"{self.name} | "
            f"{status} | "
            f"{self.score:.1f}/{self.maximum_score:.1f}"
        )
