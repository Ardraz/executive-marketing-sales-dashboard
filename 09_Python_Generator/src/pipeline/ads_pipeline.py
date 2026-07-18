"""
Advertising Fact Pipeline
"""

from generators.ads_generator import generate_ads

from validators.validator import validate_dataframe


def run_ads_pipeline(
    calendar,
    campaigns,
):
    """
    Generate and validate Advertising Fact Table.

    Export is handled after the Enterprise Data Quality Engine (EDQE)
    successfully validates the complete dataset.
    """

    dataframe = generate_ads(
        calendar=calendar,
        campaigns=campaigns,
    )

    validate_dataframe(
        dataframe,
        "Fact_Ads",
    )

    print(f"✓ Fact_Ads generated ({len(dataframe):,} records)")

    return dataframe
