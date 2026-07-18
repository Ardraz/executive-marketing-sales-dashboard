"""
Enterprise Data Quality Engine (EDQE)

Base Report Builder
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from edqe.audit_score import AuditScore


class ReportBuilder(ABC):
    """
    Base class for all report builders.
    """

    @abstractmethod
    def build(
        self,
        score: AuditScore,
    ) -> None:
        """
        Build report.
        """
        raise NotImplementedError
