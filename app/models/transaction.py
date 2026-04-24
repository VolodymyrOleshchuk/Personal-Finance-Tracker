from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


# Transaction model (income or expense record)
class Transaction(Base):
    __tablename__ = "transactions"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Transaction amount
    amount = Column(Float, nullable=False)

    # Optional transaction description
    description = Column(String, nullable=True)

    # Owner of transaction
    user_id = Column(Integer, ForeignKey("users.id"))

    # Related category
    category_id = Column(Integer, ForeignKey("categories.id"))

    # ORM relationships
    user = relationship("User")
    category = relationship("Category")