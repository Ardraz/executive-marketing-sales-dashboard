"""
Date Dimension Pipeline
"""

from core.date_dimension import generate_calendar

from validators.validator import validate_dataframe


def run_date_pipeline():
    """
    Generate and validate Date Dimension.

    Export is handled after the Enterprise Data Quality Engine (EDQE)
    successfully validates the complete dataset.
    """

    calendar = generate_calendar()

    validate_dataframe(
        calendar,
        "Dim_Date",
    )

    return calendar
