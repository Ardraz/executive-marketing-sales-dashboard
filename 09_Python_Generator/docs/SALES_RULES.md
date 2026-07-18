# SALES_RULES.md

# ==========================================================
# SALES BUSINESS RULES
# Executive Marketing & Sales Dashboard
# ==========================================================

Version : 1.0.0

Status : APPROVED

Last Updated : Before Sprint 16

This document defines the business rules
used to generate the Fact_Sales table.

==========================================================
1. OBJECTIVE
==========================================================

Fact_Sales represents successful sales
generated from qualified marketing leads.

Each sales transaction
must simulate a realistic business process.

==========================================================
2. SALES PROCESS
==========================================================

Customer

↓

Marketing Campaign

↓

Lead Generated

↓

Sales Representative Follow-up

↓

Opportunity

↓

Closed Won

↓

Sales Transaction

Only successful sales
are stored in Fact_Sales.

==========================================================
3. SALES SOURCE
==========================================================

Fact_Sales is generated
from Fact_Leads.

Fact_Sales must NOT create
new customers.

Fact_Sales must NOT create
new products.

Fact_Sales must NOT create
new campaigns.

==========================================================
4. ELIGIBLE LEADS
==========================================================

Only leads with status:

Converted

are eligible
to become sales.

All other lead statuses
must be ignored.

==========================================================
5. SALES DATE
==========================================================

SalesDate

must be

greater than or equal to

LeadDate.

SalesDate

must not occur
before the lead exists.

==========================================================
6. SALES REPRESENTATIVE
==========================================================

SalesRepID

must be inherited
from Fact_Leads.

Sales ownership
cannot change.

==========================================================
7. CUSTOMER
==========================================================

CustomerID

must be inherited
from Fact_Leads.

==========================================================
8. PRODUCT
==========================================================

ProductID

must be inherited
from Fact_Leads.

==========================================================
9. CAMPAIGN
==========================================================

CampaignID

must be inherited
from Fact_Leads.

==========================================================
10. SALES QUANTITY
==========================================================

Quantity

Minimum

1

Maximum

5

Quantity
represents the number
of purchased licenses
or products.

==========================================================
11. UNIT PRICE
==========================================================

UnitPrice

is inherited from

Dim_Product

(ListPrice)

==========================================================
12. DISCOUNT
==========================================================

Discount

Minimum

0%

Maximum

30%

Discount simulation
depends on customer segment
and campaign promotion.

==========================================================
13. GROSS SALES
==========================================================

Formula

GrossSales

=

Quantity

×

UnitPrice

==========================================================
14. DISCOUNT AMOUNT
==========================================================

Formula

DiscountAmount

=

GrossSales

×

Discount

==========================================================
15. NET SALES
==========================================================

Formula

NetSales

=

GrossSales

−

DiscountAmount

==========================================================
16. UNIT COST
==========================================================

UnitCost

is inherited
from Dim_Product.

==========================================================
17. TOTAL COST
==========================================================

Formula

TotalCost

=

Quantity

×

UnitCost

==========================================================
18. GROSS PROFIT
==========================================================

Formula

GrossProfit

=

NetSales

−

TotalCost

==========================================================
19. PAYMENT METHOD
==========================================================

Allowed Values

Credit Card

Bank Transfer

Virtual Account

E-Wallet

Corporate Invoice

==========================================================
20. PAYMENT STATUS
==========================================================

Allowed Values

Paid

Pending

Failed

Distribution

Paid

85%

Pending

10%

Failed

5%

==========================================================
21. ORDER STATUS
==========================================================

Allowed Values

Completed

Processing

Cancelled

Distribution

Completed

90%

Processing

7%

Cancelled

3%

==========================================================
22. SALES CHANNEL
==========================================================

Allowed Values

Website

Sales Representative

Partner

Referral

Marketplace

==========================================================
23. INVOICE NUMBER
==========================================================

InvoiceNumber

must be unique.

Recommended format

INV-2025-000001

==========================================================
24. SALES CODE
==========================================================

SalesCode

must be unique.

Recommended format

SAL000001

==========================================================
25. RETURN POLICY
==========================================================

Version 1

Returns
are NOT simulated.

This feature
may be added
in Version 2.

==========================================================
26. REFUND POLICY
==========================================================

Version 1

Refunds
are NOT simulated.

==========================================================
27. TAX POLICY
==========================================================

Version 1

Tax
is NOT simulated.

NetSales
already represents
the final transaction value.

==========================================================
28. FACT_SALES STRUCTURE
==========================================================

SalesID

Primary Key

----------------------------------------------------------

SalesCode

Business Key

----------------------------------------------------------

DateKey

FK

Dim_Date

----------------------------------------------------------

CustomerID

FK

Dim_Customer

----------------------------------------------------------

ProductID

FK

Dim_Product

----------------------------------------------------------

CampaignID

FK

Dim_Campaign

----------------------------------------------------------

SalesRepID

FK

Dim_SalesRep

----------------------------------------------------------

Quantity

----------------------------------------------------------

UnitPrice

----------------------------------------------------------

GrossSales

----------------------------------------------------------

Discount

----------------------------------------------------------

DiscountAmount

----------------------------------------------------------

NetSales

----------------------------------------------------------

UnitCost

----------------------------------------------------------

TotalCost

----------------------------------------------------------

GrossProfit

----------------------------------------------------------

PaymentMethod

----------------------------------------------------------

PaymentStatus

----------------------------------------------------------

OrderStatus

----------------------------------------------------------

SalesChannel

----------------------------------------------------------

InvoiceNumber

==========================================================
29. VALIDATION RULES
==========================================================

Every sales record must satisfy:

✓ Customer exists

✓ Product exists

✓ Campaign exists

✓ SalesRep exists

✓ Quantity > 0

✓ UnitPrice > 0

✓ NetSales ≥ 0

✓ GrossProfit calculated correctly

✓ InvoiceNumber unique

✓ SalesCode unique

==========================================================
30. IMPROVEMENT V2
==========================================================

Future enhancements

• Multiple products
per invoice

• Refund simulation

• Product returns

• Shipping cost

• VAT / Sales Tax

• Coupon system

• Loyalty points

• Installment payment

• Subscription renewal

• Multi-currency support

==========================================================
END OF DOCUMENT
==========================================================