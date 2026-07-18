"""
Product Dimension Generator
"""

import random
from datetime import datetime

import pandas as pd

from business.products import PRODUCTS
from business.product_rules import (
    DELIVERY_METHODS,
    CATEGORY_INSTRUCTORS,
    TARGET_AUDIENCE,
    LANGUAGES,
    CERTIFICATE_OPTIONS,
    SUBSCRIPTION_OPTIONS,
    STATUS_OPTIONS,
    PRICE_RANGE,
    MIN_COST_PERCENT,
    MAX_COST_PERCENT,
    MIN_RATING,
    MAX_RATING,
)

from core.config import (
    RANDOM_SEED,
    START_DATE,
    END_DATE,
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


def generate_products() -> pd.DataFrame:
    """
    Generate Product Dimension.
    """

    products = []

    active_start_date = datetime.strptime(
        START_DATE,
        "%Y-%m-%d",
    ).date()

    active_end_date = datetime.strptime(
        END_DATE,
        "%Y-%m-%d",
    ).date()

    retired_start_date = datetime.strptime(
        "2022-01-01",
        "%Y-%m-%d",
    ).date()

    retired_end_date = datetime.strptime(
        "2024-12-31",
        "%Y-%m-%d",
    ).date()

    for product_id, product in enumerate(PRODUCTS, start=1):

        category = product["Category"]
        difficulty = product["Difficulty"]

        # =====================================================
        # Delivery Method
        # =====================================================

        delivery_method = weighted_choice(DELIVERY_METHODS[category])

        # =====================================================
        # Instructor
        # =====================================================

        instructor = random.choice(CATEGORY_INSTRUCTORS[category])

        # =====================================================
        # Product Status
        # =====================================================

        status = weighted_choice(STATUS_OPTIONS)

        # =====================================================
        # Price
        # =====================================================

        min_price, max_price = PRICE_RANGE[
            (
                category,
                difficulty,
            )
        ]

        list_price = random.randint(
            min_price,
            max_price,
        )

        # =====================================================
        # Cost & Margin
        # =====================================================

        cost_percent = random.uniform(
            MIN_COST_PERCENT,
            MAX_COST_PERCENT,
        )

        unit_cost = round(
            list_price * cost_percent,
            2,
        )

        gross_margin = round(
            list_price - unit_cost,
            2,
        )

        # =====================================================
        # Launch Date
        # =====================================================

        if status == "Retired":

            launch_start = retired_start_date
            launch_end = retired_end_date

        else:

            launch_start = active_start_date
            launch_end = active_end_date

        launch_date = (
            pd.Timestamp(launch_start)
            + pd.to_timedelta(
                random.randint(
                    0,
                    (launch_end - launch_start).days,
                ),
                unit="D",
            )
        ).date()

        # =====================================================
        # Last Updated
        # =====================================================

        if status == "Retired":

            last_updated = (
                pd.Timestamp(launch_date)
                + pd.to_timedelta(
                    random.randint(
                        60,
                        300,
                    ),
                    unit="D",
                )
            ).date()

        else:

            last_updated = (
                pd.Timestamp(launch_date)
                + pd.to_timedelta(
                    random.randint(
                        7,
                        90,
                    ),
                    unit="D",
                )
            ).date()

        # =====================================================
        # Product Record
        # =====================================================

        products.append(
            {
                "ProductID": product_id,
                "ProductCode": f"PRD{product_id:05}",
                "SKU": f"SKU-{1000 + product_id}",
                "ProductName": product["ProductName"],
                "Category": category,
                "DeliveryMethod": delivery_method,
                "Instructor": instructor,
                "Difficulty": difficulty,
                "DurationHours": product["DurationHours"],
                "ListPrice": list_price,
                "UnitCost": unit_cost,
                "GrossMargin": gross_margin,
                "Rating": round(
                    random.uniform(
                        MIN_RATING,
                        MAX_RATING,
                    ),
                    1,
                ),
                "Language": weighted_choice(LANGUAGES),
                "Certificate": weighted_choice(CERTIFICATE_OPTIONS),
                "SubscriptionEligible": weighted_choice(SUBSCRIPTION_OPTIONS),
                "TargetAudience": weighted_choice(TARGET_AUDIENCE),
                "LaunchDate": launch_date,
                "LastUpdated": last_updated,
                "Status": status,
            }
        )

    return pd.DataFrame(products)
