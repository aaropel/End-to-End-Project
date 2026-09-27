CREATE TABLE customers (
    customer_id TEXT PRIMARY KEY,
    signup_date TEXT NOT NULL,
    country TEXT,
    country_code TEXT,
    region TEXT,
    city TEXT,
    age INTEGER, 
    customer_segment TEXT,
    acquisition_channel TEXT,
    email_opt_in INTEGER
);

CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    brand TEXT,
    unit_cost REAL,
    list_price REAL,
    launch_date TEXT,
    active INTEGER
);

CREATE TABLE campaigns (
    campaign_id TEXT PRIMARY KEY,
    month TEXT,
    channel TEXT,
    country_code TEXT,
    campaign_name TEXT,
    spend REAL,
    impressions INTEGER,
    clicks INTEGER
);

CREATE TABLE orders (
    order_id TEXT PRIMARY KEY,
    customer_id TEXT NOT NULL,
    order_date TEXT NOT NULL,
    status TEXT,
    sales_channel TEXT,
    marketing_channel TEXT,
    campaign_id TEXT,
    device TEXT,
    payment_method TEXT,
    discount_rate REAL,
    shipping_fee REAL,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (campaign_id)
        REFERENCES campaigns(campaign_id)
);

CREATE TABLE order_items (
    order_item_id TEXT PRIMARY KEY,
    order_id TEXT NOT NULL,
    product_id TEXT NOT NULL,
    quantity INTEGER,
    unit_price REAL,
    discount_amount REAL,
    net_revenue REAL,
    cost_of_goods REAL,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

CREATE TABLE returns (
    return_id TEXT PRIMARY KEY,
    order_item_id TEXT NOT NULL UNIQUE,
    return_date TEXT,
    return_reason TEXT,
    refund_amount REAL,

    FOREIGN KEY (order_item_id)
        REFERENCES order_items(order_item_id)
);

CREATE TABLE website_traffic (
    date TEXT PRIMARY KEY,
    sessions INTEGER,
    unique_visitors INTEGER,
    add_to_cart INTEGER,
    conversion_rate REAL,
    bounce_rate REAL
);