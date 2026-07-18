"""
Sales Fact Generator
"""

import random
from datetime import datetime, timedelta

import pandas as pd

from business.sales_rules import (
    MIN_QUANTITY,
    MAX_QUANTITY,
    DISCOUNT_BY_QUANTITY,
    PAYMENT_METHOD,
    PAYMENT_STATUS,
    ORDER_STATUS,
    SALES_CHANNEL,
    SALES_CODE_PREFIX,
    INVOICE_PREFIX,
    BUSINESS_HOUR_START,
    BUSINESS_HOUR_END,
    BUSINESS_MINUTE_START,
    BUSINESS_MINUTE_END,
    BUSINESS_SECOND_START,
    BUSINESS_SECOND_END,
    MIN_CLOSE_DAYS,
    MAX_CLOSE_DAYS,
    calculate_gross_sales,
    calculate_discount_amount,
    calculate_net_sales,
    calculate_total_cost,
    calculate_gross_profit,
)

from core.config import RANDOM_SEED

random.seed(RANDOM_SEED)


def weighted_choice(options: dict):
    """
    Select one value using weighted probability.
    """

    return random.choices(
        population=list(options.keys()),
        weights=list(options.values()),
        k=1,
    )[0]


def random_row(dataframe: pd.DataFrame) -> pd.Series:
    """
    Return one random row from DataFrame.
    """

    return dataframe.sample(
        n=1,
        replace=False,
    ).iloc[0]


