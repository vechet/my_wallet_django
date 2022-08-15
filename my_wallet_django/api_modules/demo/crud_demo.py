import sys
from sqlalchemy.orm import Session
from my_wallet_django.api_modules.base_schemas import Response
from my_wallet_django.api_modules.device.models import Device


def create_demo_data(db: Session):
    try:
        return "hello"
    except:
        print("Error: ", sys.exc_info()[0])
