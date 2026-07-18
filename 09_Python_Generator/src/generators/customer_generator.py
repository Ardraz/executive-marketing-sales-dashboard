import random
from datetime import datetime

import pandas as pd
from faker import Faker

from business.country_master import COUNTRIES
from business.customer_rules import (
    AGE_RANGE,
    GENDER_DISTRIBUTION,
    SEGMENT_DISTRIBUTION,
    LTV_RANGE,
    LOYALTY_TIERS,
)
from core.config import (
    RANDOM_SEED,
    TARGET_CUSTOMERS,
    END_DATE,
)

# ==========================================================
# Faker Configuration
# ==========================================================

fake = Faker(["id_ID", "en_US"])

Faker.seed(RANDOM_SEED)
random.seed(RANDOM_SEED)

# ==========================================================
# Helper Functions
# ==========================================================


def age_group(age: int) -> str:
    """Return age group based on age."""

    if age <= 24:
        return "18-24"
    elif age <= 34:
        return "25-34"
    elif age <= 44:
        return "35-44"
    elif age <= 54:
        return "45-54"
    else:
        return "55+"


def get_loyalty_tier(value: int) -> str:
    """Return loyalty tier based on Lifetime Value."""

    for tier, minimum, maximum in LOYALTY_TIERS:
        if minimum <= value <= maximum:
            return tier

    return "Bronze"


# ==========================================================
# Main Generator
# ==========================================================


def generate_customers() -> pd.DataFrame:
    """Generate Customer Dimension."""

    customers = []

    end_date = datetime.strptime(END_DATE, "%Y-%m-%d").date()

    for customer_id in range(1, TARGET_CUSTOMERS + 1):

        # --------------------------------------------------
        # Country & City
        # --------------------------------------------------

        country = random.choice(COUNTRIES)
        city = random.choice(country["Cities"])

        # --------------------------------------------------
        # Customer Demographics
        # --------------------------------------------------

        age = random.randint(*AGE_RANGE)

        gender = random.choices(
            population=list(GENDER_DISTRIBUTION.keys()),
            weights=list(GENDER_DISTRIBUTION.values()),
            k=1,
        )[0]

        segment = random.choices(
            population=list(SEGMENT_DISTRIBUTION.keys()),
            weights=list(SEGMENT_DISTRIBUTION.values()),
            k=1,
        )[0]

        # --------------------------------------------------
        # Business Rules
        # --------------------------------------------------

        min_ltv, max_ltv = LTV_RANGE[segment]
        ltv = random.randint(min_ltv, max_ltv)

        # --------------------------------------------------
        # Customer Record
        # --------------------------------------------------

        customers.append(
            {
                "CustomerID": customer_id,
                "CustomerCode": f"CUST{customer_id:05}",
                "CustomerName": fake.name(),
                "Email": fake.email(),
                "Phone": fake.phone_number(),
                "Gender": gender,
                "Age": age,
                "AgeGroup": age_group(age),
                "CountryID": country["CountryID"],
                "Country": country["Country"],
                "City": city,
                "CustomerSegment": segment,
                "RegistrationDate": fake.date_between(
                    start_date="-3y",
                    end_date=end_date,
                ),
                "Status": "Active",
                "LifetimeValue": ltv,
                "LoyaltyTier": get_loyalty_tier(ltv),
            }
        )

    return pd.DataFrame(customers)
