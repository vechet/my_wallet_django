from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api_modules.account_type.crud_account_type import get_account_type, create_account_type, update_account_type, delete_account_type
from api_modules.account_type.schemas import AccountTypeCreate, AccountTypeUpdate, AccountTypeDelete
from api_modules.base_schemas import Response
from config import SessionLocal
from api_modules.authentication.auth import AuthHandler

router = APIRouter()
auth_handler = AuthHandler()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/accountType")
async def get_account_type_service(skip: int = 0, limit: int = 100, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    _account_types = get_account_type(db, skip, limit)
    return _account_types


@router.post("/createAccountType")
async def create_account_type_service(request: AccountTypeCreate, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    create_account_type(db, account_type=request)
    return Response(status="Ok",
                    code="200",
                    message="Account Type created successfully!").dict(exclude_none=True)


@router.patch("/updateAccountType")
async def update_account_type_service(request: AccountTypeUpdate, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    _account_type = update_account_type(db, account_type=request)
    return Response(status="Ok", code="200", message="Account Type updated successfully!", result=_account_type)


@router.delete("/deleteAccountType")
async def delete_account_type_service(request: AccountTypeDelete, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    delete_account_type(db, id=request.id)
    return Response(status="Ok", code="200", message="Account Type deleted successfully!").dict(exclude_none=True)
