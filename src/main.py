from report import (
    create_monthly_sales_chart,
    create_product_sales_chart,
    create_region_sales_chart
)
from data_loader import load_sales_data
from analyzer import (
    calculate_kpis,
    product_performance,
    region_performance,
    monthly_sales,
    top_products
)
from business_report import generate_business_report
from ai_report import generate_ai_report
import report

DATA_PATH = "data/sales_data.csv"


def main():
    df = load_sales_data(DATA_PATH)

    print("\n===== AI SALES ANALYTICS =====")

    kpis = calculate_kpis(df)

    print("\n--- KPIs ---")
    print(f"Total Revenue: {kpis['total_revenue']:,.2f} TL")
    print(f"Total Quantity: {kpis['total_quantity']}")
    print(f"Average Order Value: {kpis['average_order_value']:,.2f} TL")

    print("\n--- Product Performance ---")
    print(product_performance(df))

    print("\n--- Region Performance ---")
    print(region_performance(df))

    print("\n--- Monthly Sales ---")
    print(monthly_sales(df))

    print("\n--- Top Products ---")
    print(top_products(df))
    create_monthly_sales_chart(monthly_sales(df))
    create_product_sales_chart(product_performance(df))
    create_region_sales_chart(region_performance(df))

    print("\nCharts generated successfully.")
    report = generate_business_report(
        kpis,
        product_performance(df),
        region_performance(df),
        monthly_sales(df)
    )

    print("\n--- BUSINESS REPORT ---")
    print(report)

    with open("reports/business_report.txt", "w", encoding="utf-8") as file:
     file.write(report)

print("\nBusiness report generated successfully.")

print("\n--- AI EXECUTIVE REPORT ---")

ai_report = generate_ai_report(report)

print(ai_report)

with open("reports/ai_business_report.txt", "w", encoding="utf-8") as file:
    file.write(ai_report)

print("\nAI business report generated successfully.")

if __name__ == "__main__":
    main()