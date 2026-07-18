"""
Display Utility
"""

import pandas as pd

LINE = "=" * 60


def display_header(title: str) -> None:
    """
    Display section header.
    """

    print()
    print(LINE)
    print(title.upper())
    print(LINE)


def display_sample(
    title: str,
    dataframe: pd.DataFrame,
    sample_rows: int = 5,
) -> None:
    """
    Display dataframe sample and total rows.
    """

    display_header(f"{title} SAMPLE")

    print(dataframe.head(sample_rows))

    print()
    print(f"Total {title.title()} : {len(dataframe):,}")
