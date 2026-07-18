"""
Lead Business Rules
"""

# ==========================================================
# LEAD STATUS
# ==========================================================

LEAD_STATUS = {
    "New": 20,
    "Contacted": 25,
    "Qualified": 25,
    "Lost": 20,
    "Converted": 10,
}

# ==========================================================
# LEAD SCORE
# ==========================================================

LEAD_SCORE_RANGE = {
    "New": (20, 45),
    "Contacted": (35, 60),
    "Qualified": (60, 85),
    "Lost": (5, 40),
    "Converted": (80, 100),
}

# ==========================================================
# DEAL VALUE MULTIPLIER
# Estimated Deal Value = Product List Price × Multiplier
# ==========================================================

DEAL_VALUE_MULTIPLIER = {
    "New": (0.90, 1.10),
    "Contacted": (0.95, 1.15),
    "Qualified": (1.00, 1.20),
    "Lost": (0.80, 1.00),
    "Converted": (1.00, 1.30),
}

# ==========================================================
# EXPECTED CLOSE DAYS
# ==========================================================

EXPECTED_CLOSE_DAYS = {
    "New": (30, 60),
    "Contacted": (20, 45),
    "Qualified": (7, 30),
    "Lost": (0, 0),
    "Converted": (0, 7),
}
