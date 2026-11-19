CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  language TEXT NOT NULL DEFAULT 'de'
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  sku TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  unit TEXT NOT NULL DEFAULT 'pcs',
  unit_price NUMERIC(10,2) NOT NULL
);

CREATE TABLE inbound_emails (
  id SERIAL PRIMARY KEY,
  message_id TEXT UNIQUE NOT NULL,
  sender TEXT NOT NULL,
  subject TEXT,
  body TEXT NOT NULL,
  received_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  email_id INT UNIQUE REFERENCES inbound_emails(id),
  customer_id INT REFERENCES customers(id),
  status TEXT NOT NULL
    CHECK (status IN ('draft','approved','rejected','needs_review')),
  delivery_date DATE,
  review_reason TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE order_items (
  id SERIAL PRIMARY KEY,
  order_id INT NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
  product_id INT REFERENCES products(id),
  raw_text TEXT,
  quantity INT NOT NULL CHECK (quantity > 0)
);