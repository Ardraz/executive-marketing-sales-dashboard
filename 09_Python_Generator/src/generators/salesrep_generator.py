"""
Sales Representative Dimension Generator
"""

import random
from datetime import datetime

import pandas as pd

from business.salesrep_rules import (
    SALESREP_NAMES,
    GENDER,
    ORGANIZATION,
    BRANCH_DISTRIBUTION,
    EXPERIENCE_LEVEL,
    STATUS_OPTIONS,
    TARGET_REVENUE,
    COMMISSION_RATE,
)

from core.config import (
    RANDOM_SEED,
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


def generate_sales_reps() -> pd.DataFrame:
    """
    Generate Sales Representative Dimension.
    """

    sales_reps = []

    salesrep_names = SALESREP_NAMES.copy()
    random.shuffle(salesrep_names)

    salesrep_id = 1

    for organization in ORGANIZATION:

        branch = organization["Branch"]

        total_sales = BRANCH_DISTRIBUTION[branch]

        for _ in range(total_sales):

            experience = weighted_choice(
                EXPERIENCE_LEVEL,
            )

            status = weighted_choice(
                STATUS_OPTIONS,
            )

            gender = weighted_choice(
                GENDER,
            )

            # =====================================================
            # Hire Date
            # =====================================================

            if experience == "Senior":

                hire_start = datetime(
                    2018,
                    1,
                    1,
                ).date()

                hire_end = datetime(
                    2022,
                    12,
                    31,
                ).date()

            else:

                hire_start = datetime(
                    2022,
                    1,
                    1,
                ).date()

                hire_end = datetime(
                    2025,
                    6,
                    30,
                ).date()

            hire_date = (
                pd.Timestamp(hire_start)
                + pd.to_timedelta(
                    random.randint(
                        0,
                        (hire_end - hire_start).days,
                    ),
                    unit="D",
                )
            ).date()

            # =====================================================
            # Target Revenue
            # =====================================================

            min_target, max_target = TARGET_REVENUE[experience]

            target_revenue = random.randint(
                min_target,
                max_target,
            )

            # =====================================================
            # Commission
            # =====================================================

            commission_rate = COMMISSION_RATE[experience]

            # =====================================================
            # Sales Representative Record
            # =====================================================

            sales_reps.append(
                {
                    "SalesRepID": salesrep_id,
                    "SalesRepCode": f"REP{salesrep_id:05}",
                    "SalesRepName": salesrep_names[salesrep_id - 1],
                    "Gender": gender,
                    "Country": organization["Country"],
                    "Region": organization["Region"],
                    "Branch": organization["Branch"],
                    "HireDate": hire_date,
                    "ExperienceLevel": experience,
                    "TargetRevenue": target_revenue,
                    "CommissionRate": commission_rate,
                    "Status": status,
                }
            )

            salesrep_id += 1

    return pd.DataFrame(sales_reps)
