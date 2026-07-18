"""
Enterprise Data Quality Engine (EDQE)

Duplicate Primary Key Audit
"""

import pandas as pd

from edqe.audit_result import AuditResult
from edqe.audit_rules import TABLE_RULES

from .base_audit import BaseAudit


class DuplicateAudit(BaseAudit):
    """
    Checks duplicate primary key values for every configured table.
    """

    NAME = "Duplicate Primary Key Audit"

    MAXIMUM_SCORE = 15.0

    def execute(
        self,
        dataframes: dict[str, pd.DataFrame],
    ) -> AuditResult:

        errors: list[str] = []

        checked_tables = 0

        total_duplicate_records = 0

        for table_name, rules in TABLE_RULES.items():

            dataframe = dataframes.get(table_name)

            if dataframe is None:
                continue

            checked_tables += 1

            primary_keys = rules["primary_key"]

            duplicated = dataframe.duplicated(
                subset=primary_keys,
                keep=False,
            )

            duplicate_count = int(duplicated.sum())

            if duplicate_count > 0:

                total_duplicate_records += duplicate_count

                errors.append(
                    f"{table_name}"
                    f" ({', '.join(primary_keys)}) : "
                    f"{duplicate_count:,} duplicate record(s)"
                )

        passed = total_duplicate_records == 0

        score = self.MAXIMUM_SCORE if passed else 0.0

        if passed:

            message = (
                f"No duplicate primary keys detected "
                f"({checked_tables} tables checked)."
            )

            recommendation = "No action required."

        else:

            message = (
                f"{total_duplicate_records:,} duplicate "
                f"primary key record(s) detected."
            )

            recommendation = "Primary key values must be unique."

        return AuditResult(
            name=self.NAME,
            passed=passed,
            score=score,
            maximum_score=self.MAXIMUM_SCORE,
            message=message,
            errors=errors,
            recommendation=recommendation,
        )
