from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.authentication.auth import AuthHandler
from my_wallet_django.api_modules.device.crud_device import get_device
from my_wallet_django.api_modules.base_schemas import Response
from my_wallet_django.config import SessionLocal

router = APIRouter()
auth_handler = AuthHandler()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/device")
async def get_device_service(skip: int = 0, limit: int = 100, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    _devices = get_device(db, skip, limit)
    return _devices
