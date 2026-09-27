import pandas as pd
from pathlib import Path

# Find the data
PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DIR = PROJECT_ROOT / "data" / "raw"
CLEAN_DIR = PROJECT_ROOT / "data" / "clean"


# Make the data useable based on observed issues
def clean_orders(df):
    df = df.copy()

    df.columns = df.columns.str.strip()
    df["order_date"] = pd.to_datetime(df["order_date"], format = 'mixed')
    df["marketing_channel"] = df["marketing_channel"].str.title()
    df["device"] = df["device"].fillna("Unknown")

    return df

def clean_customers(df):
    df = df.copy()

    df.columns = df.columns.str.strip()
    df["signup_date"] = pd.to_datetime(df["signup_date"], format = 'mixed')
    df["country"] = df["country"].str.strip().str.title()
    df = df.drop_duplicates()

    return df

def clean_products(df):
    df = df.copy()
    df.columns = df.columns.str.strip()

    df["launch_date"] = pd.to_datetime(df["launch_date"], format = 'mixed')
    df["category"] = df["category"].str.strip()
    df["brand"] = df["brand"].fillna("Unknown")

    return df

def clean_order_items(df):
    df = df.copy()
    df.columns = df.columns.str.strip()

    df["discount_amount"] = df["discount_amount"].fillna(0.00)
    return df

def clean_returns(df):
    df = df.copy()
    df.columns = df.columns.str.strip()

    df["return_date"] = pd.to_datetime(df["return_date"], format = 'mixed')
    return df

def clean_campaigns(df):
    df = df.copy()
    df.columns = df.columns.str.strip()

    df["month"] = pd.to_datetime(df["month"], format = 'mixed')
    return df

def clean_website_traffic(df):
    df = df.copy()
    df.columns = df.columns.str.strip()

    df["date"] = pd.to_datetime(df["date"], format = 'mixed')
    return df

# Set checks for the most critical values
def validate_orders(df):
    assert df["order_id"].is_unique, "Duplicate order IDs found"
    assert df["order_id"].notna().all(), "Missing order IDs found"
    assert df["customer_id"].notna().all(), "Missing customer IDs found"
    assert df["order_date"].notna().all(), "Missing order dates found"
    print("ORDERS VALIDATION OK")

def validate_customers(df):
    assert df["customer_id"].is_unique, "Duplicate customer IDs found"
    assert df["customer_id"].notna().all(), "Missing customer IDs found"
    assert df["email_opt_in"].notna().all(), "Missing email opt in found"
    assert df["signup_date"].notna().all(), "Missing sign up dates found"
    print("CUSTOMERS VALIDATION OK")

def validate_products(df):
    assert df["product_id"].is_unique, "Duplicate product IDs found"
    assert df["active"].notna().all(), "Missing active status found"   
    print("PRODUCTS VALIDATION OK")

def validate_order_items(df):
    assert df["order_item_id"].is_unique, "Duplicate order item IDs found"
    assert df["order_item_id"].notna().all(), "Missing order item IDs found"
    print("ORDER ITEMS VALIDATION OK")

def validate_returns(df):
    assert df["return_id"].is_unique, "Duplicate return IDs found"
    assert df["return_id"].notna().all(), "Missing return IDs found"
    assert df["order_item_id"].is_unique, "Duplicate order item IDs found"
    assert df["order_item_id"].notna().all(), "Missing order item IDs found"
    print("RETURNS VALIDATION OK")

def validate_campaigns(df):
    assert df["campaign_id"].is_unique, "Duplicate campaign IDs found"
    assert df["campaign_id"].notna().all(), "Missing campaign IDs found"
    print("CAMPAIGN VALIDATION OK")

def validate_website_traffic(df):
    assert df["date"].notna().all(), "Missing date found"
    print("WEBSITE TRAFFIC VALIDATION OK")

def main():
    # Load the data
    orders = pd.read_csv(RAW_DIR / "orders.csv")
    products = pd.read_csv(RAW_DIR / "products.csv")
    customers = pd.read_csv(RAW_DIR / "customers.csv")
    order_items = pd.read_csv(RAW_DIR / "order_items.csv")
    returns = pd.read_csv(RAW_DIR / "returns.csv")
    campaigns = pd.read_csv(RAW_DIR / "campaigns.csv")
    website_traffic = pd.read_csv(RAW_DIR / "website_traffic.csv")

    # Clean the data
    customers = clean_customers(customers)
    orders = clean_orders(orders)
    products = clean_products(products)
    order_items = clean_order_items(order_items)
    returns = clean_returns(returns)
    campaigns = clean_campaigns(campaigns)
    website_traffic = clean_website_traffic(website_traffic)

    # Make sure it's ok
    validate_customers(customers)
    validate_orders(orders)
    validate_products(products)
    validate_order_items(order_items)
    validate_returns(returns)
    validate_campaigns(campaigns)
    validate_website_traffic(website_traffic)

    # Check the validity of foreign keys
    assert orders["customer_id"].isin(customers["customer_id"]).all(), "Orders contains unkown customer IDs"
    assert order_items["order_id"].isin(orders["order_id"]).all(), "Order items contains unkown order IDs"
    assert order_items["product_id"].isin(products["product_id"]).all(), "Order items contains unkown product IDs"
    assert returns["order_item_id"].isin(order_items["order_item_id"]).all(), "Returns contains unknown order item IDs"


    # Make sure the folder exists before saving files into it
    CLEAN_DIR.mkdir(parents=True, exist_ok=True)

    # Save cleaned data to a new file
    customers.to_csv(CLEAN_DIR / "customers.csv", index=False)
    orders.to_csv(CLEAN_DIR / "orders.csv",index=False)
    products.to_csv(CLEAN_DIR / "products.csv", index=False)
    order_items.to_csv(CLEAN_DIR / "order_items.csv", index=False)
    returns.to_csv(CLEAN_DIR / "returns.csv", index=False)
    campaigns.to_csv(CLEAN_DIR / "campaigns.csv", index=False)
    website_traffic.to_csv(CLEAN_DIR / "website_traffic.csv", index=False)

if __name__ == "__main__":
    main()

