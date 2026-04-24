from sqlalchemy import Column, Integer, String

from app.core.database import Base


# User model (application user)
class User(Base):
    __tablename__ = "users"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Unique username
    username = Column(String, unique=True, index=True, nullable=False)

    # Unique email
    email = Column(String, unique=True, index=True, nullable=False)

    # Hashed password (never store plain password!)
    hashed_password = Column(String, nullable=False)