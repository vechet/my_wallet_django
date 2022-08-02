from sqlalchemy import Column, Integer, String, DateTime
from config import Base


class Configuration(Base):
    __tablename__ = "model_configuration"

    id = Column(Integer, primary_key=True)
    key_name = Column(String)
    value = Column(String, nullable=True)
    memo = Column(String, nullable=True)
    type = Column(String, nullable=True)
    name = Column(String, nullable=True)

    class Meta:
        managed = False
        db_table = 'model_configuration'
