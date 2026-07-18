"""
Centralized Excel Export Manager

Responsible for exporting all generated DataFrames
after the Enterprise Data Quality Engine (EDQE)
successfully validates the complete dataset.
"""

from pathlib import Path

import pandas as pd

from utils.excel_exporter import export_to_excel


def export_all_dataframes(
    dataframes: dict[str, pd.DataFrame],
    output_dir: Path,
) -> None:
    """
    Export all DataFrames to Excel.

    Parameters
    ----------
    dataframes
        Dictionary containing all generated DataFrames.

    output_dir
        Output folder.
    """

    print()
    print("=" * 60)
    print("EXPORTING DATASETS")
    print("=" * 60)

    exported = 0

    for table_name, dataframe in dataframes.items():

        export_to_excel(
            dataframe=dataframe,
            file_path=output_dir / f"{table_name}.xlsx",
            sheet_name=table_name,
        )

        exported += 1

    print()
    print(f"✓ Successfully exported {exported} dataset(s).")
