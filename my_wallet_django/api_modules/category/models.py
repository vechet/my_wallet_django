from xmlrpc.client import Boolean
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from my_wallet_django.config import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Category(Base):
    __tablename__ = "model_category"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    memo = Column(String, nullable=True)
    icon = Column(String, nullable=True)
    is_system_value = Column(Boolean)
    created_date = Column(DateTime)
    modified_date = Column(DateTime, nullable=True)
    version = Column(Integer)
    created_by = Column(Integer)
    modified_by = Column(Integer, nullable=True)
    status_id = Column(Integer)
    parent_id = Column(Integer, ForeignKey('model_category.id'))
    parent = relationship("Category")

    class Meta:
        managed = False
        db_table = 'model_category'
