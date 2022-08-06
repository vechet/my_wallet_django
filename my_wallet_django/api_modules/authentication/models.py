from xmlrpc.client import Boolean
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from my_wallet_django.config import Base


class AuthUser(Base):
    __tablename__ = "auth_user"

    id = Column(Integer, primary_key=True)
    password = Column(String)
    last_login = Column(DateTime, nullable=True)
    is_superuser = Column(Boolean)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    is_staff = Column(Boolean)
    is_active = Column(Boolean)
    date_joined = Column(DateTime)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserToken(Base):
    __tablename__ = "model_authusertoken"

    id = Column(Integer, primary_key=True)
    token = Column(String)
    expires_in = Column(DateTime)
    user_account_id = Column(Integer)

    class Meta:
        managed = False
        db_table = 'model_authusertoken'
