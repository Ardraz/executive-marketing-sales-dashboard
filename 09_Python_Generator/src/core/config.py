"""
=========================================================
Executive Marketing & Sales Dashboard
Global Configuration
=========================================================
"""

from pathlib import Path

# =========================================================
# PROJECT INFORMATION
# =========================================================

PROJECT_NAME = "Executive Marketing & Sales Dashboard"
VERSION = "2.1"
AUTHOR = "Prayudi Ardiansyah"

# =========================================================
# RANDOM SEED
# =========================================================

RANDOM_SEED = 2025

# =========================================================
# DATE RANGE
# =========================================================

START_DATE = "2025-01-01"
END_DATE = "2025-12-31"

# =========================================================
# PROJECT PATH
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

RAW_DIR = DATA_DIR / "raw"
DIMENSION_DIR = DATA_DIR / "dimension"
FACT_DIR = DATA_DIR / "fact"
OUTPUT_DIR = DATA_DIR / "output"

# =========================================================
# TARGET RECORDS
# =========================================================

TARGET_CUSTOMERS = 8000
TARGET_SALES = 30000
TARGET_LEADS = 50_000
TARGET_ADS = 10_000

# =========================================================
# DIMENSIONS
# =========================================================

TOTAL_COUNTRIES = 3
TOTAL_PLATFORMS = 5
TOTAL_PRODUCT_CATEGORIES = 4
TOTAL_PRODUCTS = 12
TOTAL_CAMPAIGNS = 12
TOTAL_MANAGERS = 6
TOTAL_SALES_REPS = 18

# =========================================================
# BUSINESS RULES
# =========================================================

MAX_DISCOUNT_PERCENT = 0.30
VAT_RATE = 0.11

# =========================================================
# EXPORT SETTINGS
# =========================================================

EXCEL_ENGINE = "openpyxl"
DATE_FORMAT = "%Y-%m-%d"
