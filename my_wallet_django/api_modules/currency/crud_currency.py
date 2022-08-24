import sys
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.currency.models import Currency
from my_wallet_django.api_modules.status.models import Status
from my_wallet_django.api_modules.base_schemas import Response


def get_currency(db: Session, skip: int, limit: int):
    try:
        status = db.query(Status).filter(Status.key_name == "Active").first()
        results = db.query(Currency).where(
            Currency.status_id == status.id).order_by(Currency.id).offset(skip).limit(limit).all()

        result_list = []
        for result in results:
            record = Currency(
                id=result.id,
                name=result.name,
            )
            result_list.append(record)
        return Response(status="Ok", code="200", message="Fetch data successfully!", size=len(result_list), result=result_list)
    except:
        print("Error: ", sys.exc_info()[0])
