
from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))
    raw_text = Column(String)
    quantity = Column(Integer, nullable=False)
