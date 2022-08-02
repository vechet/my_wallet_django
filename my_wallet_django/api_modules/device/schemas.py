from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel


class DeviceSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    class Config:
        orm_mode = True


class RequestDevice(BaseModel):
    parameter: DeviceSchema = Field(...)
