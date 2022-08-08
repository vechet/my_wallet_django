from typing import Optional
from pydantic import BaseModel


class AccountCreate(BaseModel):
    name: str
    memo: Optional[str]


class AccountUpdate(BaseModel):
    id: int
    name: str
    memo: Optional[str]


class AccountDelete(BaseModel):
    id: int
