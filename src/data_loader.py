import pandas as pd


REQUIRED_COLUMNS = [
    "date",
    "product",
    "category",
    "region",
    "quantity",
    "unit_price",
    "revenue",
]


def validate_sales_data(df):
    """
    Validate sales data before sending it to the analysis pipeline.
    """

    # Required columns
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {', '.join(missing_columns)}"
        )

    # Remove completely empty rows
    df = df.dropna(how="all").copy()

    # Required fields cannot be empty
    required_value_columns = [
        "date",
        "product",
        "category",
        "region",
        "quantity",
        "unit_price",
        "revenue",
    ]

    missing_value_counts = df[required_value_columns].isnull().sum()

    columns_with_missing_values = (
        missing_value_counts[missing_value_counts > 0]
    )

    if not columns_with_missing_values.empty:
        details = ", ".join(
            f"{column}: {count}"
            for column, count in columns_with_missing_values.items()
        )

        raise ValueError(
            f"Missing values detected: {details}"
        )

    # Numeric columns
    numeric_columns = [
        "quantity",
        "unit_price",
        "revenue",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # Check invalid numeric conversions
    if df[numeric_columns].isnull().any().any():
        raise ValueError(
            "Invalid numeric values detected."
        )

    # Quantity must be positive
    if (df["quantity"] <= 0).any():
        raise ValueError(
            "Quantity must be greater than zero."
        )

    # Unit price must be positive
    if (df["unit_price"] <= 0).any():
        raise ValueError(
            "Unit price must be greater than zero."
        )

    # Revenue must be positive
    if (df["revenue"] <= 0).any():
        raise ValueError(
            "Revenue must be greater than zero."
        )

    # Revenue consistency check
    expected_revenue = (
        df["quantity"] * df["unit_price"]
    ).round(2)

    actual_revenue = df["revenue"].round(2)

    if not expected_revenue.equals(actual_revenue):
        raise ValueError(
            "Revenue values do not match "
            "quantity × unit_price."
        )

    return df


def load_sales_data(file_path):
    """
    Load and validate sales data from CSV.
    """

    df = pd.read_csv(file_path)

    # Convert date column
    df["date"] = pd.to_datetime(
        df["date"],
        errors="coerce"
    )

    # Check invalid dates
    if df["date"].isnull().any():
        raise ValueError(
            "Invalid date values detected."
        )

    # Validate dataset
    df = validate_sales_data(df)

    return df