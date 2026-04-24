from pydantic import BaseModel, EmailStr


# Data for user registration
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


# Response model (without password!)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    # Allow reading from SQLAlchemy model
    model_config = {
        "from_attributes": True
    }