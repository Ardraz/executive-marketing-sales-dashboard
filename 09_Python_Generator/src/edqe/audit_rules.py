"""
Enterprise Data Quality Engine (EDQE)

Central metadata configuration for all audit modules.
"""

TABLE_RULES = {
    "Dim_Date": {
        "primary_key": [
            "DateKey",
        ],
        "foreign_keys": {},
    },
    "Dim_Customer": {
        "primary_key": [
            "CustomerID",
        ],
        "foreign_keys": {},
    },
    "Dim_Product": {
        "primary_key": [
            "ProductID",
        ],
        "foreign_keys": {},
    },
    "Dim_Campaign": {
        "primary_key": [
            "CampaignID",
        ],
        "foreign_keys": {},
    },
    "Dim_SalesRep": {
        "primary_key": [
            "SalesRepID",
        ],
        "foreign_keys": {},
    },
    "Fact_Leads": {
        "primary_key": [
            "LeadID",
        ],
        "foreign_keys": {
            "DateKey": "Dim_Date",
            "CustomerID": "Dim_Customer",
            "CampaignID": "Dim_Campaign",
            "ProductID": "Dim_Product",
            "SalesRepID": "Dim_SalesRep",
        },
    },
    "Fact_Ads": {
        "primary_key": [
            "AdsID",
        ],
        "foreign_keys": {
            "DateKey": "Dim_Date",
            "CampaignID": "Dim_Campaign",
        },
    },
    "Fact_Sales": {
        "primary_key": [
            "SalesID",
        ],
        "foreign_keys": {
            "DateKey": "Dim_Date",
            "CustomerID": "Dim_Customer",
            "CampaignID": "Dim_Campaign",
            "ProductID": "Dim_Product",
            "SalesRepID": "Dim_SalesRep",
        },
    },
}
