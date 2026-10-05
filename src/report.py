import os
import matplotlib.pyplot as plt


REPORTS_DIR = "reports"


def create_reports_directory():
    os.makedirs(REPORTS_DIR, exist_ok=True)


def create_monthly_sales_chart(monthly_sales):
    create_reports_directory()

    plt.figure(figsize=(10, 6))

    months = monthly_sales.index.astype(str)
    revenue = monthly_sales.values

    plt.plot(months, revenue, marker="o")

    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue (TL)")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        os.path.join(REPORTS_DIR, "monthly_revenue.png")
    )

    plt.close()


def create_product_sales_chart(product_performance):
    create_reports_directory()

    plt.figure(figsize=(10, 6))

    products = product_performance.index
    revenue = product_performance["revenue"]

    plt.bar(products, revenue)

    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue (TL)")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        os.path.join(REPORTS_DIR, "product_revenue.png")
    )

    plt.close()


def create_region_sales_chart(region_performance):
    create_reports_directory()

    plt.figure(figsize=(10, 6))

    regions = region_performance.index
    revenue = region_performance["revenue"]

    plt.bar(regions, revenue)

    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue (TL)")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(
        os.path.join(REPORTS_DIR, "region_revenue.png")
    )

    plt.close()