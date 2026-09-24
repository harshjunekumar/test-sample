-- =====================================================================
-- SQL Practice Database: "Northwind-lite" office & electronics retailer
-- Portable DDL: runs on SQLite, PostgreSQL and MySQL 8+.
-- Dates are stored as ISO strings ('YYYY-MM-DD'), timestamps as
-- 'YYYY-MM-DD HH:MM:SS'.
-- =====================================================================

DROP TABLE IF EXISTS web_events;
DROP TABLE IF EXISTS marketing_spend;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS regions;

CREATE TABLE regions (
    region_id    INTEGER PRIMARY KEY,
    region_name  VARCHAR(20) NOT NULL
);

CREATE TABLE customers (
    customer_id          INTEGER PRIMARY KEY,
    first_name           VARCHAR(50) NOT NULL,
    last_name            VARCHAR(50) NOT NULL,
    email                VARCHAR(100),          -- may be NULL / messy (data-quality exercises)
    city                 VARCHAR(50),           -- may be NULL / messy
    region_id            INTEGER REFERENCES regions(region_id),
    segment              VARCHAR(20) NOT NULL,  -- Consumer | SMB | Enterprise
    acquisition_channel  VARCHAR(20) NOT NULL,  -- Paid Search | Social | Email | Affiliate | Organic | Referral
    signup_date          DATE NOT NULL
);

CREATE TABLE products (
    product_id    INTEGER PRIMARY KEY,
    product_name  VARCHAR(50) NOT NULL,
    category      VARCHAR(20) NOT NULL,
    unit_price    DECIMAL(10,2) NOT NULL,       -- current list price
    unit_cost     DECIMAL(10,2) NOT NULL,
    launch_date   DATE NOT NULL
);

CREATE TABLE employees (
    employee_id  INTEGER PRIMARY KEY,
    full_name    VARCHAR(50) NOT NULL,
    title        VARCHAR(50) NOT NULL,
    manager_id   INTEGER REFERENCES employees(employee_id),
    region_id    INTEGER REFERENCES regions(region_id),
    hire_date    DATE NOT NULL,
    salary       DECIMAL(10,2) NOT NULL
);

CREATE TABLE orders (
    order_id     INTEGER PRIMARY KEY,
    customer_id  INTEGER NOT NULL REFERENCES customers(customer_id),
    employee_id  INTEGER REFERENCES employees(employee_id),  -- NULL = self-serve online order
    order_date   DATE NOT NULL,
    ship_date    DATE,                                     -- NULL when cancelled (or missing!)
    status       VARCHAR(20) NOT NULL                      -- completed | cancelled | returned
);

CREATE TABLE order_items (
    order_item_id  INTEGER PRIMARY KEY,
    order_id       INTEGER NOT NULL REFERENCES orders(order_id),
    product_id     INTEGER NOT NULL REFERENCES products(product_id),
    quantity       INTEGER NOT NULL,
    unit_price     DECIMAL(10,2) NOT NULL,   -- price actually charged per unit
    discount       DECIMAL(4,2)  NOT NULL    -- fraction, e.g. 0.10 = 10% off
);

CREATE TABLE marketing_spend (
    month_start  DATE NOT NULL,              -- first day of month
    channel      VARCHAR(20) NOT NULL,
    spend        DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (month_start, channel)
);

CREATE TABLE web_events (
    event_id     INTEGER PRIMARY KEY,
    session_id   INTEGER NOT NULL,
    customer_id  INTEGER REFERENCES customers(customer_id),  -- NULL = anonymous visitor
    device       VARCHAR(10) NOT NULL,       -- desktop | mobile | tablet
    event_type   VARCHAR(20) NOT NULL,       -- visit | view_product | add_to_cart | checkout | purchase
    event_time   TIMESTAMP NOT NULL
);
