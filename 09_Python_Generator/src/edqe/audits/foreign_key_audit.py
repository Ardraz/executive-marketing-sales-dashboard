"""
Enterprise Data Quality Engine (EDQE)

Foreign Key Audit
"""

from __future__ import annotations

import pandas as pd

from edqe.audit_result import AuditResult
from edqe.audit_rules import TABLE_RULES

from .base_audit import BaseAudit


class ForeignKeyAudit(BaseAudit):
    """
    Validate referential integrity between fact tables
    and dimension tables.
    """

    NAME = "Foreign Key Audit"

    MAXIMUM_SCORE = 20.0

    SAMPLE_LIMIT = 5

    def execute(
        self,
        dataframes: dict[str, pd.DataFrame],
    ) -> AuditResult:

        errors: list[str] = []

        warnings: list[str] = []

        total_relations = 0

        failed_relations = 0

        orphan_records = 0

        for child_table, rules in TABLE_RULES.items():

            foreign_keys = rules.get(
                "foreign_keys",
                {},
            )

            if not foreign_keys:
                continue

            child_df = dataframes.get(child_table)

            if child_df is None:

                warnings.append(f"{child_table} not found.")

                continue

            for fk_column, parent_table in foreign_keys.items():

                total_relations += 1

                parent_df = dataframes.get(parent_table)

                if parent_df is None:

                    failed_relations += 1

                    errors.append(f"{parent_table} not found.")

                    continue

                if fk_column not in child_df.columns:

                    failed_relations += 1

                    errors.append(f"{child_table}.{fk_column} column not found.")

                    continue

                parent_pk = TABLE_RULES[parent_table]["primary_key"][0]

                if parent_pk not in parent_df.columns:

                    failed_relations += 1

                    errors.append(f"{parent_table}.{parent_pk} column not found.")

                    continue

                fk_values = child_df[fk_column]

                pk_values = set(parent_df[parent_pk])

                invalid_rows = child_df[~fk_values.isin(pk_values)]

                if invalid_rows.empty:
                    continue

                failed_relations += 1

                orphan_count = len(invalid_rows)

                orphan_records += orphan_count

                sample_values = (
                    invalid_rows[fk_column]
                    .drop_duplicates()
                    .head(self.SAMPLE_LIMIT)
                    .tolist()
                )

                errors.append(
                    f"{child_table}.{fk_column} -> "
                    f"{parent_table}.{parent_pk} : "
                    f"{orphan_count:,} orphan record(s). "
                    f"Examples: {sample_values}"
                )

        passed = failed_relations == 0

        score = self.MAXIMUM_SCORE if passed else 0.0

        if passed:

            message = f"All {total_relations} foreign key " "relationships are valid."

            recommendation = "No action required."

        else:

            message = (
                f"{failed_relations} relationship(s) failed. "
                f"{orphan_records:,} orphan record(s) detected."
            )

            recommendation = (
                "Correct invalid foreign key values before publishing data."
            )

        return AuditResult(
            name=self.NAME,
            passed=passed,
            score=score,
            maximum_score=self.MAXIMUM_SCORE,
            message=message,
            errors=errors,
            warnings=warnings,
            recommendation=recommendation,
        )
