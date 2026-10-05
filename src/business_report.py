def generate_business_report(
    kpis,
    product_data,
    region_data,
    monthly_data
):
    total_revenue = kpis["total_revenue"]
    total_quantity = kpis["total_quantity"]
    average_revenue = kpis["average_order_value"]

    best_product = product_data["revenue"].idxmax()
    best_product_revenue = product_data["revenue"].max()

    best_region = region_data["revenue"].idxmax()
    best_region_revenue = region_data["revenue"].max()

    best_month = monthly_data.idxmax()
    best_month_revenue = monthly_data.max()

    worst_month = monthly_data.idxmin()
    worst_month_revenue = monthly_data.min()

    report = f"""
AI SALES ANALYTICS - BUSINESS REPORT
====================================

KEY PERFORMANCE INDICATORS
--------------------------
Total Revenue: {total_revenue:,.2f} TL
Total Quantity: {total_quantity}
Average Revenue per Transaction: {average_revenue:,.2f} TL


PRODUCT PERFORMANCE
-------------------
Best Performing Product: {best_product}
Product Revenue: {best_product_revenue:,.2f} TL


REGIONAL PERFORMANCE
--------------------
Best Performing Region: {best_region}
Regional Revenue: {best_region_revenue:,.2f} TL


MONTHLY PERFORMANCE
--------------------
Best Month: {best_month}
Best Month Revenue: {best_month_revenue:,.2f} TL

Lowest Month: {worst_month}
Lowest Month Revenue: {worst_month_revenue:,.2f} TL


BUSINESS INSIGHTS
-----------------
1. {best_product} is the highest-revenue product in the dataset.

2. {best_region} is the strongest-performing region based on revenue.

3. {best_month} generated the highest monthly revenue.

4. {worst_month} generated the lowest monthly revenue.

5. The dataset contains {total_quantity} units sold
   and generated {total_revenue:,.2f} TL in total revenue.
"""

    return report