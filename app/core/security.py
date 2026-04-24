from datetime import datetime, timedelta, timezone

from jose import jwt
from passlib.context import CryptContext

from app.core.config import settings

# Password hashing config (bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Hash plain password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# Verify plain password against hashed one
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# Create JWT access token
def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    # Set token expiration time
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    # Add expiration to payload
    to_encode.update({"exp": expire})

    # Encode JWT token
    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )