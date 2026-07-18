from core.config import (
    PROJECT_NAME,
    VERSION,
    AUTHOR,
    BASE_DIR,
    DATA_DIR,
    OUTPUT_DIR,
)

from pipeline.date_pipeline import run_date_pipeline
from pipeline.customer_pipeline import run_customer_pipeline
from pipeline.product_pipeline import run_product_pipeline
from pipeline.campaign_pipeline import run_campaign_pipeline
from pipeline.salesrep_pipeline import run_salesrep_pipeline
from pipeline.leads_pipeline import run_leads_pipeline
from pipeline.ads_pipeline import run_ads_pipeline
from pipeline.sales_pipeline import run_sales_pipeline

from utils.display import display_sample

LINE = "=" * 60


def main():

    print(LINE)
    print(PROJECT_NAME)
    print(f"Version : {VERSION}")
    print(f"Author  : {AUTHOR}")
    print(LINE)

    print(f"Project Folder : {BASE_DIR}")
    print(f"Data Folder    : {DATA_DIR}")
    print(f"Output Folder  : {OUTPUT_DIR}")

    print()
    print("Configuration Loaded Successfully.")

    # =====================================================
    # DATE DIMENSION
    # =====================================================

    calendar = run_date_pipeline()

    display_sample(
        "Date",
        calendar,
    )

    # =====================================================
    # CUSTOMER DIMENSION
    # =====================================================

    customers = run_customer_pipeline()

    display_sample(
        "Customer",
        customers,
    )

    # =====================================================
    # PRODUCT DIMENSION
    # =====================================================

    products = run_product_pipeline()

    display_sample(
        "Product",
        products,
    )

    # =====================================================
    # CAMPAIGN DIMENSION
    # =====================================================

    campaigns = run_campaign_pipeline()

    display_sample(
        "Campaign",
        campaigns,
    )

    # =====================================================
    # SALES REPRESENTATIVE DIMENSION
    # =====================================================

    sales_reps = run_salesrep_pipeline()

    display_sample(
        "Sales Representative",
        sales_reps,
    )

    print()
    print(LINE)
    print("ALL DIMENSIONS GENERATED SUCCESSFULLY")
    print(LINE)

    # =====================================================
    # FACT LEADS
    # =====================================================

    leads = run_leads_pipeline(
        calendar=calendar,
        customers=customers,
        products=products,
        campaigns=campaigns,
        sales_reps=sales_reps,
    )

    display_sample(
        "Fact Leads",
        leads,
    )

    # =====================================================
    # FACT ADS
    # =====================================================

    ads = run_ads_pipeline(
        calendar=calendar,
        campaigns=campaigns,
    )

    display_sample(
        "Fact Ads",
        ads,
    )

    # =====================================================
    # FACT SALES
    # =====================================================

    sales = run_sales_pipeline(
        calendar=calendar,
        leads=leads,
        products=products,
    )

    display_sample(
        "Fact Sales",
        sales,
    )

    print()
    print(LINE)
    print("ALL FACT TABLES GENERATED SUCCESSFULLY")
    print(LINE)

    print()
    print(LINE)
    print("PROJECT COMPLETED SUCCESSFULLY")
    print(LINE)


if __name__ == "__main__":
    main()
