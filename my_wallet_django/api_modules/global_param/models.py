from xmlrpc.client import Boolean
from sqlalchemy import Column, DateTime, Integer, String, Boolean, DECIMAL
from my_wallet_django.config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class GlobalParam(Base):
    __tablename__ = "model_globalparam"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    key_name = Column(String)
    type = Column(String)
    value1 = Column(Integer, nullable=True)
    value2 = Column(String, nullable=True)
    memo = Column(String, nullable=True)
    status_id = Column(Integer)

    class Meta:
        managed = False
        db_table = 'model_globalparam'
