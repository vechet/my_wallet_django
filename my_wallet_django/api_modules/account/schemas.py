from decimal import Decimal
from typing import Optional
from pydantic import BaseModel


class AccountCreate(BaseModel):
    name: str
    back_account_number: Optional[str]
    opening_balance: Decimal
    account_type_id: int
    currency_id: int


class AccountUpdate(BaseModel):
    id: int
    name: str
    back_account_number: Optional[str]
    opening_balance: Decimal
    account_type_id: int
    currency_id: int


class AccountDelete(BaseModel):
    id: int
