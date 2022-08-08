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
        return Response(status="Ok", code="200", message="Fetch data successfully!", result=results)
    except:
        print("Error: ", sys.exc_info()[0])
