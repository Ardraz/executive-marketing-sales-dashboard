"""
Campaign Business Rules
"""

# ==========================================================
# CAMPAIGN TYPES
# ==========================================================

CAMPAIGN_TYPES = [
    "Google Search Ads",
    "Google Display Ads",
    "Facebook Ads",
    "Instagram Ads",
    "LinkedIn Ads",
    "TikTok Ads",
    "Email Marketing",
    "Webinar",
    "Workshop",
    "Referral Program",
    "SEO Content",
    "Affiliate Program",
]

# ==========================================================
# MARKETING CHANNEL
# ==========================================================

MARKETING_CHANNEL = {
    "Google Search Ads": "Paid Ads",
    "Google Display Ads": "Paid Ads",
    "Facebook Ads": "Paid Ads",
    "Instagram Ads": "Paid Ads",
    "LinkedIn Ads": "Paid Ads",
    "TikTok Ads": "Paid Ads",
    "Email Marketing": "Email",
    "Webinar": "Partnership",
    "Workshop": "Partnership",
    "Referral Program": "Referral",
    "SEO Content": "Organic",
    "Affiliate Program": "Partnership",
}

# ==========================================================
# PLATFORM
# ==========================================================

PLATFORMS = {
    "Google Search Ads": "Google",
    "Google Display Ads": "Google",
    "Facebook Ads": "Facebook",
    "Instagram Ads": "Instagram",
    "LinkedIn Ads": "LinkedIn",
    "TikTok Ads": "TikTok",
    "Email Marketing": "Email",
    "Webinar": "Offline",
    "Workshop": "Offline",
    "Referral Program": "Website",
    "SEO Content": "Website",
    "Affiliate Program": "Website",
}

# ==========================================================
# OBJECTIVES
# ==========================================================

OBJECTIVES = {
    "Google Search Ads": "Sales Conversion",
    "Google Display Ads": "Brand Awareness",
    "Facebook Ads": "Lead Generation",
    "Instagram Ads": "Lead Generation",
    "LinkedIn Ads": "Lead Generation",
    "TikTok Ads": "Brand Awareness",
    "Email Marketing": "Customer Retention",
    "Webinar": "Lead Generation",
    "Workshop": "Lead Generation",
    "Referral Program": "Sales Conversion",
    "SEO Content": "Brand Awareness",
    "Affiliate Program": "Sales Conversion",
}

# ==========================================================
# STATUS
# ==========================================================

STATUS_OPTIONS = {
    "Completed": 60,
    "Active": 30,
    "Planning": 10,
}

# ==========================================================
# BUDGET RANGE (IDR)
# ==========================================================

BUDGET_RANGE = {
    "Google Search Ads": (100_000_000, 180_000_000),
    "Google Display Ads": (80_000_000, 150_000_000),
    "Facebook Ads": (50_000_000, 120_000_000),
    "Instagram Ads": (40_000_000, 100_000_000),
    "LinkedIn Ads": (90_000_000, 160_000_000),
    "TikTok Ads": (40_000_000, 90_000_000),
    "Email Marketing": (5_000_000, 20_000_000),
    "Webinar": (20_000_000, 40_000_000),
    "Workshop": (25_000_000, 50_000_000),
    "Referral Program": (3_000_000, 15_000_000),
    "SEO Content": (10_000_000, 35_000_000),
    "Affiliate Program": (10_000_000, 30_000_000),
}

# ==========================================================
# TARGET LEADS
# ==========================================================

TARGET_LEADS_RANGE = {
    "Google Search Ads": (1200, 2200),
    "Google Display Ads": (900, 1800),
    "Facebook Ads": (1000, 2000),
    "Instagram Ads": (900, 1800),
    "LinkedIn Ads": (300, 700),
    "TikTok Ads": (1200, 2500),
    "Email Marketing": (500, 1200),
    "Webinar": (300, 800),
    "Workshop": (150, 400),
    "Referral Program": (100, 350),
    "SEO Content": (500, 1000),
    "Affiliate Program": (250, 600),
}

# ==========================================================
# TARGET REVENUE MULTIPLIER
# Revenue ≈ Budget x Multiplier
# ==========================================================

REVENUE_MULTIPLIER = {
    "Google Search Ads": (6.0, 10.0),
    "Google Display Ads": (3.0, 5.0),
    "Facebook Ads": (5.0, 8.0),
    "Instagram Ads": (4.5, 7.0),
    "LinkedIn Ads": (8.0, 12.0),
    "TikTok Ads": (4.0, 6.5),
    "Email Marketing": (10.0, 15.0),
    "Webinar": (5.0, 8.0),
    "Workshop": (4.0, 7.0),
    "Referral Program": (12.0, 20.0),
    "SEO Content": (8.0, 14.0),
    "Affiliate Program": (7.0, 12.0),
}
