import pandas as pd
import sqlite3
from pathlib import Path



PROJECT_ROOT = Path(__file__).resolve().parents[2]
DB_DIR = PROJECT_ROOT / "database" 
DB_PATH = DB_DIR / "ecommerce.db"
CLEAN_DIR = PROJECT_ROOT / "data" / "clean"
SCHEMA_PATH = PROJECT_ROOT / "sql" / "schema.sql"   

# Make sure the folder exists
DB_DIR.mkdir(parents=True, exist_ok=True)

# open sqlite connection
conn = sqlite3.connect(DB_PATH)

with open(SCHEMA_PATH, "r", encoding="utf-8") as file: 
    conn.executescript(file.read())

# Read cleaned CSVs
orders = pd.read_csv(CLEAN_DIR / "orders.csv")
products = pd.read_csv(CLEAN_DIR / "products.csv")
customers = pd.read_csv(CLEAN_DIR / "customers.csv")
order_items = pd.read_csv(CLEAN_DIR / "order_items.csv")
returns = pd.read_csv(CLEAN_DIR / "returns.csv")
campaigns = pd.read_csv(CLEAN_DIR / "campaigns.csv")
website_traffic = pd.read_csv(CLEAN_DIR / "website_traffic.csv")

# Create db tables based on said 
customers.to_sql('customers', conn, if_exists='append', index=False)
products.to_sql('products', conn, if_exists='append', index=False)
campaigns.to_sql('campaigns', conn, if_exists='append', index=False)
orders.to_sql('orders', conn, if_exists='append', index=False)
order_items.to_sql('order_items', conn, if_exists='append', index=False)
returns.to_sql('returns', conn, if_exists='append', index=False)
website_traffic.to_sql('website_traffic', conn, if_exists='append', index=False)

conn.commit()
conn.close()