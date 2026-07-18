"""
Excel Export Utility
"""

from pathlib import Path

import pandas as pd

from core.config import EXCEL_ENGINE


def export_to_excel(
    dataframe: pd.DataFrame,
    output_path: Path,
    sheet_name: str = "Sheet1",
) -> None:
    """
    Export DataFrame to Excel.

    Parameters
    ----------
    dataframe : pd.DataFrame
        DataFrame yang akan disimpan.

    output_path : Path
        Lokasi file Excel.

    sheet_name : str
        Nama worksheet.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    dataframe.to_excel(
        output_path,
        index=False,
        sheet_name=sheet_name,
        engine=EXCEL_ENGINE,
    )

    print(f"✅ Saved : {output_path}")
