from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.payment_method.crud_payment_method import get_payment_method
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


@router.get("/paymentMethod")
async def get_payment_method_service(skip: int = 0, limit: int = 100, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    _currencies = get_payment_method(db, skip, limit)
    return _currencies
