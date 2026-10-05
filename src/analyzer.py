def calculate_kpis(df):
    total_revenue = df["revenue"].sum()
    total_quantity = df["quantity"].sum()
    average_order_value = df["revenue"].mean()

    return {
        "total_revenue": total_revenue,
        "total_quantity": total_quantity,
        "average_order_value": average_order_value
    }


def product_performance(df):
    return (
        df.groupby("product")
        .agg(
            revenue=("revenue", "sum"),
            quantity=("quantity", "sum")
        )
        .sort_values("revenue", ascending=False)
    )


def region_performance(df):
    return (
        df.groupby("region")
        .agg(
            revenue=("revenue", "sum"),
            quantity=("quantity", "sum")
        )
        .sort_values("revenue", ascending=False)
    )


def monthly_sales(df):
    return (
        df.groupby(df["date"].dt.to_period("M"))["revenue"]
        .sum()
        .sort_index()
    )


def top_products(df, n=5):
    return (
        df.groupby("product")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
    )