"""
Enterprise Data Quality Engine (EDQE)

Missing Value Audit
"""

import pandas as pd

from edqe.audit_result import AuditResult

from .base_audit import BaseAudit


class MissingValueAudit(BaseAudit):
    """
    Checks every DataFrame for missing values.
    """

    NAME = "Missing Value Audit"

    MAXIMUM_SCORE = 15.0

    def execute(
        self,
        dataframes: dict[str, pd.DataFrame],
    ) -> AuditResult:

        errors: list[str] = []

        checked_columns = 0

        total_missing = 0

        for table_name, dataframe in dataframes.items():

            for column in dataframe.columns:

                checked_columns += 1

                missing = int(dataframe[column].isna().sum())

                if missing > 0:

                    total_missing += missing

                    errors.append(
                        f"{table_name}.{column} : " f"{missing:,} missing value(s)"
                    )

        passed = total_missing == 0

        score = self.MAXIMUM_SCORE if passed else 0.0

        if passed:

            message = (
                f"No missing values detected " f"({checked_columns:,} columns checked)."
            )

            recommendation = "No action required."

        else:

            message = (
                f"{total_missing:,} missing value(s) "
                f"found across {len(errors)} column(s)."
            )

            recommendation = (
                "Review the affected columns and " "complete the missing values."
            )

        return AuditResult(
            name=self.NAME,
            passed=passed,
            score=score,
            maximum_score=self.MAXIMUM_SCORE,
            message=message,
            errors=errors,
            recommendation=recommendation,
        )
