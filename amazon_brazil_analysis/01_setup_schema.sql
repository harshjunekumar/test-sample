-- =====================================================================
-- Amazon Brazil -> Amazon India : Database & schema setup
-- Run in pgAdmin. Step 1 (CREATE DATABASE) must run on its own while
-- connected to the default "postgres" database; then connect to
-- amazon_analysis and run the rest.
-- =====================================================================

-- CREATE DATABASE amazon_analysis;

CREATE SCHEMA IF NOT EXISTS amazon_brazil;

-- Customers: one row per customer_id (an order-level customer key);
-- customer_unique_id identifies the real person across orders.
CREATE TABLE amazon_brazil.customers (
    customer_id               VARCHAR(50) PRIMARY KEY,
    customer_unique_id        VARCHAR(50) NOT NULL,
    customer_zip_code_prefix  INT
);

-- Seller master data
CREATE TABLE amazon_brazil.seller (
    seller_id                 VARCHAR(50) PRIMARY KEY,
    seller_zip_code_prefix    INT
);

-- Product specifications
CREATE TABLE amazon_brazil.product (
    product_id                  VARCHAR(50) PRIMARY KEY,
    product_category_name       VARCHAR(100),
    product_name_lenght         INT,
    product_description_lenght  INT,
    product_photos_qty          INT,
    product_weight_g            INT,
    product_length_cm           INT,
    product_height_cm           INT,
    product_width_cm            INT
);

-- Orders: one row per order (1 customer_id -> 1 order)
CREATE TABLE amazon_brazil.orders (
    order_id                       VARCHAR(50) PRIMARY KEY,
    customer_id                    VARCHAR(50) REFERENCES amazon_brazil.customers(customer_id),
    order_status                   VARCHAR(20),
    order_purchase_timestamp       TIMESTAMP,
    order_approved_at              TIMESTAMP,
    order_delivered_carrier_date   TIMESTAMP,
    order_delivered_customer_date  TIMESTAMP,
    order_estimated_delivery_date  TIMESTAMP
);

-- Order items: one row per item line (1 order -> many items)
CREATE TABLE amazon_brazil.order_items (
    order_id             VARCHAR(50) REFERENCES amazon_brazil.orders(order_id),
    order_item_id        INT,
    product_id           VARCHAR(50) REFERENCES amazon_brazil.product(product_id),
    seller_id            VARCHAR(50) REFERENCES amazon_brazil.seller(seller_id),
    shipping_limit_date  TIMESTAMP,
    price                NUMERIC(10,2),
    freight_value        NUMERIC(10,2),
    PRIMARY KEY (order_id, order_item_id)
);

-- Payments: one row per payment instalment record (1 order -> many payments)
CREATE TABLE amazon_brazil.payments (
    order_id              VARCHAR(50) REFERENCES amazon_brazil.orders(order_id),
    payment_sequential    INT,
    payment_type          VARCHAR(20),
    payment_installments  INT,
    payment_value         NUMERIC(10,2),
    PRIMARY KEY (order_id, payment_sequential)
);

-- Import order (respect foreign keys): customers, seller, product,
-- orders, order_items, payments. In pgAdmin use Import/Export -> CSV,
-- delimiter ',', Header ON. psql equivalent:
-- \copy amazon_brazil.customers   FROM 'customers.csv'   CSV HEADER
-- \copy amazon_brazil.seller      FROM 'seller.csv'      CSV HEADER
-- \copy amazon_brazil.product     FROM 'product.csv'     CSV HEADER
-- \copy amazon_brazil.orders      FROM 'orders.csv'      CSV HEADER
-- \copy amazon_brazil.order_items FROM 'order_items.csv' CSV HEADER
-- \copy amazon_brazil.payments    FROM 'payments.csv'    CSV HEADER
