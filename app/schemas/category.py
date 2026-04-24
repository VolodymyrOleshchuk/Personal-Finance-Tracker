from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    type: str


class CategoryResponse(BaseModel):
    id: int
    name: str
    type: str

    model_config = {
        "from_attributes": True
    }