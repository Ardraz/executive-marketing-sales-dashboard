"""
Enterprise Data Quality Engine (EDQE)

Console Report
"""

from __future__ import annotations

from edqe.audit_score import AuditScore

from .report_builder import ReportBuilder


class ConsoleReport(ReportBuilder):
    """
    Print audit results to console.
    """

    def build(
        self,
        score: AuditScore,
    ) -> None:

        print()

        print("=" * 60)
        print("ENTERPRISE DATA QUALITY ENGINE")
        print("=" * 60)

        print()

        print("AUDIT RESULTS")

        print("-" * 60)

        for result in score.results:

            status = "PASS" if result.passed else "FAIL"

            print(f"[{status}] {result.name}")

            print(f"  {result.message}")

            if result.errors:

                print()

                print("  Errors:")

                for error in result.errors:

                    print(f"    - {error}")

            if result.warnings:

                print()

                print("  Warnings:")

                for warning in result.warnings:

                    print(f"    - {warning}")

            if result.recommendation:

                print()

                print(f"  Recommendation: " f"{result.recommendation}")

            print()

        print("-" * 60)

        print("SUMMARY")

        print("-" * 60)

        print(
            f"Score      : "
            f"{score.total_score:.1f}"
            f"/"
            f"{score.maximum_score:.1f}"
        )

        print(f"Percentage : " f"{score.percentage:.2f}%")

        print(f"Grade      : " f"{score.grade}")

        print(f"Status     : " f"{score.status}")

        print()

        print("=" * 60)
        print("END OF REPORT")
        print("=" * 60)
