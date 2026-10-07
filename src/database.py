import sqlite3
import pandas as pd


DB_PATH = "database/sales.db"


def create_database():
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE NOT NULL,
            product TEXT NOT NULL,
            category TEXT NOT NULL,
            region TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            revenue REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_sales_data(df):
    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("DELETE FROM sales")

    df.to_sql(
        "sales",
        connection,
        if_exists="append",
        index=False
    )

    connection.commit()
    connection.close()


def load_sales_data_from_database():
    connection = sqlite3.connect(DB_PATH)

    query = """
        SELECT
            date,
            product,
            category,
            region,
            quantity,
            unit_price,
            revenue
        FROM sales
    """

    df = pd.read_sql_query(query, connection)

    connection.close()

    df["date"] = pd.to_datetime(df["date"])

    return df