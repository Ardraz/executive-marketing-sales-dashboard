"""
Lead Fact Pipeline
"""

from generators.leads_generator import generate_leads

from validators.validator import validate_dataframe


def run_leads_pipeline(
    calendar,
    customers,
    products,
    campaigns,
    sales_reps,
):
    """
    Generate and validate Lead Fact Table.

    Export is handled after the Enterprise Data Quality Engine (EDQE)
    successfully validates the complete dataset.
    """

    dataframe = generate_leads(
        calendar=calendar,
        customers=customers,
        products=products,
        campaigns=campaigns,
        sales_reps=sales_reps,
    )

    validate_dataframe(
        dataframe,
        "Fact_Leads",
    )

    print(f"✓ Fact_Leads generated ({len(dataframe):,} records)")

    return dataframe