def generate_sales(
    calendar: pd.DataFrame,
    leads: pd.DataFrame,
    products: pd.DataFrame,
) -> pd.DataFrame:
    """
    Generate Fact_Sales.
    """

    sales = []

    converted_leads = leads[leads["LeadStatus"] == "Converted"]

    if converted_leads.empty:
        raise ValueError("No converted leads available.")

    active_products = products[products["Status"] == "Active"]

    if active_products.empty:
        raise ValueError("No active product available.")

    sales_id = 1

    for _, lead in converted_leads.iterrows():

        # ==============================================
        # Product Lookup
        # ==============================================

        product = active_products[active_products["ProductID"] == lead["ProductID"]]

        if product.empty:
            continue

        product = product.iloc[0]

        # ==============================================
        # Quantity
        # ==============================================

        quantity = random.randint(
            MIN_QUANTITY,
            MAX_QUANTITY,
        )

        # ==============================================
        # Unit Price
        # ==============================================

        unit_price = float(product["ListPrice"])

        # ==============================================
        # Unit Cost
        # ==============================================

        unit_cost = float(product["UnitCost"])

        # ==============================================
        # Gross Sales
        # ==============================================

        gross_sales = calculate_gross_sales(
            quantity=quantity,
            unit_price=unit_price,
        )

        # ==============================================
        # Discount
        # ==============================================

        min_discount, max_discount = DISCOUNT_BY_QUANTITY[quantity]

        discount_percent = round(
            random.uniform(
                min_discount,
                max_discount,
            ),
            2,
        )

        # ==============================================
        # Discount Amount
        # ==============================================

        discount_amount = calculate_discount_amount(
            gross_sales=gross_sales,
            discount_percent=discount_percent,
        )

        # ==============================================
        # Net Sales
        # ==============================================

        net_sales = calculate_net_sales(
            gross_sales=gross_sales,
            discount_amount=discount_amount,
        )
        # ==============================================
        # Total Cost
        # ==============================================

        total_cost = calculate_total_cost(
            quantity=quantity,
            unit_cost=unit_cost,
        )

        # ==============================================
        # Gross Profit
        # ==============================================

        gross_profit = calculate_gross_profit(
            net_sales=net_sales,
            total_cost=total_cost,
        )

        # ==============================================
        # Margin Amount
        # ==============================================

        margin_amount = gross_profit

        # ==============================================
        # Margin Percent
        # ==============================================

        if net_sales > 0:

            margin_percent = round(
                (gross_profit / net_sales) * 100,
                2,
            )

        else:

            margin_percent = 0

        # ==============================================
        # Sales Date
        # ==============================================

        lead_date = pd.Timestamp(lead["LeadDate"])

        close_days = random.randint(
            MIN_CLOSE_DAYS,
            MAX_CLOSE_DAYS,
        )

        sales_date = lead_date + timedelta(days=close_days)

        # ==============================================
        # DateKey Lookup
        # ==============================================

        calendar_row = calendar[calendar["Date"] == sales_date.normalize()]

        if calendar_row.empty:
            continue

        date_key = int(calendar_row.iloc[0]["DateKey"])

        # ==============================================
        # Sales Timestamp
        # ==============================================

        sales_timestamp = datetime(
            year=sales_date.year,
            month=sales_date.month,
            day=sales_date.day,
            hour=random.randint(
                BUSINESS_HOUR_START,
                BUSINESS_HOUR_END,
            ),
            minute=random.randint(
                BUSINESS_MINUTE_START,
                BUSINESS_MINUTE_END,
            ),
            second=random.randint(
                BUSINESS_SECOND_START,
                BUSINESS_SECOND_END,
            ),
        )

        # ==============================================
        # Payment Method
        # ==============================================

        payment_method = weighted_choice(
            PAYMENT_METHOD,
        )

        # ==============================================
        # Payment Status
        # ==============================================

        payment_status = weighted_choice(
            PAYMENT_STATUS,
        )

        # ==============================================
        # Order Status
        # ==============================================

        order_status = weighted_choice(
            ORDER_STATUS,
        )

        # ==============================================
        # Sales Channel
        # ==============================================

        sales_channel = weighted_choice(
            SALES_CHANNEL,
        )

        # ==============================================
        # Sales Code
        # ==============================================

        sales_code = f"{SALES_CODE_PREFIX}-" f"{sales_date.year}-" f"{sales_id:06}"

        # ==============================================
        # Invoice Number
        # ==============================================

        invoice_number = (
            f"{INVOICE_PREFIX}-" f"{sales_date.strftime('%Y%m%d')}-" f"{sales_id:06}"
        )
        # ==============================================
        # Build Sales Record
        # ==============================================

        sales_record = {
            # ------------------------------------------
            # Primary Key
            # ------------------------------------------
            "SalesID": sales_id,
            "SalesCode": sales_code,
            "InvoiceNumber": invoice_number,
            # ------------------------------------------
            # Date
            # ------------------------------------------
            "DateKey": date_key,
            "SalesDate": sales_date.date(),
            "SalesTimestamp": sales_timestamp,
            # ------------------------------------------
            # Dimension Keys
            # ------------------------------------------
            "CustomerID": lead["CustomerID"],
            "CampaignID": lead["CampaignID"],
            "ProductID": lead["ProductID"],
            "SalesRepID": lead["SalesRepID"],
            # ------------------------------------------
            # Sales Information
            # ------------------------------------------
            "Quantity": quantity,
            "UnitPrice": unit_price,
            "UnitCost": unit_cost,
            # ------------------------------------------
            # Discount
            # ------------------------------------------
            "DiscountPercent": discount_percent,
            "DiscountAmount": discount_amount,
            # ------------------------------------------
            # Financial
            # ------------------------------------------
            "GrossSales": gross_sales,
            "NetSales": net_sales,
            "TotalCost": total_cost,
            "GrossProfit": gross_profit,
            "MarginAmount": margin_amount,
            "MarginPercent": margin_percent,
            # ------------------------------------------
            # Transaction
            # ------------------------------------------
            "PaymentMethod": payment_method,
            "PaymentStatus": payment_status,
            "OrderStatus": order_status,
            "SalesChannel": sales_channel,
        }

        sales.append(sales_record)

        sales_id += 1

    # ==================================================
    # Create DataFrame
    # ==================================================

    dataframe = pd.DataFrame(
        sales,
        columns=[
            "SalesID",
            "SalesCode",
            "InvoiceNumber",
            "DateKey",
            "SalesDate",
            "SalesTimestamp",
            "CustomerID",
            "CampaignID",
            "ProductID",
            "SalesRepID",
            "Quantity",
            "UnitPrice",
            "UnitCost",
            "DiscountPercent",
            "DiscountAmount",
            "GrossSales",
            "NetSales",
            "TotalCost",
            "GrossProfit",
            "MarginAmount",
            "MarginPercent",
            "PaymentMethod",
            "PaymentStatus",
            "OrderStatus",
            "SalesChannel",
        ],
    )

    dataframe = dataframe.sort_values(by="SalesID").reset_index(drop=True)

    return dataframe
