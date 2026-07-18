"""
Enterprise Data Quality Engine (EDQE)

Audit Session
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime

from edqe.audit_score import AuditScore


@dataclass
class AuditSession:
    """
    Represents one complete EDQE execution session.
    """

    project_name: str = "Executive Marketing & Sales Dashboard"

    engine_name: str = "Enterprise Data Quality Engine"

    engine_version: str = "1.0.0"

    started_at: datetime = field(default_factory=datetime.now)

    finished_at: datetime | None = None

    execution_time: float = 0.0

    dataframe_summary: dict[str, dict] = field(default_factory=dict)

    score: AuditScore = field(default_factory=AuditScore)

    # ==========================================================
    # DataFrame Statistics
    # ==========================================================

    @property
    def total_tables(self) -> int:
        return len(self.dataframe_summary)

    @property
    def total_rows(self) -> int:
        return sum(info["rows"] for info in self.dataframe_summary.values())

    @property
    def total_columns(self) -> int:
        return sum(info["columns"] for info in self.dataframe_summary.values())

    @property
    def total_memory_mb(self) -> float:
        return round(
            sum(info["memory_mb"] for info in self.dataframe_summary.values()),
            2,
        )

    # ==========================================================
    # Audit Statistics
    # ==========================================================

    @property
    def total_audits(self) -> int:
        return len(self.score.results)

    @property
    def passed_audits(self) -> int:
        return sum(1 for result in self.score.results if result.passed)

    @property
    def failed_audits(self) -> int:
        return sum(1 for result in self.score.results if not result.passed)

    @property
    def total_errors(self) -> int:
        return sum(result.error_count for result in self.score.results)

    @property
    def total_warnings(self) -> int:
        return sum(result.warning_count for result in self.score.results)

    @property
    def success_rate(self) -> float:

        if self.total_audits == 0:
            return 0.0

        return round(
            (self.passed_audits / self.total_audits) * 100,
            2,
        )

    # ==========================================================
    # Execution
    # ==========================================================

    def finish(self) -> None:
        """
        Mark session as completed.
        """

        self.finished_at = datetime.now()

    # ==========================================================
    # Formatting Helpers
    # ==========================================================

    @property
    def started_at_text(self) -> str:

        return self.started_at.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def finished_at_text(self) -> str:

        if self.finished_at is None:
            return "-"

        return self.finished_at.strftime("%Y-%m-%d %H:%M:%S")

    @property
    def execution_time_text(self) -> str:
        return f"{self.execution_time:.3f} sec"
