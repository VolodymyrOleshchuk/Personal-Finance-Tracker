from pydantic import BaseModel, EmailStr


# Request body for login
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


# Response with JWT token
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"  # default auth type