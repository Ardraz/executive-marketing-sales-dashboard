"""
Sales Representative Business Rules
"""

# ==========================================================
# SALES REPRESENTATIVE NAMES
# ==========================================================

SALESREP_NAMES = [
    "Andi Pratama",
    "Budi Santoso",
    "Dimas Saputra",
    "Fajar Hidayat",
    "Rizky Maulana",
    "Yoga Prasetyo",
    "Ari Wibowo",
    "Agus Nugroho",
    "Rahmat Hidayat",
    "Siti Aisyah",
    "Dewi Lestari",
    "Putri Maharani",
    "Nadia Kusuma",
    "Indah Permata",
    "Rina Kartika",
    "Maya Sari",
    "Lina Wulandari",
    "Fitri Handayani",
]

# ==========================================================
# GENDER
# ==========================================================

GENDER = {
    "Male": 50,
    "Female": 50,
}

# ==========================================================
# ORGANIZATION STRUCTURE
# ==========================================================

ORGANIZATION = [
    {
        "Country": "Indonesia",
        "Region": "West",
        "Branch": "Jakarta",
    },
    {
        "Country": "Indonesia",
        "Region": "West",
        "Branch": "Bandung",
    },
    {
        "Country": "Indonesia",
        "Region": "Central",
        "Branch": "Surabaya",
    },
    {
        "Country": "Indonesia",
        "Region": "Central",
        "Branch": "Semarang",
    },
    {
        "Country": "Indonesia",
        "Region": "East",
        "Branch": "Makassar",
    },
    {
        "Country": "Indonesia",
        "Region": "East",
        "Branch": "Balikpapan",
    },
]

# ==========================================================
# SALES DISTRIBUTION
# ==========================================================

BRANCH_DISTRIBUTION = {
    "Jakarta": 5,
    "Bandung": 3,
    "Surabaya": 4,
    "Semarang": 2,
    "Makassar": 2,
    "Balikpapan": 2,
}

# ==========================================================
# EXPERIENCE LEVEL
# ==========================================================

EXPERIENCE_LEVEL = {
    "Junior": 60,
    "Senior": 40,
}

# ==========================================================
# SALES STATUS
# ==========================================================

STATUS_OPTIONS = {
    "Active": 90,
    "Inactive": 10,
}

# ==========================================================
# TARGET REVENUE (IDR)
# ==========================================================

TARGET_REVENUE = {
    "Junior": (
        1_200_000_000,
        2_500_000_000,
    ),
    "Senior": (
        2_500_000_000,
        5_000_000_000,
    ),
}

# ==========================================================
# COMMISSION RATE
# ==========================================================

COMMISSION_RATE = {
    "Junior": 0.03,
    "Senior": 0.05,
}
