"""
Customer Dimension Pipeline
"""

from generators.customer_generator import generate_customers

from validators.validator import validate_dataframe


def run_customer_pipeline():
    """
    Generate and validate Customer Dimension.

    Export is handled after the Enterprise Data Quality Engine (EDQE)
    successfully validates the complete dataset.
    """

    customers = generate_customers()

    validate_dataframe(
        customers,
        "Dim_Customer",
    )

    return customers
