"""
Enterprise Data Quality Engine (EDQE)

Audit Score Model
"""

from dataclasses import dataclass, field

from .audit_result import AuditResult


@dataclass(slots=True)
class AuditScore:
    """
    Represents the final score of all audits.
    """

    results: list[AuditResult] = field(default_factory=list)

    @property
    def total_score(self) -> float:
        return sum(result.score for result in self.results)

    @property
    def maximum_score(self) -> float:
        return sum(result.maximum_score for result in self.results)

    @property
    def percentage(self) -> float:

        if self.maximum_score == 0:
            return 0.0

        return self.total_score / self.maximum_score * 100

    @property
    def passed(self) -> bool:
        return all(result.passed for result in self.results)

    @property
    def grade(self) -> str:

        score = self.percentage

        if score >= 98:
            return "A+"

        if score >= 95:
            return "A"

        if score >= 90:
            return "B"

        if score >= 80:
            return "C"

        return "F"

    @property
    def status(self) -> str:

        if self.percentage >= 95:
            return "READY FOR ANALYTICS"

        if self.percentage >= 80:
            return "NEEDS IMPROVEMENT"

        return "FAILED"

    def add_result(
        self,
        result: AuditResult,
    ) -> None:

        self.results.append(result)
