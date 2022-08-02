from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api_modules.device.crud_device import get_device, create_device, update_device, delete_device
from api_modules.device.schemas import DeviceSchema, RequestDevice
from api_modules.base_schemas import Response
from config import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/device")
async def get_device_service(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _devices = get_device(db, skip, limit)
    return Response(status="Ok", code="200", message="Fetch all device successfully", result=_devices)


@router.post("/createDevice")
async def create_device_service(request: RequestDevice, db: Session = Depends(get_db)):
    create_device(db, device=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Device created successfully").dict(exclude_none=True)


@router.patch("/updateDevice")
async def update_device_service(request: RequestDevice, db: Session = Depends(get_db)):
    _device = update_device(db, id=request.parameter.id,
                            name=request.parameter.name)
    return Response(status="Ok", code="200", message="Device updated successfully", result=_device)


@router.delete("/deleteDevice")
async def delete_device_service(request: RequestDevice,  db: Session = Depends(get_db)):
    delete_device(db, id=request.parameter.id)
    return Response(status="Ok", code="200", message="Device deleted successfully").dict(exclude_none=True)
