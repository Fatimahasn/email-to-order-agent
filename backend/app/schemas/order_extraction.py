
from datetime import date
from pydantic import BaseModel, Field

class ExtractedOrderItem(BaseModel):
    # raw_text:	Original product description
    raw_text: str = Field(
        description="The product description exactly as written in the email."
    )
    
    # quantity:	Requested quantity
    quantity: int | None = Field(
        default=None,
        gt=0,
        description="Requested quantity. None if missing or unclear."
    )


class ExtractedOrder(BaseModel):
    # customer_email: Identifies the customer
    customer_email: str | None = Field(
        default=None,
        description="Customer email address, if available."
    )

    # customer_name: Extracts the customer's name
    customer_name: str | None = None

    # delivery_date: 	Requested delivery date
    delivery_date: date | None = None

    # items:Products requested
    items: list[ExtractedOrderItem] = Field(default_factory=list)

    # should_flag_for_review: Indicates whether human review is needed
    should_flag_for_review: bool = False

    # review_reason: Explains why review is required
    review_reason: str | None = None
