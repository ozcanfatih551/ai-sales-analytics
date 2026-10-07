import os
import tempfile
import unittest

import pandas as pd

import src.database as database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()

        self.original_db_path = database.DB_PATH

        database.DB_PATH = os.path.join(
            self.temp_directory.name,
            "test_sales.db"
        )

    def tearDown(self):
        database.DB_PATH = self.original_db_path

        self.temp_directory.cleanup()

    def create_test_data(self):
        return pd.DataFrame({
            "date": pd.to_datetime([
                "2026-01-01",
                "2026-01-02"
            ]),
            "product": [
                "Laptop",
                "Mouse"
            ],
            "category": [
                "Electronics",
                "Accessories"
            ],
            "region": [
                "Istanbul",
                "Ankara"
            ],
            "quantity": [
                2,
                3
            ],
            "unit_price": [
                35000.00,
                1200.00
            ],
            "revenue": [
                70000.00,
                3600.00
            ]
        })

    def test_create_database(self):
        database.create_database()

        self.assertTrue(
            os.path.exists(database.DB_PATH)
        )

    def test_save_and_load_sales_data(self):
        df = self.create_test_data()

        database.create_database()
        database.save_sales_data(df)

        loaded_df = database.load_sales_data_from_database()

        self.assertEqual(len(loaded_df), 2)

        self.assertEqual(
            loaded_df["product"].tolist(),
            ["Laptop", "Mouse"]
        )

        self.assertEqual(
            loaded_df["quantity"].tolist(),
            [2, 3]
        )


if __name__ == "__main__":
    unittest.main()