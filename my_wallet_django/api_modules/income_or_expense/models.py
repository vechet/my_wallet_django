from xmlrpc.client import Boolean
from sqlalchemy import Column, DateTime, Integer, String, Boolean, DECIMAL
from my_wallet_django.config import Base


class IncomeOrExpense(Base):
    __tablename__ = "model_incomeorexpense"

    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    amount = Column(DECIMAL)
    transaction_date = Column(DateTime)
    memo = Column(String, nullable=True)
    account_id = Column(Integer)
    category_id = Column(Integer)
    payment_method_id = Column(Integer)
    user_account_id = Column(Integer)
    is_system_value = Column(Boolean)
    created_date = Column(DateTime)
    modified_date = Column(DateTime, nullable=True)
    version = Column(Integer)
    created_by = Column(Integer)
    modified_by = Column(Integer, nullable=True)
    status_id = Column(Integer)

    class Meta:
        managed = False
        db_table = 'model_incomeorexpense'
