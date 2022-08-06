from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.currency.crud_currency import get_currency
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


@router.get("/currency")
async def get_currency_service(skip: int = 0, limit: int = 100, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    _currencies = get_currency(db, skip, limit)
    return _currencies
