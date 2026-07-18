"""
Product Dimension Pipeline
"""

from generators.product_generator import generate_products

from validators.validator import validate_dataframe


def run_product_pipeline():
    """
    Generate and validate Product Dimension.

    Export is handled after the Enterprise Data Quality Engine (EDQE)
    successfully validates the complete dataset.
    """

    products = generate_products()

    validate_dataframe(
        products,
        "Dim_Product",
    )

    return products
