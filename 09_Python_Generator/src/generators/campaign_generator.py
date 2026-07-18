"""
Campaign Dimension Generator
"""

import random
from datetime import datetime

import pandas as pd

from business.campaign_rules import (
    CAMPAIGN_TYPES,
    MARKETING_CHANNEL,
    PLATFORMS,
    OBJECTIVES,
    STATUS_OPTIONS,
    BUDGET_RANGE,
    TARGET_LEADS_RANGE,
    REVENUE_MULTIPLIER,
)

from core.config import (
    RANDOM_SEED,
    START_DATE,
    END_DATE,
    TOTAL_CAMPAIGNS,
)

random.seed(RANDOM_SEED)


def weighted_choice(options: dict):
    """
    Select one value using weighted probability.
    """

    return random.choices(
        population=list(options.keys()),
        weights=list(options.values()),
        k=1,
    )[0]


def generate_campaigns() -> pd.DataFrame:
    """
    Generate Campaign Dimension.
    """

    campaigns = []

    active_start_date = datetime.strptime(
        START_DATE,
        "%Y-%m-%d",
    ).date()

    active_end_date = datetime.strptime(
        END_DATE,
        "%Y-%m-%d",
    ).date()

    planning_start_date = datetime.strptime(
        "2026-01-01",
        "%Y-%m-%d",
    ).date()

    planning_end_date = datetime.strptime(
        "2026-06-30",
        "%Y-%m-%d",
    ).date()

    completed_start_date = datetime.strptime(
        "2024-01-01",
        "%Y-%m-%d",
    ).date()

    completed_end_date = datetime.strptime(
        "2024-12-31",
        "%Y-%m-%d",
    ).date()

    selected_campaigns = CAMPAIGN_TYPES[:TOTAL_CAMPAIGNS]

    for campaign_id, campaign_type in enumerate(
        selected_campaigns,
        start=1,
    ):

        status = weighted_choice(STATUS_OPTIONS)

        # =====================================================
        # Campaign Period
        # =====================================================

        if status == "Completed":

            start_period = completed_start_date
            end_period = completed_end_date

        elif status == "Planning":

            start_period = planning_start_date
            end_period = planning_end_date

        else:

            start_period = active_start_date
            end_period = active_end_date

        start_date = (
            pd.Timestamp(start_period)
            + pd.to_timedelta(
                random.randint(
                    0,
                    (end_period - start_period).days,
                ),
                unit="D",
            )
        ).date()

        duration_days = random.randint(
            30,
            120,
        )

        end_date = (
            pd.Timestamp(start_date)
            + pd.to_timedelta(
                duration_days,
                unit="D",
            )
        ).date()

        # =====================================================
        # Budget
        # =====================================================

        min_budget, max_budget = BUDGET_RANGE[campaign_type]

        budget = random.randint(
            min_budget,
            max_budget,
        )

        # =====================================================
        # Target Leads
        # =====================================================

        min_leads, max_leads = TARGET_LEADS_RANGE[campaign_type]

        target_leads = random.randint(
            min_leads,
            max_leads,
        )

        # =====================================================
        # Target Revenue
        # =====================================================

        min_multiplier, max_multiplier = REVENUE_MULTIPLIER[campaign_type]

        multiplier = random.uniform(
            min_multiplier,
            max_multiplier,
        )

        target_revenue = round(
            budget * multiplier,
            2,
        )

        # =====================================================
        # Campaign Record
        # =====================================================

        campaigns.append(
            {
                "CampaignID": campaign_id,
                "CampaignCode": f"CMP{campaign_id:05}",
                "CampaignName": f"{campaign_type} {start_date.year}",
                "CampaignType": campaign_type,
                "MarketingChannel": MARKETING_CHANNEL[campaign_type],
                "Platform": PLATFORMS[campaign_type],
                "Objective": OBJECTIVES[campaign_type],
                "StartDate": start_date,
                "EndDate": end_date,
                "Budget": budget,
                "TargetLeads": target_leads,
                "TargetRevenue": target_revenue,
                "Status": status,
            }
        )

    return pd.DataFrame(campaigns)
