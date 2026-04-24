from pydantic import BaseModel


# Data for creating/updating transaction
class TransactionCreate(BaseModel):
    amount: float
    description: str | None = None
    category_id: int


# Response model for transaction
class TransactionResponse(BaseModel):
    id: int
    amount: float
    description: str | None = None
    category_id: int

    # Allow reading from SQLAlchemy model
    model_config = {
        "from_attributes": True
    }