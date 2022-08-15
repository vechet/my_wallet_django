from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.authentication.auth import AuthHandler
from my_wallet_django.api_modules.demo.crud_demo import create_demo_data
from my_wallet_django.config import SessionLocal

router = APIRouter()
auth_handler = AuthHandler()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/createDemoData")
async def create_demo_data_service(db: Session = Depends(get_db)):
    return create_demo_data(db)
