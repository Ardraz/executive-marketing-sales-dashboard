"""
Lead Fact Generator
"""

import random
from datetime import datetime

import pandas as pd

from business.leads_rules import (
    LEAD_STATUS,
    LEAD_SCORE_RANGE,
    DEAL_VALUE_MULTIPLIER,
    EXPECTED_CLOSE_DAYS,
)

from core.config import (
    RANDOM_SEED,
    TARGET_LEADS,
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


def random_row(dataframe: pd.DataFrame) -> pd.Series:
    """
    Return one random row from DataFrame.
    """
    return dataframe.sample(
        n=1,
        replace=False,
    ).iloc[0]


def generate_leads(
    calendar: pd.DataFrame,
    customers: pd.DataFrame,
    products: pd.DataFrame,
    campaigns: pd.DataFrame,
    sales_reps: pd.DataFrame,
) -> pd.DataFrame:
    """
    Generate Lead Fact Table.
    """

    leads = []

    # =====================================================
    # Active Campaign
    # =====================================================

    active_campaigns = campaigns[campaigns["Status"] == "Active"]

    if active_campaigns.empty:
        raise ValueError("No active campaign available.")

    # =====================================================
    # Active Product
    # =====================================================

    active_products = products[products["Status"] == "Active"]

    if active_products.empty:
        raise ValueError("No active product available.")

    # =====================================================
    # Active Sales Representative
    # =====================================================

    active_sales = sales_reps[sales_reps["Status"] == "Active"]

    if active_sales.empty:
        raise ValueError("No active sales representative available.")

    # =====================================================
    # Generate Lead
    # =====================================================

    for lead_id in range(
        1,
        TARGET_LEADS + 1,
    ):

        # -------------------------------------------------
        # Campaign
        # -------------------------------------------------

        campaign = random_row(
            active_campaigns,
        )

        # -------------------------------------------------
        # Campaign Period
        # -------------------------------------------------

        campaign_start = pd.Timestamp(campaign["StartDate"])

        campaign_end = pd.Timestamp(campaign["EndDate"])

        valid_dates = calendar[
            (calendar["Date"] >= campaign_start) & (calendar["Date"] <= campaign_end)
        ]

        if valid_dates.empty:
            continue

        lead_date = random_row(
            valid_dates,
        )

        # -------------------------------------------------
        # Customer
        # -------------------------------------------------

        customer = random_row(
            customers,
        )

        # -------------------------------------------------
        # Product
        # -------------------------------------------------

        product = random_row(
            active_products,
        )

        # -------------------------------------------------
        # Sales Representative
        # -------------------------------------------------

        sales_rep = random_row(
            active_sales,
        )

        # -------------------------------------------------
        # Lead Status
        # -------------------------------------------------

        lead_status = weighted_choice(
            LEAD_STATUS,
        )

        # -------------------------------------------------
        # Lead Score
        # -------------------------------------------------

        min_score, max_score = LEAD_SCORE_RANGE[lead_status]

        lead_score = random.randint(
            min_score,
            max_score,
        )
        # -------------------------------------------------
        # Estimated Deal Value
        # -------------------------------------------------

        min_multiplier, max_multiplier = DEAL_VALUE_MULTIPLIER[lead_status]

        multiplier = random.uniform(
            min_multiplier,
            max_multiplier,
        )

        estimated_deal_value = round(
            product["ListPrice"] * multiplier,
            2,
        )

        # -------------------------------------------------
        # Expected Close Date
        # -------------------------------------------------

        min_days, max_days = EXPECTED_CLOSE_DAYS[lead_status]

        close_days = random.randint(
            min_days,
            max_days,
        )

        expected_close_date = lead_date["Date"] + pd.Timedelta(days=close_days)

        # -------------------------------------------------
        # Lead Source
        # -------------------------------------------------

        lead_source = campaign["MarketingChannel"]

        # -------------------------------------------------
        # Lead Timestamp
        # -------------------------------------------------

        lead_timestamp = datetime.combine(
            lead_date["Date"].date(),
            datetime.min.time(),
        )

        # -------------------------------------------------
        # Build Lead Record
        # -------------------------------------------------

        lead_record = {
            "LeadID": lead_id,
            "LeadCode": (f"LEAD{lead_id:06}"),
            "DateKey": lead_date["DateKey"],
            "LeadDate": (lead_date["Date"].date()),
            "LeadTimestamp": (lead_timestamp),
            "CustomerID": customer["CustomerID"],
            "CampaignID": campaign["CampaignID"],
            "ProductID": product["ProductID"],
            "SalesRepID": sales_rep["SalesRepID"],
            "LeadSource": lead_source,
            "LeadStatus": lead_status,
            "LeadScore": lead_score,
            "EstimatedDealValue": (estimated_deal_value),
            "ExpectedCloseDate": (expected_close_date.date()),
        }

        leads.append(lead_record)
    # =====================================================
    # Create DataFrame
    # =====================================================

    dataframe = pd.DataFrame(
        leads,
        columns=[
            "LeadID",
            "LeadCode",
            "DateKey",
            "LeadDate",
            "LeadTimestamp",
            "CustomerID",
            "CampaignID",
            "ProductID",
            "SalesRepID",
            "LeadSource",
            "LeadStatus",
            "LeadScore",
            "EstimatedDealValue",
            "ExpectedCloseDate",
        ],
    )

    return dataframe
