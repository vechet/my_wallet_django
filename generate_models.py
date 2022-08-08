# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Book(models.Model):
    title = models.CharField(max_length=-1, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ModelAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    back_account_number = models.CharField(max_length=500, blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=18, decimal_places=4)
    is_system_value = models.BooleanField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    account_type = models.ForeignKey('ModelAccounttype', models.DO_NOTHING)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by')
    currency = models.ForeignKey('ModelCurrency', models.DO_NOTHING)
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)
    status = models.ForeignKey('ModelStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'model_account'


class ModelAccounttype(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    memo = models.CharField(max_length=500, blank=True, null=True)
    is_system_value = models.BooleanField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by')
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)
    status = models.ForeignKey('ModelStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'model_accounttype'


class ModelAuthusertoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.TextField()
    expires_in = models.DateTimeField()
    user_account = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'model_authusertoken'


class ModelCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    memo = models.CharField(max_length=500, blank=True, null=True)
    is_system_value = models.BooleanField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by')
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    status = models.ForeignKey('ModelStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'model_category'


class ModelConfiguration(models.Model):
    id = models.BigAutoField(primary_key=True)
    key_name = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_configuration'


class ModelConfigurationparam(models.Model):
    id = models.BigAutoField(primary_key=True)
    configuration_key_type = models.CharField(max_length=300)
    value = models.CharField(max_length=300)
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'model_configurationparam'


class ModelCurrency(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    is_base_currency = models.BooleanField()
    abbreviate = models.CharField(max_length=100)
    memo = models.CharField(max_length=500, blank=True, null=True)
    is_system_value = models.BooleanField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by')
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)
    status = models.ForeignKey('ModelStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'model_currency'


class ModelCustomer(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    memo = models.CharField(max_length=500, blank=True, null=True)
    is_system_value = models.BooleanField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by')
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)
    status = models.ForeignKey('ModelStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'model_customer'


class ModelDevice(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'model_device'


class ModelErrorreport(models.Model):
    id = models.BigAutoField(primary_key=True)
    module_name = models.CharField(max_length=100)
    message = models.CharField(max_length=4000)
    created_date = models.DateTimeField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by')

    class Meta:
        managed = False
        db_table = 'model_errorreport'


class ModelFiledocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    transaction_no = models.CharField(max_length=50)
    key_name = models.CharField(max_length=50)
    file_name = models.CharField(max_length=200)
    file_extension = models.CharField(max_length=5)
    file_type = models.IntegerField()
    income_or_expense = models.ForeignKey('ModelIncomeorexpense', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'model_filedocument'


class ModelGlobalparam(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    key_name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    value1 = models.IntegerField(blank=True, null=True)
    value2 = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=500, blank=True, null=True)
    status = models.ForeignKey('ModelStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'model_globalparam'


class ModelIncomeorexpense(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.IntegerField()
    amount = models.DecimalField(max_digits=18, decimal_places=4)
    transaction_date = models.DateTimeField()
    memo = models.CharField(max_length=500, blank=True, null=True)
    is_system_value = models.BooleanField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    account = models.ForeignKey(ModelAccount, models.DO_NOTHING)
    category = models.ForeignKey(ModelCategory, models.DO_NOTHING)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by')
    customer = models.ForeignKey(ModelCustomer, models.DO_NOTHING)
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)
    payment_method = models.ForeignKey('ModelPaymentmethod', models.DO_NOTHING)
    status = models.ForeignKey('ModelStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'model_incomeorexpense'


class ModelNotificationdevicetoken(models.Model):
    id = models.BigAutoField(primary_key=True)
    device_token = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'model_notificationdevicetoken'


class ModelPaymentmethod(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    memo = models.CharField(max_length=500, blank=True, null=True)
    is_system_value = models.BooleanField()
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by')
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)
    status = models.ForeignKey('ModelStatus', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'model_paymentmethod'


class ModelPhotoandvideo(models.Model):
    id = models.BigAutoField(primary_key=True)
    sort_order = models.IntegerField()
    file_name = models.CharField(max_length=200)
    user_account_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_photoandvideo'


class ModelStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    key_name = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    version = models.IntegerField()
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='created_by')
    modified_by = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='modified_by', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_status'
