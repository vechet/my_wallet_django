from datetime import datetime
import sys
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.account.models import Account
from my_wallet_django.api_modules.account.schemas import AccountCreate, AccountUpdate
from my_wallet_django.api_modules.status.models import Status
from my_wallet_django.api_modules.base_schemas import Response
from my_wallet_django.api_modules.currency.models import Currency
from my_wallet_django.api_modules.account_type.models import AccountType


def get_account(db: Session, skip: int, limit: int):
    try:
        status = db.query(Status).filter(Status.key_name == "Active").first()
        results = db.query(Account).where(
            Account.status_id == status.id).order_by(Account.id).offset(skip).limit(limit).all()
        return Response(status="Ok", code="200", message="Fetch data successfully!", result=results)
    except:
        print("Error: ", sys.exc_info()[0])


def get_account_by_id(db: Session, id: int):
    return db.query(Account).filter(Account.id == id).first()


def create_account(db: Session, account: AccountCreate):
    try:
        status = db.query(Status).filter(Status.key_name == "Active").first()
        currency = db.query(Currency).filter(
            Currency.id == account.currency_id).first()
        account_type = db.query(AccountType).filter(
            AccountType.id == account.account_type_id).first()

        new_account = Account(
            name=account.name,
            back_account_number=account.back_account_number or '',
            opening_balance=account.opening_balance,
            account_type_id=account_type.id,
            currency_id=currency.id,
            is_system_value=False,
            created_date=datetime.now(),
            created_by=1,
            status_id=status.id,
            version=1,
        )

        db.add(new_account)
        db.commit()
        db.refresh(new_account)
        return {"_id": new_account.id}
    except:
        print("Error: ", sys.exc_info())


def delete_account(db: Session, id: int):
    try:
        status = db.query(Status).filter(Status.key_name == "Inactive").first()
        _account = get_account_by_id(db=db, id=id)
        _account.status_id = status.id
        db.commit()
    except:
        print("Error: ", sys.exc_info()[0])


def update_account(db: Session, account: AccountUpdate):
    try:
        currency = db.query(Currency).filter(
            Currency.id == account.currency_id).first()
        account_type = db.query(AccountType).filter(
            AccountType.id == account.account_type_id).first()

        current_account = get_account_by_id(
            db=db, id=account.id)
        current_account.name = account.name
        current_account.back_account_number = account.back_account_number,
        current_account.opening_balance = account.opening_balance,
        current_account.account_type_id = account_type.id,
        current_account.currency_id = currency.id,
        current_account.modified_date = datetime.now(),
        current_account.modified_by = 1,
        current_account.version = current_account.version + 1,

        db.commit()
        db.refresh(current_account)
        return {"_id": current_account.id}
    except:
        print("Error: ", sys.exc_info()[0])
