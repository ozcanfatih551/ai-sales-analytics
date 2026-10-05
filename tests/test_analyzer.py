import unittest
import pandas as pd

from src.analyzer import (
    calculate_kpis,
    product_performance,
    region_performance,
    monthly_sales,
    top_products
)


class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            "date": pd.to_datetime([
                "2026-01-01",
                "2026-01-02",
                "2026-02-01"
            ]),
            "product": [
                "Laptop",
                "Phone",
                "Laptop"
            ],
            "category": [
                "Electronics",
                "Electronics",
                "Electronics"
            ],
            "region": [
                "Istanbul",
                "Ankara",
                "Istanbul"
            ],
            "quantity": [
                2,
                3,
                1
            ],
            "unit_price": [
                35000,
                22000,
                35000
            ],
            "revenue": [
                70000,
                66000,
                35000
            ]
        })

    def test_kpis(self):
        kpis = calculate_kpis(self.df)

        self.assertEqual(kpis["total_revenue"], 171000)
        self.assertEqual(kpis["total_quantity"], 6)

    def test_product_performance(self):
        result = product_performance(self.df)

        self.assertEqual(result.loc["Laptop", "revenue"], 105000)

    def test_region_performance(self):
        result = region_performance(self.df)

        self.assertEqual(result.loc["Istanbul", "revenue"], 105000)

    def test_monthly_sales(self):
        result = monthly_sales(self.df)

        self.assertEqual(result.iloc[0], 136000)
        self.assertEqual(result.iloc[1], 35000)

    def test_top_products(self):
        result = top_products(self.df, 1)

        self.assertEqual(result.index[0], "Laptop")


if __name__ == "__main__":
    unittest.main()