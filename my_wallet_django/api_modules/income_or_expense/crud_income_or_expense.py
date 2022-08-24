from datetime import datetime
import sys
from unicodedata import category
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.account.models import Account
from my_wallet_django.api_modules.category.models import Category
from my_wallet_django.api_modules.global_param.models import GlobalParam
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
                account={
                    "id": result.account.id,
                    "name": result.account.name,
                    "currency": result.account.currency.name,
                    "abbreviate":  result.account.currency.abbreviate},
                category={
                    "id": result.category.id,
                    "name": result.category.name,
                    "icon": result.category.icon},
                payment_method={
                    "id": result.payment_method.id,
                    "name": result.payment_method.name},
                transaction_type={
                    "id": result.transaction_type.id,
                    "name": result.transaction_type.name},
            )
            result_list.append(record)
        return Response(status="Ok", code="200", message="Fetch data successfully!", result=result_list)
    except:
        print("Error: ", sys.exc_info()[0])


def get_income_or_expense_detail(db: Session, id: int):
    try:
        status = db.query(Status).filter(Status.key_name == "Active").first()
        data = db.query(IncomeOrExpense).filter(
            IncomeOrExpense.status_id == status.id and IncomeOrExpense.id == id).first()

        result = IncomeOrExpense(
            id=data.id,
            amount=data.amount,
            transaction_date=data.transaction_date,
            memo=data.memo,
            account={
                "id": data.account.id,
                "name": data.account.name,
                "currency_id": data.account.currency.id,
                "currency": data.account.currency.name,
                "abbreviate":  data.account.currency.abbreviate},
            category={
                "id": data.category.id,
                "name": data.category.name},
            payment_method={
                "id": data.payment_method.id,
                "name": data.payment_method.name},
            transaction_type={
                "id": data.transaction_type.id,
                "name": data.transaction_type.name},
        )

        return Response(status="Ok", code="200", message="Fetch data successfully!", result=result)
    except:
        print("Error: ", sys.exc_info()[0])


def get_income_or_expense_by_id(db: Session, id: int):
    return db.query(IncomeOrExpense).filter(IncomeOrExpense.id == id).first()


def create_income_or_expense(user_id: int, db: Session, income_or_expense: IncomeOrExpenseCreate):
    try:
        status = db.query(Status).filter(Status.key_name == "Active").first()
        account = db.query(Account).filter(
            Account.id == income_or_expense.account_id).first()
        category = db.query(Category).filter(
            Category.id == income_or_expense.category_id).first()
        payment_method = db.query(PaymentMethod).filter(
            PaymentMethod.id == income_or_expense.payment_method_id).first()
        user = db.query(AuthUser).filter(
            AuthUser.id == user_id).first()
        transaction_type = db.query(GlobalParam).filter(
            GlobalParam.id == income_or_expense.transaction_type_id).first()

        new_income_or_expense = IncomeOrExpense(
            transaction_type=transaction_type,
            amount=income_or_expense.amount,
            transaction_date=income_or_expense.transaction_date,
            memo=income_or_expense.memo,
            account=account,
            category=category,
            payment_method=payment_method,
            user=user,
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

        current_income_or_expense = get_income_or_expense_by_id(
            db=db, id=income_or_expense.id)
        current_income_or_expense.global_param_id = income_or_expense.transaction_type_id
        current_income_or_expense.amount = income_or_expense.amount,
        current_income_or_expense.transaction_date = income_or_expense.transaction_date,
        current_income_or_expense.memo = income_or_expense.memo,
        current_income_or_expense.account_id = income_or_expense.account_id,
        current_income_or_expense.category_id = income_or_expense.category_id,
        current_income_or_expense.payment_method_id = income_or_expense.payment_method_id,
        current_income_or_expense.user_account_id = 1,
        current_income_or_expense.modified_date = datetime.now(),
        current_income_or_expense.modified_by = 1,
        current_income_or_expense.version = current_income_or_expense.version + 1,

        db.commit()
        db.refresh(current_income_or_expense)
        return {"_id": current_income_or_expense.id}
    except:
        print("Error: ", sys.exc_info()[0])
