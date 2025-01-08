from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.models import Category
from src.schemas.category_schemas import CategoryCreate, Category as CategorySchema
from typing import List

router = APIRouter(prefix='/categories', tags=['categories'])

@router.post("/", response_model=CategorySchema)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = db.query(Category).filter(Category.label == category.label).first()
    if db_category:
        raise HTTPException(status_code=400, detail="Name already registered")

    db_category = Category(
        label=category.label,
        description=category.description,
        id=category.id
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category