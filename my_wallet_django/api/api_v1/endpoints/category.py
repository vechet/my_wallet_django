from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.category.crud_category import get_category, create_category, update_category, delete_category
from my_wallet_django.api_modules.category.schemas import CategoryCreate, CategoryUpdate, CategoryDelete
from my_wallet_django.api_modules.base_schemas import Response
from my_wallet_django.config import SessionLocal
from my_wallet_django.api_modules.authentication.auth import AuthHandler

router = APIRouter()
auth_handler = AuthHandler()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/category")
async def get_category_service(
    skip: int = 0,
    limit: int = 100,
    parent_id: int = 0,
    name: str = '',
    username=Depends(auth_handler.auth_wrapper),
    db: Session = Depends(get_db)
):
    _categories = get_category(db, skip, limit, parent_id, name)
    return _categories


@router.post("/createCategory")
async def create_category_service(request: CategoryCreate, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    create_category(db, category=request)
    return Response(status="Ok",
                    code="200",
                    message="Category created successfully!").dict(exclude_none=True)


@router.patch("/updateCategory")
async def update_category_service(request: CategoryUpdate, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    _category = update_category(db, category=request)
    return Response(status="Ok", code="200", message="Category updated successfully!", result=_category)


@router.delete("/deleteCategory")
async def delete_category_service(request: CategoryDelete, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    delete_category(db, id=request.id)
    return Response(status="Ok", code="200", message="Category deleted successfully!").dict(exclude_none=True)
