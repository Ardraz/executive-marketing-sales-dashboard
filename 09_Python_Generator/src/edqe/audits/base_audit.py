"""
Enterprise Data Quality Engine (EDQE)

Base Audit Class
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from time import perf_counter

import pandas as pd

from edqe.audit_result import AuditResult


class BaseAudit(ABC):
    """
    Base class for all EDQE audits.
    """

    NAME = "Base Audit"

    MAXIMUM_SCORE = 0.0

    def run(
        self,
        dataframes: dict[str, pd.DataFrame],
    ) -> AuditResult:
        """
        Execute the audit and measure execution time.
        """

        start = perf_counter()

        result = self.execute(dataframes)

        result.duration = perf_counter() - start

        return result

    @abstractmethod
    def execute(
        self,
        dataframes: dict[str, pd.DataFrame],
    ) -> AuditResult:
        """
        Audit implementation.
        """
        raise NotImplementedError
