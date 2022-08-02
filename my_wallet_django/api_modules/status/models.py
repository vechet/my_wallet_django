from sqlalchemy import Column, Integer, String, DateTime
from config import Base


class Status(Base):
    __tablename__ = "model_status"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    key_name = Column(String)
    created_date = Column(DateTime)
    modified_date = Column(DateTime, nullable=True)
    version = Column(Integer)
    created_by = Column(Integer)
    modified_by = Column(Integer, nullable=True)

    class Meta:
        managed = False
        db_table = 'model_status'
