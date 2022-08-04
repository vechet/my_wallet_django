from xmlrpc.client import Boolean
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from my_wallet_django.config import Base


class AccountType(Base):
    __tablename__ = "model_accounttype"

    id = Column(Integer, primary_key=True)
    name = Column(String)
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
        db_table = 'model_accounttype'

# class ModelAccounttype(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     memo = models.CharField(max_length=500, blank=True, null=True)
#     is_system_value = models.BooleanField()
#     created_date = models.DateTimeField()
#     modified_date = models.DateTimeField(blank=True, null=True)
#     version = models.IntegerField()
#     created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by')
#     modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)
#     status = models.ForeignKey('ModelStatus', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'model_accounttype'
