from pydantic import BaseModel


class TransactionCreate(BaseModel):
    amount: float
    description: str | None = None
    category_id: int


class TransactionResponse(BaseModel):
    id: int
    amount: float
    description: str | None = None
    category_id: int

    model_config = {
        "from_attributes": True
    }