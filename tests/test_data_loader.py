import unittest
import pandas as pd

from src.data_loader import validate_sales_data


class TestDataValidation(unittest.TestCase):

    def create_valid_data(self):
        return pd.DataFrame({
            "date": ["2026-01-01", "2026-01-02"],
            "product": ["Laptop", "Mouse"],
            "category": ["Electronics", "Accessories"],
            "region": ["Istanbul", "Ankara"],
            "quantity": [2, 3],
            "unit_price": [35000.00, 1200.00],
            "revenue": [70000.00, 3600.00]
        })

    def test_valid_data(self):
        df = self.create_valid_data()

        validated_df = validate_sales_data(df)

        self.assertEqual(len(validated_df), 2)

    def test_missing_column(self):
        df = self.create_valid_data()

        df = df.drop(columns=["region"])

        with self.assertRaises(ValueError):
            validate_sales_data(df)

    def test_missing_value(self):
        df = self.create_valid_data()

        df.loc[0, "product"] = None

        with self.assertRaises(ValueError):
            validate_sales_data(df)

    def test_negative_quantity(self):
        df = self.create_valid_data()

        df.loc[0, "quantity"] = -1

        with self.assertRaises(ValueError):
            validate_sales_data(df)

    def test_negative_unit_price(self):
        df = self.create_valid_data()

        df.loc[0, "unit_price"] = -100

        with self.assertRaises(ValueError):
            validate_sales_data(df)

    def test_negative_revenue(self):
        df = self.create_valid_data()

        df.loc[0, "revenue"] = -500

        with self.assertRaises(ValueError):
            validate_sales_data(df)

    def test_revenue_mismatch(self):
        df = self.create_valid_data()

        df.loc[0, "revenue"] = 1000

        with self.assertRaises(ValueError):
            validate_sales_data(df)


if __name__ == "__main__":
    unittest.main()