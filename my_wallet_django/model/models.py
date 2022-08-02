from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Status(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    key_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='created_by')
    created_date = models.DateTimeField()
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='modified_by', related_name='model_status_modified_by_fk_auth_user_id', null=True, blank=True)
    modified_date = models.DateTimeField(null=True, blank=True)
    version = models.IntegerField()


class AccountType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    memo = models.CharField(max_length=500, null=True, blank=True)
    is_system_value = models.BooleanField()
    status_id = models.ForeignKey(
        Status, models.DO_NOTHING, db_column='status_id')
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='created_by')
    created_date = models.DateTimeField()
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='modified_by', related_name='model_account_type_modified_by_fk_auth_user_id', null=True, blank=True)
    modified_date = models.DateTimeField(null=True, blank=True)
    version = models.IntegerField()


class Currency(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    is_base_currency = models.BooleanField()
    abbreviate = models.CharField(max_length=100)
    memo = models.CharField(max_length=500, null=True, blank=True)
    is_system_value = models.BooleanField()
    status_id = models.ForeignKey(
        Status, models.DO_NOTHING, db_column='status_id')
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='created_by')
    created_date = models.DateTimeField()
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='modified_by', related_name='model_currency_modified_by_fk_auth_user_id', null=True, blank=True)
    modified_date = models.DateTimeField(null=True, blank=True)
    version = models.IntegerField()


class Account(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    back_account_number = models.CharField(max_length=500)
    account_type_id = models.ForeignKey(
        AccountType, models.DO_NOTHING, db_column='account_type_id')
    opening_balance = models.DecimalField(max_digits=18, decimal_places=4)
    currency_id = models.ForeignKey(
        Currency, models.DO_NOTHING, db_column='currency_id')
    is_system_value = models.BooleanField()
    status_id = models.ForeignKey(
        Status, models.DO_NOTHING, db_column='status_id')
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='created_by')
    created_date = models.DateTimeField()
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='modified_by', related_name='model_account_modified_by_fk_auth_user_id', null=True, blank=True)
    modified_date = models.DateTimeField(null=True, blank=True)
    version = models.IntegerField()


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    parent_id = models.ForeignKey(
        "self", models.DO_NOTHING, db_column='parent_id', null=True, blank=True)
    memo = models.CharField(max_length=500, null=True, blank=True)
    is_system_value = models.BooleanField()
    status_id = models.ForeignKey(
        Status, models.DO_NOTHING, db_column='status_id')
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='created_by')
    created_date = models.DateTimeField()
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='modified_by', related_name='model_category_modified_by_fk_auth_user_id', null=True, blank=True)
    modified_date = models.DateTimeField(null=True, blank=True)
    version = models.IntegerField()


class Configuration(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_name = models.CharField(max_length=100)
    value = models.CharField(max_length=100, null=True, blank=True)
    memo = models.CharField(max_length=500, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)


class ConfigurationParam(models.Model):
    id = models.BigAutoField(primary_key=True)
    configuration_key_type = models.CharField(max_length=300)
    value = models.CharField(max_length=300)
    name = models.CharField(max_length=300)


class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    memo = models.CharField(max_length=500, null=True, blank=True)
    is_system_value = models.BooleanField()
    status_id = models.ForeignKey(
        Status, models.DO_NOTHING, db_column='status_id')
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='created_by')
    created_date = models.DateTimeField()
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='modified_by', related_name='model_customer_modified_by_fk_auth_user_id', null=True, blank=True)
    modified_date = models.DateTimeField(null=True, blank=True)
    version = models.IntegerField()


class Device(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=300)


class ErrorReport(models.Model):
    id = models.BigAutoField(primary_key=True)
    module_name = models.CharField(max_length=100)
    message = models.CharField(max_length=4000)
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='created_by')
    created_date = models.DateTimeField()


class PaymentMethod(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    memo = models.CharField(max_length=500, null=True, blank=True)
    is_system_value = models.BooleanField()
    status_id = models.ForeignKey(
        Status, models.DO_NOTHING, db_column='status_id')
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='created_by')
    created_date = models.DateTimeField()
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='modified_by', related_name='model_payment_method_modified_by_fk_auth_user_id', null=True, blank=True)
    modified_date = models.DateTimeField(null=True, blank=True)
    version = models.IntegerField()


class IncomeOrExpense(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    category_id = models.ForeignKey(
        Category, models.DO_NOTHING, db_column='category_id')
    amount = models.DecimalField(max_digits=18, decimal_places=4)
    transaction_date = models.DateTimeField()
    memo = models.CharField(max_length=500, null=True, blank=True)
    customer_id = models.ForeignKey(
        Customer, models.DO_NOTHING, db_column='customer_id')
    account_id = models.ForeignKey(
        Account, models.DO_NOTHING, db_column='account_id')
    payment_method_id = models.ForeignKey(
        PaymentMethod, models.DO_NOTHING, db_column='payment_method_id')
    is_system_value = models.BooleanField()
    status_id = models.ForeignKey(
        Status, models.DO_NOTHING, db_column='status_id')
    created_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='created_by')
    created_date = models.DateTimeField()
    modified_by = models.ForeignKey(
        User, models.DO_NOTHING, db_column='modified_by', related_name='model_income_or_expense_modified_by_fk_auth_user_id', null=True, blank=True)
    modified_date = models.DateTimeField(null=True, blank=True)
    version = models.IntegerField()


class FileDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    transaction_no = models.CharField(max_length=50)
    key_name = models.CharField(max_length=50)
    file_name = models.CharField(max_length=200)
    file_extension = models.CharField(max_length=5)
    file_type = models.IntegerField()
    income_or_expense_id = models.ForeignKey(
        IncomeOrExpense, models.DO_NOTHING, db_column='income_or_expense_id')


class GlobalParam(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    key_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    value1 = models.IntegerField(null=True)
    value2 = models.CharField(max_length=100, null=True)
    memo = models.CharField(max_length=500, null=True, blank=True)
    status_id = models.ForeignKey(
        Status, models.DO_NOTHING, db_column='status_id')


class NotificationDeviceToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    device_token = models.CharField(max_length=500)


class PhotoAndVideo(models.Model):
    id = models.BigAutoField(primary_key=True)
    sort_order = models.IntegerField()
    file_name = models.CharField(max_length=200)
    user_account_id = models.IntegerField(null=True, blank=True)
    memo = models.CharField(max_length=500, null=True, blank=True)
