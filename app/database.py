import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE = BASE_DIR / "northstar.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_number TEXT UNIQUE NOT NULL,
            customer_name TEXT NOT NULL,
            product TEXT NOT NULL,
            status TEXT NOT NULL,
            expected_delivery TEXT NOT NULL
        )
    """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS returns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_number TEXT NOT NULL,
            product TEXT NOT NULL,
            return_status TEXT NOT NULL,
            instructions TEXT NOT NULL
        )
    """)

    existing_orders = connection.execute(
        "SELECT COUNT(*) AS count FROM orders"
    ).fetchone()["count"]

    if existing_orders == 0:
        connection.executemany("""
            INSERT INTO orders
            (order_number, customer_name, product, status, expected_delivery)
            VALUES (?, ?, ?, ?, ?)
        """, [
            (
                "NS1001",
                "John Kamau",
                "Wireless Headphones",
                "Shipped",
                "2026-08-16"
            ),
            (
                "NS1002",
                "Mary Wanjiku",
                "Laptop Backpack",
                "Processing",
                "2026-08-19"
            ),
            (
                "NS1003",
                "David Otieno",
                "Mechanical Keyboard",
                "Delivered",
                "2026-08-10"
            )
        ])

    existing_returns = connection.execute(
        "SELECT COUNT(*) AS count FROM returns"
    ).fetchone()["count"]

    if existing_returns == 0:
        connection.executemany("""
            INSERT INTO returns
            (order_number, product, return_status, instructions)
            VALUES (?, ?, ?, ?)
        """, [
            (
                "NS1001",
                "Wireless Headphones",
                "Eligible",
                "Contact support within 30 days and provide the order number."
            ),
            (
                "NS1002",
                "Laptop Backpack",
                "Eligible",
                "Package the item securely and submit a return request."
            ),
            (
                "NS1003",
                "Mechanical Keyboard",
                "Completed",
                "The return for this order has already been completed."
            )
        ])

    connection.commit()
    connection.close()
