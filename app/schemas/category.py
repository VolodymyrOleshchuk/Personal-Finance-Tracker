from pydantic import BaseModel


# Data for creating/updating category
class CategoryCreate(BaseModel):
    name: str
    type: str  # "income" or "expense"


# Response model for category
class CategoryResponse(BaseModel):
    id: int
    name: str
    type: str

    # Allow reading from SQLAlchemy model
    model_config = {
        "from_attributes": True
    }