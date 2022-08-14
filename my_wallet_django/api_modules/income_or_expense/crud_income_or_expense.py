from datetime import datetime
import sys
from unicodedata import category
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.account.models import Account
from my_wallet_django.api_modules.category.models import Category
from my_wallet_django.api_modules.payment_method.models import PaymentMethod
from my_wallet_django.api_modules.authentication.models import AuthUser
from my_wallet_django.api_modules.income_or_expense.models import IncomeOrExpense
from my_wallet_django.api_modules.income_or_expense.schemas import IncomeOrExpenseCreate, IncomeOrExpenseUpdate
from my_wallet_django.api_modules.status.models import Status
from my_wallet_django.api_modules.base_schemas import Response


def get_income_or_expense(db: Session, skip: int, limit: int):
    try:
        status = db.query(Status).filter(Status.key_name == "Active").first()
        results = db.query(IncomeOrExpense).where(
            IncomeOrExpense.status_id == status.id).order_by(IncomeOrExpense.id).offset(skip).limit(limit).all()

        result_list = []
        for result in results:
            record = IncomeOrExpense(
                id=result.id,
                amount=result.amount,
                transaction_date=result.transaction_date,
                memo=result.memo,
                is_system_value=result.is_system_value,
                created_date=result.created_date,
                created_by=result.created_by,
                status_id=result.status_id,
                version=result.version,
                account={
                    "id": result.account.id,
                    "name": result.account.name},
                category={
                    "id": result.category.id,
                    "name": result.category.name,
                    "icon": result.category.icon},
                payment_method={
                    "id": result.payment_method.id,
                    "name": result.payment_method.name},
                user={"id": result.user.id, "name": result.user.username},
                transaction_type={
                    "id": result.transaction_type.id,
                    "name": result.transaction_type.name},
            )
            result_list.append(record)
        # return Response(status="Ok", code="200", message="Fetch data successfully!", result=results)
        return Response(status="Ok", code="200", message="Fetch data successfully!", result=result_list)
    except:
        print("Error: ", sys.exc_info()[0])


def get_income_or_expense_by_id(db: Session, id: int):
    return db.query(IncomeOrExpense).filter(IncomeOrExpense.id == id).first()


def create_income_or_expense(db: Session, income_or_expense: IncomeOrExpenseCreate):
    try:
        status = db.query(Status).filter(Status.key_name == "Active").first()
        account = db.query(Account).filter(
            Account.id == income_or_expense.account_id).first()
        category = db.query(Category).filter(
            Category.id == income_or_expense.category_id).first()
        payment_method = db.query(PaymentMethod).filter(
            PaymentMethod.id == income_or_expense.payment_method_id).first()
        user = db.query(AuthUser).filter(
            AuthUser.id == income_or_expense.user_account_id).first()

        new_income_or_expense = IncomeOrExpense(
            type=income_or_expense.type,
            amount=income_or_expense.amount,
            transaction_date=income_or_expense.transaction_date,
            memo=income_or_expense.memo,
            account_id=account.id,
            category_id=category.id,
            payment_method_id=payment_method.id,
            user_account_id=user.id,
            is_system_value=False,
            created_date=datetime.now(),
            created_by=1,
            status_id=status.id,
            version=1,
        )
        db.add(new_income_or_expense)
        db.commit()
        db.refresh(new_income_or_expense)
        return {"_id": new_income_or_expense.id}
    except:
        print("Error: ", sys.exc_info()[0])


def delete_income_or_expense(db: Session, id: int):
    try:
        status = db.query(Status).filter(Status.key_name == "Inactive").first()
        _income_or_expense = get_income_or_expense_by_id(db=db, id=id)
        _income_or_expense.status_id = status.id
        db.commit()
    except:
        print("Error: ", sys.exc_info()[0])


def update_income_or_expense(db: Session, income_or_expense: IncomeOrExpenseUpdate):
    try:
        account = db.query(Account).filter(
            Account.id == income_or_expense.account_id).first()
        category = db.query(Category).filter(
            Category.id == income_or_expense.category_id).first()
        payment_method = db.query(PaymentMethod).filter(
            PaymentMethod.id == income_or_expense.payment_method_id).first()
        user = db.query(AuthUser).filter(
            AuthUser.id == income_or_expense.user_account_id).first()

        current_income_or_expense = get_income_or_expense_by_id(
            db=db, id=income_or_expense.id)
        current_income_or_expense.type = income_or_expense.type,
        current_income_or_expense.amount = income_or_expense.amount,
        current_income_or_expense.transaction_date = income_or_expense.transaction_date,
        current_income_or_expense.memo = income_or_expense.memo,
        current_income_or_expense.account_id = account.id,
        current_income_or_expense.category_id = category.id,
        current_income_or_expense.payment_method_id = payment_method.id,
        current_income_or_expense.user_account_id = user.id,
        current_income_or_expense.modified_date = datetime.now(),
        current_income_or_expense.modified_by = 1,
        current_income_or_expense.version = current_income_or_expense.version + 1,

        db.commit()
        db.refresh(current_income_or_expense)
        return {"_id": current_income_or_expense.id}
    except:
        print("Error: ", sys.exc_info()[0])
