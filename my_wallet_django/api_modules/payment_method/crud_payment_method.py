import sys
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.payment_method.models import PaymentMethod
from my_wallet_django.api_modules.status.models import Status
from my_wallet_django.api_modules.base_schemas import Response


def get_payment_method(db: Session, skip: int, limit: int):
    try:
        status = db.query(Status).filter(Status.key_name == "Active").first()
        results = db.query(PaymentMethod).where(
            PaymentMethod.status_id == status.id).order_by(PaymentMethod.id).offset(skip).limit(limit).all()

        result_list = []
        for result in results:
            record = PaymentMethod(
                id=result.id,
                name=result.name,
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
