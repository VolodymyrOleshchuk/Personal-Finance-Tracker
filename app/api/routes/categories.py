from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.category import Category
from app.models.user import User
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("", response_model=CategoryResponse)
def create_category(
    category_data: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing_category = db.query(Category).filter(
        Category.name == category_data.name,
        Category.user_id == current_user.id
    ).first()

    if existing_category:
        raise HTTPException(status_code=400, detail="Category already exists")

    category = Category(
        name=category_data.name,
        type=category_data.type,
        user_id=current_user.id
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


@router.get("", response_model=List[CategoryResponse])
def get_categories(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Category).filter(
        Category.user_id == current_user.id
    ).all()


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    category_data: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    category = db.query(Category).filter(
        Category.id == category_id,
        Category.user_id == current_user.id
    ).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    existing_category = db.query(Category).filter(
        Category.name == category_data.name,
        Category.user_id == current_user.id,
        Category.id != category_id
    ).first()

    if existing_category:
        raise HTTPException(status_code=400, detail="Category already exists")

    category.name = category_data.name
    category.type = category_data.type

    db.commit()
    db.refresh(category)

    return category


@router.delete("/{category_id}")
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    category = db.query(Category).filter(
        Category.id == category_id,
        Category.user_id == current_user.id
    ).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category)
    db.commit()

    return {"message": "Category deleted"}