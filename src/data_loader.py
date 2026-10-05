import pandas as pd


REQUIRED_COLUMNS = [
    "date",
    "product",
    "category",
    "region",
    "quantity",
    "unit_price",
    "revenue"
]


def load_sales_data(file_path):
    df = pd.read_csv(file_path)

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {', '.join(missing_columns)}"
        )

    df["date"] = pd.to_datetime(df["date"])

    numeric_columns = [
        "quantity",
        "unit_price",
        "revenue"
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df = df.dropna()

    return df