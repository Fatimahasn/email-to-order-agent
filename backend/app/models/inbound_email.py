
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.db.database import Base


class InboundEmail(Base):
    __tablename__ = "inbound_emails"

    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(String, unique=True, nullable=False)
    sender = Column(String, nullable=False)
    subject = Column(String)
    body = Column(Text, nullable=False)
    received_at = Column(DateTime(timezone=True), server_default=func.now())
