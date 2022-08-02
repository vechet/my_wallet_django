from sqlalchemy.orm import Session
from api_modules.device.models import Device
from api_modules.device.schemas import DeviceSchema


def get_device(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Device).offset(skip).limit(limit).all()


def get_device_by_id(db: Session, id: int):
    return db.query(Device).filter(Device.id == id).first()


def create_device(db: Session, device: DeviceSchema):
    _device = Device(name=device.name)
    db.add(_device)
    db.commit()
    db.refresh(_device)
    return _device


def delete_device(db: Session, id: int):
    _device = get_device_by_id(db=db, id=id)
    db.delete(_device)
    db.commit()


def update_device(db: Session, id: int, name: str):
    _device = get_device_by_id(db=db, id=id)
    _device.name = name

    db.commit()
    db.refresh(_device)
    return _device
