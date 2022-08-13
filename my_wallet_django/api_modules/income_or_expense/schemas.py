from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from decimal import Decimal


class IncomeOrExpenseCreate(BaseModel):
    type: int
    amount: Decimal
    transaction_date: datetime
    memo: Optional[str]
    account_id: int
    category_id: int
    payment_method_id: int
    user_account_id: int


class IncomeOrExpenseUpdate(BaseModel):
    id: int
    type: int
    amount: Decimal
    transaction_date: datetime
    memo: Optional[str]
    account_id: int
    category_id: int
    payment_method_id: int
    user_account_id: int


class IncomeOrExpenseDelete(BaseModel):
    id: int


class IncomeOrExpenseCustomModel(BaseModel):
    id: int
    type: int
    amount: Decimal
    transaction_date: datetime
    memo: Optional[str]
    account_id: int
    category_id: int
    payment_method_id: int
    user_account_id: int
    is_system_value = bool
    created_date = datetime
    modified_date = datetime
    version = int
    created_by = int
    modified_by = int
    status_id = int
