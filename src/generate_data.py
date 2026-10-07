import csv
import random
from datetime import datetime, timedelta


PRODUCTS = {
    "Laptop": ("Electronics", 35000),
    "Phone": ("Electronics", 22000),
    "Monitor": ("Electronics", 8500),
    "Headphones": ("Electronics", 3500),
    "Keyboard": ("Accessories", 2500),
    "Mouse": ("Accessories", 1200),
    "Tablet": ("Electronics", 15000),
    "Webcam": ("Accessories", 3000),
}

REGIONS = [
    "Istanbul",
    "Ankara",
    "Izmir",
    "Bursa",
    "Antalya",
    "Adana",
]

START_DATE = datetime(2026, 1, 1)
END_DATE = datetime.now()
NUMBER_OF_ROWS = 1000


def generate_sales_data():
    rows = []

    for _ in range(NUMBER_OF_ROWS):
        total_days = (END_DATE - START_DATE).days
        random_days = random.randint(0, total_days)
        date = START_DATE + timedelta(days=random_days)

        product = random.choice(list(PRODUCTS.keys()))
        category, base_price = PRODUCTS[product]

        region = random.choice(REGIONS)

        quantity = random.randint(1, 10)

        price_variation = random.uniform(0.90, 1.10)
        unit_price = round(base_price * price_variation, 2)

        revenue = round(quantity * unit_price, 2)

        rows.append([
            date.strftime("%Y-%m-%d"),
            product,
            category,
            region,
            quantity,
            unit_price,
            revenue
        ])

    return rows


def save_data(rows):
    with open("data/sales_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "date",
            "product",
            "category",
            "region",
            "quantity",
            "unit_price",
            "revenue"
        ])

        writer.writerows(rows)


if __name__ == "__main__":
    data = generate_sales_data()
    save_data(data)

    print(f"{len(data)} sales records generated successfully.")