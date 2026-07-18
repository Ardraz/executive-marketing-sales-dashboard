from pipeline.date_pipeline import run_date_pipeline
from pipeline.customer_pipeline import run_customer_pipeline
from pipeline.product_pipeline import run_product_pipeline
from pipeline.campaign_pipeline import run_campaign_pipeline
from pipeline.salesrep_pipeline import run_salesrep_pipeline
from pipeline.leads_pipeline import run_leads_pipeline
from pipeline.ads_pipeline import run_ads_pipeline
from pipeline.sales_pipeline import run_sales_pipeline

from edqe.audit_runner import run_all_audits

calendar = run_date_pipeline()

customers = run_customer_pipeline()

products = run_product_pipeline()

campaigns = run_campaign_pipeline()

sales_reps = run_salesrep_pipeline()

leads = run_leads_pipeline(
    calendar=calendar,
    customers=customers,
    products=products,
    campaigns=campaigns,
    sales_reps=sales_reps,
)

ads = run_ads_pipeline(
    calendar=calendar,
    campaigns=campaigns,
)

sales = run_sales_pipeline(
    calendar=calendar,
    leads=leads,
    products=products,
)

dataframes = {
    "Dim_Date": calendar,
    "Dim_Customer": customers,
    "Dim_Product": products,
    "Dim_Campaign": campaigns,
    "Dim_SalesRep": sales_reps,
    "Fact_Leads": leads,
    "Fact_Ads": ads,
    "Fact_Sales": sales,
}

run_all_audits(dataframes)
