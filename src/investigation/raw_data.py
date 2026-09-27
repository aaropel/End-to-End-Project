import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
CLEAN_DIR = DATA_DIR / "clean"



customers = pd.read_csv(RAW_DIR / "customers.csv")
orders = pd.read_csv(RAW_DIR / "orders.csv")
products = pd.read_csv(RAW_DIR / "products.csv")
order_items = pd.read_csv(RAW_DIR / "order_items.csv")
returns = pd.read_csv(RAW_DIR / "returns.csv")
campaigns = pd.read_csv(RAW_DIR / "campaigns.csv")
website_traffic = pd.read_csv(RAW_DIR / "website_traffic.csv")


# Let's have a look at whats going on
def inspect_data(df):

    print("\nshape")
    print(df.shape)

    print("\ninfo")
    df.info()

    print("\nData Types")
    print(df.dtypes)

    print("\nMissing values")
    print(df.isna().sum())

    print("\nDuplicate values")
    print(df.duplicated().sum())
    # This gives all the different values per column
    for col in df.columns:
        print("\n", col)
        print(df[col].value_counts(dropna=False).head(20))

    if "order_id" in df.columns:
        duplicate_ids = df["order_id"].duplicated(keep=False)
        print(df[duplicate_ids].sort_values("order_id"))

    if "customer_id" in df.columns:
        duplicate_ids = df["customer_id"].duplicated(keep=False)
        print(df[duplicate_ids].sort_values("customer_id"))


inspect_data(orders)