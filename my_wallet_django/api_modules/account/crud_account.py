from datetime import datetime
import sys
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.account.models import Account
from my_wallet_django.api_modules.account.schemas import AccountCreate, AccountUpdate
from my_wallet_django.api_modules.status.models import Status
from my_wallet_django.api_modules.base_schemas import Response


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

        new_account = Account(
            name=account.name,
            memo=account.memo,
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
        print("Error: ", sys.exc_info()[0])


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
        current_account = get_account_by_id(
            db=db, id=account.id)
        current_account.name = account.name
        current_account.memo = account.memo
        current_account.modified_date = datetime.now(),
        current_account.modified_by = 1,
        current_account.version = current_account.version + 1,

        db.commit()
        db.refresh(current_account)
        return {"_id": current_account.id}
    except:
        print("Error: ", sys.exc_info()[0])
