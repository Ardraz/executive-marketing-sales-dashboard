"""
Sales Business Rules
"""

# ==========================================================
# SALES CONFIGURATION
# ==========================================================

MIN_QUANTITY = 1
MAX_QUANTITY = 5

MAX_DISCOUNT_PERCENT = 0.30

# ==========================================================
# DISCOUNT BY QUANTITY
# ==========================================================

DISCOUNT_BY_QUANTITY = {
    1: (0.00, 0.05),
    2: (0.03, 0.10),
    3: (0.05, 0.15),
    4: (0.10, 0.25),
    5: (0.15, 0.30),
}

# ==========================================================
# PAYMENT METHOD
# ==========================================================

PAYMENT_METHOD = {
    "Bank Transfer": 35,
    "Credit Card": 25,
    "Virtual Account": 20,
    "E-Wallet": 15,
    "Corporate Invoice": 5,
}

# ==========================================================
# PAYMENT STATUS
# ==========================================================

PAYMENT_STATUS = {
    "Paid": 85,
    "Pending": 10,
    "Failed": 5,
}
# ==========================================================
# ORDER STATUS
# ==========================================================

ORDER_STATUS = {
    "Completed": 90,
    "Processing": 7,
    "Cancelled": 3,
}

# ==========================================================
# SALES CHANNEL
# ==========================================================

SALES_CHANNEL = {
    "Website": 30,
    "Sales Representative": 35,
    "Partner": 15,
    "Referral": 10,
    "Marketplace": 10,
}

# ==========================================================
# SALES CODE
# ==========================================================

SALES_CODE_PREFIX = "SAL"

# Format:
# SAL-2026-000001

# ==========================================================
# INVOICE NUMBER
# ==========================================================

INVOICE_PREFIX = "INV"

# Format:
# INV-YYYYMMDD-000001

# ==========================================================
# SALES TIMESTAMP
# ==========================================================

BUSINESS_HOUR_START = 8
BUSINESS_HOUR_END = 17

BUSINESS_MINUTE_START = 0
BUSINESS_MINUTE_END = 59

BUSINESS_SECOND_START = 0
BUSINESS_SECOND_END = 59

# ==========================================================
# SALES DATE
# ==========================================================

# Sales terjadi setelah Lead dibuat.
# Nilai ini digunakan untuk menentukan jeda hari
# antara LeadDate dan SalesDate.

MIN_CLOSE_DAYS = 0
MAX_CLOSE_DAYS = 30

# ==========================================================
# ROUNDING
# ==========================================================

DECIMAL_PLACES = 2
# ==========================================================
# SALES CALCULATION
# ==========================================================


def calculate_gross_sales(
    quantity: int,
    unit_price: float,
) -> float:
    """
    Calculate Gross Sales.
    """

    return round(
        quantity * unit_price,
        DECIMAL_PLACES,
    )


def calculate_discount_amount(
    gross_sales: float,
    discount_percent: float,
) -> float:
    """
    Calculate Discount Amount.
    """

    return round(
        gross_sales * discount_percent,
        DECIMAL_PLACES,
    )


def calculate_net_sales(
    gross_sales: float,
    discount_amount: float,
) -> float:
    """
    Calculate Net Sales.
    """

    return round(
        gross_sales - discount_amount,
        DECIMAL_PLACES,
    )


def calculate_total_cost(
    quantity: int,
    unit_cost: float,
) -> float:
    """
    Calculate Total Cost.
    """

    return round(
        quantity * unit_cost,
        DECIMAL_PLACES,
    )


def calculate_gross_profit(
    net_sales: float,
    total_cost: float,
) -> float:
    """
    Calculate Gross Profit.
    """

    return round(
        net_sales - total_cost,
        DECIMAL_PLACES,
    )
