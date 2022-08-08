from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.account.crud_account import get_account, create_account, update_account, delete_account
from my_wallet_django.api_modules.account.schemas import AccountCreate, AccountUpdate, AccountDelete
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


@router.get("/account")
async def get_account_service(skip: int = 0, limit: int = 100, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    _accounts = get_account(db, skip, limit)
    return _accounts


@router.post("/createAccount")
async def create_account_service(request: AccountCreate, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    create_account(db, account=request)
    return Response(status="Ok",
                    code="200",
                    message="Account created successfully!").dict(exclude_none=True)


@router.patch("/updateAccount")
async def update_account_service(request: AccountUpdate, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    _account = update_account(db, account=request)
    return Response(status="Ok", code="200", message="Account updated successfully!", result=_account)


@router.delete("/deleteAccount")
async def delete_account_service(request: AccountDelete, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    delete_account(db, id=request.id)
    return Response(status="Ok", code="200", message="Account deleted successfully!").dict(exclude_none=True)
