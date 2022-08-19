from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.income_or_expense.crud_income_or_expense import get_income_or_expense, create_income_or_expense, update_income_or_expense, delete_income_or_expense
from my_wallet_django.api_modules.income_or_expense.schemas import IncomeOrExpenseCreate, IncomeOrExpenseUpdate, IncomeOrExpenseDelete
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


@router.get("/incomeOrExpense")
async def get_income_or_expense_service(skip: int = 0, limit: int = 100, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    _income_or_expenses = get_income_or_expense(db, skip, limit)
    return _income_or_expenses


@router.post("/createIncomeOrExpense")
async def create_income_or_expense_service(request: IncomeOrExpenseCreate, user_id=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    create_income_or_expense(int(user_id), db, income_or_expense=request)
    return Response(status="Ok",
                    code="200",
                    message="Income or expense created successfully!").dict(exclude_none=True)


@router.patch("/updateIncomeOrExpense")
async def update_income_or_expense_service(request: IncomeOrExpenseUpdate, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    _income_or_expense = update_income_or_expense(
        db, income_or_expense=request)
    return Response(status="Ok", code="200", message="Income or expense updated successfully!", result=_income_or_expense)


@router.delete("/deleteIncomeOrExpense")
async def delete_income_or_expense_service(request: IncomeOrExpenseDelete, username=Depends(auth_handler.auth_wrapper), db: Session = Depends(get_db)):
    delete_income_or_expense(db, id=request.id)
    return Response(status="Ok", code="200", message="Income or expense deleted successfully!").dict(exclude_none=True)
