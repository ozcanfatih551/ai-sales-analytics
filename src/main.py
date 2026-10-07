from database import (
    create_database,
    save_sales_data,
    load_sales_data_from_database
)

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


DATA_PATH = "data/sales_data.csv"


def main():
    # Load and validate CSV data
    df = load_sales_data(DATA_PATH)

    # Save data to SQLite database
    create_database()
    save_sales_data(df)

    # Load data back from SQLite
    df = load_sales_data_from_database()

    print("\nSales data loaded successfully from the database.")
    print(f"Database records: {len(df)}")

    print("\n===== AI SALES ANALYTICS =====")

    # KPI analysis
    kpis = calculate_kpis(df)

    print("\n--- KPIs ---")
    print(f"Total Revenue: {kpis['total_revenue']:,.2f} TL")
    print(f"Total Quantity: {kpis['total_quantity']}")
    print(
        f"Average Revenue per Transaction: "
        f"{kpis['average_order_value']:,.2f} TL"
    )

    # Product analysis
    product_data = product_performance(df)

    print("\n--- Product Performance ---")
    print(product_data)

    # Region analysis
    region_data = region_performance(df)

    print("\n--- Region Performance ---")
    print(region_data)

    # Monthly analysis
    monthly_data = monthly_sales(df)

    print("\n--- Monthly Sales ---")
    print(monthly_data)

    # Top products
    print("\n--- Top Products ---")
    print(top_products(df))

    # Generate charts
    create_monthly_sales_chart(monthly_data)
    create_product_sales_chart(product_data)
    create_region_sales_chart(region_data)

    print("\nCharts generated successfully.")

    # Generate business report
    business_report_text = generate_business_report(
        kpis,
        product_data,
        region_data,
        monthly_data,
        data_end_date=df["date"].max()
    )

    print("\n--- BUSINESS REPORT ---")
    print(business_report_text)

    with open(
        "reports/business_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(business_report_text)

    print("\nBusiness report generated successfully.")

    # Generate AI executive report
    print("\n--- AI EXECUTIVE REPORT ---")

    ai_report = generate_ai_report(
        business_report_text
    )

    print(ai_report)

    with open(
        "reports/ai_business_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(ai_report)

    print("\nAI business report generated successfully.")


if __name__ == "__main__":
    main()