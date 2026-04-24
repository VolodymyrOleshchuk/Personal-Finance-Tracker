from sqlalchemy import Column, Integer, String, ForeignKey

from app.core.database import Base


# Category model (income / expense categories)
class Category(Base):
    __tablename__ = "categories"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)

    # Category name (e.g. Salary, Food)
    name = Column(String, nullable=False, index=True)

    # Category type (income / expense)
    type = Column(String, nullable=False)

    # Owner (user who created this category)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)