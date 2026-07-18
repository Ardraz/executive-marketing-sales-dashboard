"""
Enterprise Data Quality Engine (EDQE)

Audit Runner
"""

from __future__ import annotations

from time import perf_counter

from edqe.audit_session import AuditSession
from edqe.audits.duplicate_audit import DuplicateAudit
from edqe.audits.foreign_key_audit import ForeignKeyAudit
from edqe.audits.missing_value_audit import MissingValueAudit


class AuditRunner:
    """
    Execute all EDQE audits and return an AuditSession.
    """

    def __init__(
        self,
        dataframes: dict,
    ) -> None:

        self.dataframes = dataframes

        self.audits = [
            MissingValueAudit(),
            DuplicateAudit(),
            ForeignKeyAudit(),
        ]

    def run(self) -> AuditSession:

        session = AuditSession()

        session.dataframe_summary = {}

        for table_name, dataframe in self.dataframes.items():

            memory_mb = dataframe.memory_usage(deep=True).sum() / 1024 / 1024

            session.dataframe_summary[table_name] = {
                "rows": len(dataframe),
                "columns": len(dataframe.columns),
                "memory_mb": round(
                    memory_mb,
                    2,
                ),
            }

        start = perf_counter()

        for audit in self.audits:

            result = audit.run(self.dataframes)

            session.score.add_result(result)

        session.execution_time = perf_counter() - start

        session.finish()

        return session


def run_all_audits(
    dataframes: dict,
) -> AuditSession:
    """
    Convenience function.
    """

    runner = AuditRunner(dataframes)

    return runner.run()
