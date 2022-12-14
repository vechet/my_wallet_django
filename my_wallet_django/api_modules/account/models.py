from xmlrpc.client import Boolean
from sqlalchemy import Column, DateTime, Integer, String, Boolean, DECIMAL
from my_wallet_django.config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Account(Base):
    __tablename__ = "model_account"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    back_account_number = Column(String, nullable=True)
    opening_balance = Column(DECIMAL)
    account_type_id = Column(Integer, ForeignKey('model_accounttype.id'))
    account_type = relationship("AccountType")
    currency_id = Column(Integer, ForeignKey('model_currency.id'))
    currency = relationship("Currency")
    is_system_value = Column(Boolean)
    created_date = Column(DateTime)
    modified_date = Column(DateTime, nullable=True)
    version = Column(Integer)
    created_by = Column(Integer)
    modified_by = Column(Integer, nullable=True)
    status_id = Column(Integer)

    class Meta:
        managed = False
        db_table = 'model_account'
