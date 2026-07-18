"""
Generate Date Dimension
"""

import pandas as pd

from core.config import (
    START_DATE,
    END_DATE,
)

SEASONALITY = {
    1: 0.80,
    2: 0.90,
    3: 1.25,
    4: 1.35,
    5: 1.15,
    6: 1.00,
    7: 0.90,
    8: 1.00,
    9: 1.10,
    10: 1.20,
    11: 1.60,
    12: 1.80,
}


def generate_calendar():

    dates = pd.date_range(START_DATE, END_DATE, freq="D")

    df = pd.DataFrame()

    df["Date"] = dates

    df["DateKey"] = df["Date"].dt.strftime("%Y%m%d").astype(int)

    df["Year"] = df["Date"].dt.year

    df["QuarterNumber"] = df["Date"].dt.quarter

    df["Quarter"] = "Q" + df["QuarterNumber"].astype(str)

    df["MonthNumber"] = df["Date"].dt.month

    df["MonthName"] = df["Date"].dt.month_name()

    df["MonthShort"] = df["Date"].dt.strftime("%b")

    df["YearMonth"] = df["Date"].dt.strftime("%Y-%m")

    df["YearMonthLabel"] = df["Date"].dt.strftime("%b %Y")

    df["WeekNumber"] = df["Date"].dt.isocalendar().week

    df["Day"] = df["Date"].dt.day

    df["DayName"] = df["Date"].dt.day_name()

    df["DayShort"] = df["Date"].dt.strftime("%a")

    df["DayOfWeek"] = df["Date"].dt.dayofweek + 1

    df["IsWeekend"] = df["DayOfWeek"] >= 6

    df["SeasonalityIndex"] = df["MonthNumber"].map(SEASONALITY)

    return df
