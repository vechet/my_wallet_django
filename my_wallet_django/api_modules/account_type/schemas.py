from typing import Optional
from pydantic import BaseModel


class AccountTypeCreate(BaseModel):
    name: str
    memo: Optional[str]


class AccountTypeUpdate(BaseModel):
    id: int
    name: str
    memo: Optional[str]


class AccountTypeDelete(BaseModel):
    id: int
