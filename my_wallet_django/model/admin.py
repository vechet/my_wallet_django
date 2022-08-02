from django.contrib import admin

# Register your models here.
from .models import Account, AccountType, Category, Configuration
from .models import PhotoAndVideo, Status, ConfigurationParam, Currency
from .models import Customer, Device, ErrorReport, FileDocument, GlobalParam
from .models import IncomeOrExpense, NotificationDeviceToken, PaymentMethod

admin.site.register([Account, AccountType, Category, Configuration])
admin.site.register([PhotoAndVideo, Status, ConfigurationParam, Currency])
admin.site.register([Customer, Device, ErrorReport, FileDocument, GlobalParam])
admin.site.register([IncomeOrExpense, NotificationDeviceToken, PaymentMethod])
