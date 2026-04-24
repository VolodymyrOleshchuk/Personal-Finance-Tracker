from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.transaction import Transaction
from app.models.category import Category
from app.models.user import User

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    income = db.query(func.sum(Transaction.amount)).join(Category).filter(
        Transaction.user_id == current_user.id,
        Category.type == "income"
    ).scalar() or 0

    expense = db.query(func.sum(Transaction.amount)).join(Category).filter(
        Transaction.user_id == current_user.id,
        Category.type == "expense"
    ).scalar() or 0

    return {
        "income": income,
        "expense": expense,
        "balance": income - expense
    }