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
                # is_base_currency=result.is_base_currency,
                # abbreviate=result.abbreviate,
                # memo=result.memo,
                # is_system_value=result.is_system_value,
                # created_date=result.created_date,
                # created_by=result.created_by,
                # modified_date=result.modified_date,
                # modified_by=result.modified_by,
                # status_id=result.status_id,
                # version=result.version,
            )
            result_list.append(record)
        return Response(status="Ok", code="200", message="Fetch data successfully!", result=result_list)
    except:
        print("Error: ", sys.exc_info()[0])
