from datetime import datetime


def generate_business_report(
    kpis,
    product_data,
    region_data,
    monthly_data,
    data_end_date=None
):
    total_revenue = kpis["total_revenue"]
    total_quantity = kpis["total_quantity"]
    average_revenue = kpis["average_order_value"]

    best_product = product_data["revenue"].idxmax()
    best_product_revenue = product_data["revenue"].max()

    best_region = region_data["revenue"].idxmax()
    best_region_revenue = region_data["revenue"].max()

    current_period = datetime.now().strftime("%Y-%m")
    latest_period = str(monthly_data.index.max())

    # Check whether the latest month is the current/incomplete month
    is_partial_month = latest_period == current_period

    if is_partial_month and len(monthly_data) > 1:
        comparison_data = monthly_data.iloc[:-1]
    else:
        comparison_data = monthly_data

    best_month = comparison_data.idxmax()
    best_month_revenue = comparison_data.max()

    worst_month = comparison_data.idxmin()
    worst_month_revenue = comparison_data.min()

    latest_month_revenue = monthly_data.iloc[-1]

    if data_end_date is not None:
        data_end_text = data_end_date.strftime("%Y-%m-%d")
    else:
        data_end_text = "Unknown"

    if is_partial_month:
        latest_month_status = (
            f"{latest_period} is the current month and contains "
            f"partial data through {data_end_text}."
        )
    else:
        latest_month_status = (
            f"{latest_period} is the latest completed reporting month."
        )

    report = f"""
AI SALES ANALYTICS - BUSINESS REPORT
====================================

DATA PERIOD
-----------
Data Through: {data_end_text}
Latest Month Status: {latest_month_status}

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
-------------------
Best Completed Month: {best_month}
Best Completed Month Revenue: {best_month_revenue:,.2f} TL

Lowest Completed Month: {worst_month}
Lowest Completed Month Revenue: {worst_month_revenue:,.2f} TL

Latest Month Revenue: {latest_month_revenue:,.2f} TL

BUSINESS INSIGHTS
-----------------
1. {best_product} is the highest-revenue product in the dataset.
2. {best_region} is the strongest-performing region based on revenue.
3. {best_month} generated the highest revenue among completed months.
4. {worst_month} generated the lowest revenue among completed months.
5. The latest month's data may be incomplete and should not be directly
   compared with completed months.
6. The dataset contains {total_quantity} units sold and generated
   {total_revenue:,.2f} TL in total revenue.
"""

    return report