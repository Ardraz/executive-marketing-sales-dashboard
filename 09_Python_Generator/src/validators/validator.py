"""
Data Validation Utility
"""

import pandas as pd


def validate_dataframe(
    dataframe: pd.DataFrame,
    table_name: str,
) -> None:
    """
    Validate generated dataframe.

    Validation:
    - Empty dataframe
    - Duplicate rows
    - Null values
    """

    print()
    print("=" * 60)
    print(f"VALIDATING : {table_name}")
    print("=" * 60)

    # -----------------------------------------------------
    # Empty dataframe
    # -----------------------------------------------------

    if dataframe.empty:
        raise ValueError(f"{table_name} is empty.")

    print(f"✓ Total Rows : {len(dataframe):,}")

    # -----------------------------------------------------
    # Duplicate rows
    # -----------------------------------------------------

    duplicate_rows = dataframe.duplicated().sum()

    if duplicate_rows > 0:
        print(f"⚠ Duplicate Rows : {duplicate_rows}")
    else:
        print("✓ Duplicate Rows : 0")

    # -----------------------------------------------------
    # Missing Values
    # -----------------------------------------------------

    missing = dataframe.isnull().sum()

    missing = missing[missing > 0]

    if len(missing) == 0:
        print("✓ Missing Values : 0")
    else:
        print("⚠ Missing Values")

        for column, value in missing.items():
            print(f"   {column:<25}{value}")

    print("Validation Finished.")
