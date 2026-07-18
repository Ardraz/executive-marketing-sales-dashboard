"""
Business Rules for Product Dimension
"""

# ==========================================================
# DELIVERY METHOD PER CATEGORY
# ==========================================================

DELIVERY_METHODS = {
    "Data Analytics": {
        "Self-paced": 0.60,
        "Live Class": 0.20,
        "Hybrid": 0.20,
    },
    "Business Intelligence": {
        "Self-paced": 0.50,
        "Live Class": 0.30,
        "Hybrid": 0.20,
    },
    "Artificial Intelligence": {
        "Self-paced": 0.25,
        "Live Class": 0.45,
        "Hybrid": 0.30,
    },
    "Programming": {
        "Self-paced": 0.70,
        "Live Class": 0.15,
        "Hybrid": 0.15,
    },
}

# ==========================================================
# CATEGORY INSTRUCTORS
# ==========================================================

CATEGORY_INSTRUCTORS = {
    "Data Analytics": [
        "Kevin Miller",
        "Sophia Adams",
        "Daniel Moore",
    ],
    "Business Intelligence": [
        "Emily Wilson",
        "Michael Johnson",
        "Sarah Lee",
    ],
    "Artificial Intelligence": [
        "Andrew Chen",
        "James Anderson",
        "Sophia Taylor",
    ],
    "Programming": [
        "David Brown",
        "Ryan Walker",
        "Olivia Martinez",
    ],
}

# ==========================================================
# TARGET AUDIENCE
# ==========================================================

TARGET_AUDIENCE = {
    "Student": 0.30,
    "Professional": 0.50,
    "Corporate": 0.20,
}

# ==========================================================
# LANGUAGE
# ==========================================================

LANGUAGES = {
    "English": 0.60,
    "Bahasa Indonesia": 0.40,
}

# ==========================================================
# CERTIFICATE
# ==========================================================

CERTIFICATE_OPTIONS = {
    True: 0.90,
    False: 0.10,
}

# ==========================================================
# SUBSCRIPTION
# ==========================================================

SUBSCRIPTION_OPTIONS = {
    True: 0.70,
    False: 0.30,
}

# ==========================================================
# STATUS
# ==========================================================

STATUS_OPTIONS = {
    "Active": 0.90,
    "Retired": 0.10,
}

# ==========================================================
# PRICE RANGE
# ==========================================================

PRICE_RANGE = {
    ("Data Analytics", "Beginner"): (89, 129),
    ("Data Analytics", "Intermediate"): (149, 249),
    ("Data Analytics", "Advanced"): (259, 399),
    ("Business Intelligence", "Beginner"): (99, 149),
    ("Business Intelligence", "Intermediate"): (199, 299),
    ("Business Intelligence", "Advanced"): (329, 499),
    ("Artificial Intelligence", "Beginner"): (149, 249),
    ("Artificial Intelligence", "Intermediate"): (299, 449),
    ("Artificial Intelligence", "Advanced"): (499, 799),
    ("Programming", "Beginner"): (79, 139),
    ("Programming", "Intermediate"): (169, 279),
    ("Programming", "Advanced"): (299, 499),
}

# ==========================================================
# COST %
# ==========================================================

MIN_COST_PERCENT = 0.28
MAX_COST_PERCENT = 0.42

# ==========================================================
# RATING
# ==========================================================

MIN_RATING = 4.3
MAX_RATING = 5.0
