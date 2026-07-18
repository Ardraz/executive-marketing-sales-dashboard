"""
Campaign Dimension Pipeline
"""

from generators.campaign_generator import generate_campaigns

from validators.validator import validate_dataframe


def run_campaign_pipeline():
    """
    Generate and validate Campaign Dimension.

    Export is handled after the Enterprise Data Quality Engine (EDQE)
    successfully validates the complete dataset.
    """

    campaigns = generate_campaigns()

    validate_dataframe(
        campaigns,
        "Dim_Campaign",
    )

    return campaigns
