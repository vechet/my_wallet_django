from sqlalchemy import Column, Integer, String
from config import Base


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)


class Device(Base):
    __tablename__ = "model_device"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    class Meta:
        managed = False
        db_table = 'model_device'
