"""
Enterprise Data Quality Engine (EDQE)

Recommendation Engine
"""

from __future__ import annotations

from dataclasses import dataclass

from edqe.audit_session import AuditSession


@dataclass(frozen=True)
class Recommendation:

    title: str
    level: str
    color: str
    summary: str
    action: str


class RecommendationEngine:
    """
    Generate executive recommendation
    based on AuditSession.
    """

    @staticmethod
    def generate(
        session: AuditSession,
    ) -> Recommendation:

        score = session.success_rate

        if score >= 99:

            return Recommendation(
                title="Excellent Data Quality",
                level="SUCCESS",
                color="success",
                summary=(
                    "All audit rules passed successfully. "
                    "The generated dataset is ready for downstream analytics."
                ),
                action=(
                    "Dataset can be published to the analytical layer "
                    "without additional validation."
                ),
            )

        if score >= 95:

            return Recommendation(
                title="Very Good Data Quality",
                level="GOOD",
                color="primary",
                summary=(
                    "Minor quality issues were detected "
                    "but they do not significantly affect reporting."
                ),
                action=(
                    "Review warning items and continue monitoring " "future executions."
                ),
            )

        if score >= 90:

            return Recommendation(
                title="Good Data Quality",
                level="WARNING",
                color="warning",
                summary=("Some audit rules require attention."),
                action=("Investigate failed validations before " "publishing data."),
            )

        if score >= 80:

            return Recommendation(
                title="Needs Improvement",
                level="WARNING",
                color="warning",
                summary=("Multiple audit failures were detected."),
                action=("Correct data quality issues and rerun EDQE."),
            )

        return Recommendation(
            title="Critical Data Quality Issue",
            level="CRITICAL",
            color="danger",
            summary=("Dataset contains significant quality problems."),
            action=(
                "Do not publish this dataset until all critical " "issues are resolved."
            ),
        )
