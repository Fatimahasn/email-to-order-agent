
from app.schemas.order_extraction import (
    ExtractedOrder,
    ExtractedOrderItem,
)

order = ExtractedOrder(
    customer_email="orders@alpinetools.example",
    customer_name="Alpine Tools Ltd",
    delivery_date="2026-11-27",
    items=[
        ExtractedOrderItem(
            raw_text="M8 x 40 hex screws",
            quantity=200,
        ),
        ExtractedOrderItem(
            raw_text="M8 nuts",
            quantity=500,
        ),
    ],
)

print(order.model_dump_json(indent=2))
