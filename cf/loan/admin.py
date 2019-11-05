from django.contrib import admin
from .models import *


# Register your models here.
class ApplicationDataItem(admin.ModelAdmin):
    list_display = ['CfRequestId']


admin.site.register(ApplicationData)


class BusinessItem(admin.ModelAdmin):
    list_display = ['Name']


admin.site.register(Business)


class OwnerItem(admin.ModelAdmin):
    list_display = ['Name']


admin.site.register(Owner)
