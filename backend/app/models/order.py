
from sqlalchemy import Column, Integer, String, Date, Text, DateTime, ForeignKey, func
from app.db.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    email_id = Column(Integer, ForeignKey("inbound_emails.id"), unique=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    status = Column(String, nullable=False)
    delivery_date = Column(Date)
    review_reason = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
