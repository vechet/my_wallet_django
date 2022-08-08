import sys
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.base_schemas import Response
from my_wallet_django.api_modules.device.models import Device


def get_device(db: Session, skip: int, limit: int):
    try:
        results = db.query(Device).offset(skip).limit(limit).all()
        return Response(status="Ok", code="200", message="Fetch data successfully!", result=results)
    except:
        print("Error: ", sys.exc_info()[0])
