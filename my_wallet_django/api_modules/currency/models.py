from xmlrpc.client import Boolean
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from my_wallet_django.config import Base


class Currency(Base):
    __tablename__ = "model_currency"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_base_currency = Column(Boolean)
    abbreviate = Column(String)
    memo = Column(String, nullable=True)
    is_system_value = Column(Boolean)
    created_date = Column(DateTime)
    modified_date = Column(DateTime, nullable=True)
    version = Column(Integer)
    created_by = Column(Integer)
    modified_by = Column(Integer, nullable=True)
    status_id = Column(Integer)

    class Meta:
        managed = False
        db_table = 'model_currency'
