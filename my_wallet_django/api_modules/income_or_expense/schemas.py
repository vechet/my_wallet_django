from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from decimal import Decimal


class IncomeOrExpenseCreate(BaseModel):
    transaction_type_id: int
    amount: Decimal
    transaction_date: datetime
    memo: Optional[str]
    account_id: int
    category_id: int
    payment_method_id: int


class IncomeOrExpenseUpdate(BaseModel):
    id: int
    transaction_type_id: int
    amount: Decimal
    transaction_date: datetime
    memo: Optional[str]
    account_id: int
    category_id: int
    payment_method_id: int


class IncomeOrExpenseDelete(BaseModel):
    id: int
