from datetime import datetime
import sys
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.account_type.models import AccountType
from my_wallet_django.api_modules.account_type.schemas import AccountTypeCreate, AccountTypeUpdate
from my_wallet_django.api_modules.status.models import Status
from my_wallet_django.api_modules.base_schemas import Response


def get_account_type(db: Session, skip: int, limit: int):
    try:
        status = db.query(Status).filter(Status.key_name == "Active").first()
        results = db.query(AccountType).where(
            AccountType.status_id == status.id).order_by(AccountType.id).offset(skip).limit(limit).all()

        result_list = []
        for result in results:
            record = AccountType(
                id=result.id,
                name=result.name
            )
            result_list.append(record)
        return Response(status="Ok", code="200", message="Fetch data successfully!",size=len(result_list), result=result_list)
    except:
        print("Error: ", sys.exc_info()[0])


def get_account_type_by_id(db: Session, id: int):
    return db.query(AccountType).filter(AccountType.id == id).first()


def create_account_type(db: Session, account_type: AccountTypeCreate):
    try:
        status = db.query(Status).filter(Status.key_name == "Active").first()

        new_account_type = AccountType(
            name=account_type.name,
            memo=account_type.memo,
            is_system_value=False,
            created_date=datetime.now(),
            created_by=1,
            status_id=status.id,
            version=1,
        )
        db.add(new_account_type)
        db.commit()
        db.refresh(new_account_type)
        return {"_id": new_account_type.id}
    except:
        print("Error: ", sys.exc_info()[0])


def delete_account_type(db: Session, id: int):
    try:
        status = db.query(Status).filter(Status.key_name == "Inactive").first()
        _account_type = get_account_type_by_id(db=db, id=id)
        _account_type.status_id = status.id
        db.commit()
    except:
        print("Error: ", sys.exc_info()[0])


def update_account_type(db: Session, account_type: AccountTypeUpdate):
    try:
        current_account_type = get_account_type_by_id(
            db=db, id=account_type.id)
        current_account_type.name = account_type.name
        current_account_type.memo = account_type.memo
        current_account_type.modified_date = datetime.now(),
        current_account_type.modified_by = 1,
        current_account_type.version = current_account_type.version + 1,

        db.commit()
        db.refresh(current_account_type)
        return {"_id": current_account_type.id}
    except:
        print("Error: ", sys.exc_info()[0])
