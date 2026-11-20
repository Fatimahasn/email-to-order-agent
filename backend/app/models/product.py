
from sqlalchemy import Column, Integer, String, Numeric
from app.db.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False, default="pcs")
    unit_price = Column(Numeric(10, 2), nullable=False)
