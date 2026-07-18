"""
Sales Fact Pipeline
"""

from generators.sales_generator import generate_sales

from validators.validator import validate_dataframe


def run_sales_pipeline(
    calendar,
    leads,
    products,
):
    """
    Generate and validate Sales Fact Table.

    Export is handled after the Enterprise Data Quality Engine (EDQE)
    successfully validates the complete dataset.
    """

    dataframe = generate_sales(
        calendar=calendar,
        leads=leads,
        products=products,
    )

    validate_dataframe(
        dataframe,
        "Fact_Sales",
    )

    print(f"✓ Fact_Sales generated ({len(dataframe):,} records)")

    return dataframe
