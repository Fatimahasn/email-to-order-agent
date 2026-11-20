
from app.db.database import SessionLocal
from app.models import Product, Customer

db = SessionLocal()

try:
    products = db.query(Product).all()

    print("\n--- Products ---")
    for product in products:
        print(
            f"SKU: {product.sku} | "
            f"Name: {product.name} | "
            f"Price: {product.unit_price}"
        )

    customers = db.query(Customer).all()

    print("\n--- Customers ---")
    for customer in customers:
        print(
            f"Name: {customer.name} | "
            f"Email: {customer.email}"
        )

finally:
    db.close()
