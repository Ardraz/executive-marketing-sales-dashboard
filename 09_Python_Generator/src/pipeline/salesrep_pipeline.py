"""
Sales Representative Pipeline
"""

from generators.salesrep_generator import generate_sales_reps

from validators.validator import validate_dataframe


def run_salesrep_pipeline():
    """
    Generate and validate Sales Representative Dimension.

    Export is handled after the Enterprise Data Quality Engine (EDQE)
    successfully validates the complete dataset.
    """

    sales_reps = generate_sales_reps()

    validate_dataframe(
        sales_reps,
        "Dim_SalesRep",
    )

    return sales_reps
