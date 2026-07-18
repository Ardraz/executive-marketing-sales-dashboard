"""
Advertising Fact Generator
"""

import random
from datetime import datetime

import pandas as pd

from business.ads_rules import (
    IMPRESSIONS_RANGE,
    CTR_RANGE,
    CPC_RANGE,
)

from core.config import RANDOM_SEED

random.seed(RANDOM_SEED)


# ==========================================================
# Helper Functions
# ==========================================================


def random_integer(value_range: tuple) -> int:
    """
    Return random integer within range.
    """

    return random.randint(
        value_range[0],
        value_range[1],
    )


def random_float(value_range: tuple) -> float:
    """
    Return random float within range.
    """

    return random.uniform(
        value_range[0],
        value_range[1],
    )


def random_row(dataframe: pd.DataFrame) -> pd.Series:
    """
    Return one random row from dataframe.
    """

    return dataframe.sample(
        n=1,
        replace=False,
    ).iloc[0]


# ==========================================================
# Advertising Generator
# ==========================================================


def generate_ads(
    calendar: pd.DataFrame,
    campaigns: pd.DataFrame,
) -> pd.DataFrame:
    """
    Generate Advertising Fact Table.
    """

    ads = []

    ads_id = 1

    # ======================================================
    # Active Campaign
    # ======================================================

    active_campaigns = campaigns[campaigns["Status"] == "Active"]

    if active_campaigns.empty:
        raise ValueError("No active campaign available.")

    # ======================================================
    # Generate Ads
    # ======================================================

    for _, campaign in active_campaigns.iterrows():

        campaign_start = pd.Timestamp(campaign["StartDate"])

        campaign_end = pd.Timestamp(campaign["EndDate"])

        campaign_dates = calendar[
            (calendar["Date"] >= campaign_start) & (calendar["Date"] <= campaign_end)
        ]

        if campaign_dates.empty:
            continue

        platform = campaign["Platform"]

        marketing_channel = campaign["MarketingChannel"]

        impression_range = IMPRESSIONS_RANGE[platform]

        ctr_range = CTR_RANGE[platform]

        cpc_range = CPC_RANGE[platform]

        # ==============================================
        # Generate Daily Ads Metrics
        # ==============================================

        for _, ad_date in campaign_dates.iterrows():

            impressions = random_integer(impression_range)

            ctr = random_float(ctr_range)

            clicks = round(impressions * ctr)

            cpc = round(
                random_float(cpc_range),
                2,
            )

            spend = round(
                clicks * cpc,
                2,
            )
            # ==============================================
            # Conversion Rate
            # ==============================================

            if platform == "Google":
                conversion_rate = random.uniform(
                    0.040,
                    0.090,
                )

            elif platform == "Facebook":
                conversion_rate = random.uniform(
                    0.025,
                    0.060,
                )

            elif platform == "Instagram":
                conversion_rate = random.uniform(
                    0.020,
                    0.050,
                )

            elif platform == "LinkedIn":
                conversion_rate = random.uniform(
                    0.050,
                    0.120,
                )

            elif platform == "TikTok":
                conversion_rate = random.uniform(
                    0.020,
                    0.050,
                )

            elif platform == "Email":
                conversion_rate = random.uniform(
                    0.080,
                    0.180,
                )

            elif platform == "Website":
                conversion_rate = random.uniform(
                    0.030,
                    0.080,
                )

            elif platform == "Offline":
                conversion_rate = random.uniform(
                    0.100,
                    0.250,
                )

            else:
                conversion_rate = random.uniform(
                    0.020,
                    0.050,
                )

            conversions = round(clicks * conversion_rate)

            # ==============================================
            # Revenue
            # ==============================================

            if platform == "Google":
                avg_order_value = random.randint(
                    250,
                    600,
                )

            elif platform == "Facebook":
                avg_order_value = random.randint(
                    180,
                    450,
                )

            elif platform == "Instagram":
                avg_order_value = random.randint(
                    180,
                    420,
                )

            elif platform == "LinkedIn":
                avg_order_value = random.randint(
                    800,
                    2000,
                )

            elif platform == "TikTok":
                avg_order_value = random.randint(
                    180,
                    420,
                )

            elif platform == "Email":
                avg_order_value = random.randint(
                    350,
                    900,
                )

            elif platform == "Website":
                avg_order_value = random.randint(
                    250,
                    700,
                )

            elif platform == "Offline":
                avg_order_value = random.randint(
                    700,
                    1800,
                )

            else:
                avg_order_value = random.randint(
                    200,
                    500,
                )

            revenue = round(
                conversions * avg_order_value,
                2,
            )

            # ==============================================
            # ROAS
            # ==============================================

            if spend > 0:

                roas = round(
                    revenue / spend,
                    2,
                )

            else:

                roas = 0

            # ==============================================
            # Timestamp
            # ==============================================

            ads_timestamp = datetime.combine(
                ad_date["Date"].date(),
                datetime.min.time(),
            )

            # ==============================================
            # Build Record
            # ==============================================

            ads_record = {
                "AdsID": ads_id,
                "AdsCode": (f"ADS{ads_id:06}"),
                "DateKey": (ad_date["DateKey"]),
                "AdsDate": (ad_date["Date"].date()),
                "AdsTimestamp": (ads_timestamp),
                "CampaignID": (campaign["CampaignID"]),
                "Platform": (platform),
                "MarketingChannel": (marketing_channel),
                "Impressions": (impressions),
                "Clicks": (clicks),
                "CTR": (
                    round(
                        ctr,
                        4,
                    )
                ),
                "CPC": (cpc),
                "Spend": (spend),
                "Conversions": (conversions),
                "ConversionRate": (
                    round(
                        conversion_rate,
                        4,
                    )
                ),
                "Revenue": (revenue),
                "ROAS": (roas),
            }

            # ==============================================
            # Append Record
            # ==============================================

            ads.append(ads_record)

            ads_id += 1

    # ======================================================
    # Create DataFrame
    # ======================================================

    dataframe = pd.DataFrame(
        ads,
        columns=[
            "AdsID",
            "AdsCode",
            "DateKey",
            "AdsDate",
            "AdsTimestamp",
            "CampaignID",
            "Platform",
            "MarketingChannel",
            "Impressions",
            "Clicks",
            "CTR",
            "CPC",
            "Spend",
            "Conversions",
            "ConversionRate",
            "Revenue",
            "ROAS",
        ],
    )
    # ======================================================
    # Final Validation
    # ======================================================

    if dataframe.empty:
        raise ValueError("Fact_Ads generation failed. No records generated.")

    # ======================================================
    # Sort Data
    # ======================================================

    dataframe = dataframe.sort_values(
        by=[
            "AdsDate",
            "CampaignID",
        ],
        ascending=True,
    ).reset_index(
        drop=True,
    )

    # ======================================================
    # Re-index AdsID & AdsCode
    # ======================================================

    dataframe["AdsID"] = range(
        1,
        len(dataframe) + 1,
    )

    dataframe["AdsCode"] = dataframe["AdsID"].apply(lambda x: f"ADS{x:06}")

    # ======================================================
    # Data Type
    # ======================================================

    dataframe["CTR"] = dataframe["CTR"].round(4)

    dataframe["ConversionRate"] = dataframe["ConversionRate"].round(4)

    dataframe["CPC"] = dataframe["CPC"].round(2)

    dataframe["Spend"] = dataframe["Spend"].round(2)

    dataframe["Revenue"] = dataframe["Revenue"].round(2)

    dataframe["ROAS"] = dataframe["ROAS"].round(2)

    # ======================================================
    # Return
    # ======================================================

    return dataframe
