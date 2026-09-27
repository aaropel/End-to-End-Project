import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = PROJECT_ROOT / "data" / "raw"
CLEAN_DIR = PROJECT_ROOT / "data" / "clean"

# Load the data
orders = pd.read_csv(RAW_DIR / "orders.csv")
products = pd.read_csv(RAW_DIR / "products.csv")
customers = pd.read_csv(RAW_DIR / "customers.csv")
order_items = pd.read_csv(RAW_DIR / "order_items.csv")
returns = pd.read_csv(RAW_DIR / "returns.csv")
campaigns = pd.read_csv(RAW_DIR / "campaigns.csv")
website_traffic = pd.read_csv(RAW_DIR / "website_traffic.csv")

# Orders validation
def validate_orders(df):
    assert df["order_id"].is_unique, "Duplicate order IDs found"
    assert df["order_id"].notna().all(), "Missing order IDs found"
    assert df["customer_id"].notna().all(), "Missing customer IDs found"
    assert df["order_date"].notna().all(), "Missing order dates found"

    assert df["customer_id"].isin(customers["customer_id"]).all(), "Orders contains unknown customer IDs"

    print("ORDERS VALIDATION OK")

# Customers validation
def validate_customers(df):
    assert df["customer_id"].is_unique, "Duplicate customer IDs found"
    assert df["customer_id"].notna().all(), "Missing customer IDs found"
    assert df["email_opt_in"].notna().all(), "Missing email opt in found"
    assert df["signup_date"].notna().all(), "Missing sign up dates found"
    print("CUSTOMERS VALIDATION OK")

# Products validation
def validate_products(df,):
    assert df["product_id"].is_unique, "Duplicate product IDs found"
    assert df["active"].notna().all(), "Missing active status found"   
    print("PRODUCTS VALIDATION OK")

# Order items validation
def validate_order_items(df):
    assert df["order_item_id"].is_unique, "Duplicate order item IDs found"
    assert df["order_item_id"].notna().all(), "Missing order item IDs found"

    assert df["order_id"].isin(orders["order_id"]).all(), "Order items contains unkown order IDs"
    assert df["product_id"].isin(order_items["product_id"]).all(), "Order items contains unkown product IDs"

    assert (df["quantity"] > 0).all(), "Invalid quantities found"

    print("ORDER ITEMS VALIDATION OK")

# Returns validation    
def validate_returns(df):
    assert df["return_id"].is_unique, "Duplicate return IDs found"
    assert df["return_id"].notna().all(), "Missing return IDs found"

    assert df["order_item_id"].is_unique, "Duplicate order item IDs found"
    assert df["order_item_id"].notna().all(), "Missing order item IDs found"
    assert df["order_item_id"].isin(order_items["order_item_id"]).all(), "Order items contains unkown order item IDs"

    print("RETURNS VALIDATION OK")

# Campaign validation
def validate_campaigns(df):
    assert df["campaign_id"].is_unique, "Duplicate campaign IDs found"
    assert df["campaign_id"].notna().all(), "Missing campaign IDs found"

    assert (df["impressions"] >= 0).all(), "Negative impressions found"
    assert (df["clicks"] >= 0).all(), "Negative clicks found"
    assert (df["spend"] >= 0).all(), "Negative spend found"

    print("CAMPAIGN VALIDATION OK")

# Website traffic validation
def validate_website_traffic(df):

    assert df["date"].notna().all(), "Missing date found"
    assert (df["sessions"] >= 0).all(), "Negative sessions found"

    print("WEBSITE TRAFFIC VALIDATION OK")