from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
# Create your models here.

class UserModel(AbstractUser):
    account = models.CharField(null=False, max_length=100)
    role = models.CharField(null=False,max_length=100)

@admin.register(UserModel)
class UserAdminModel(admin.ModelAdmin):
    list_display = ('account','role')
    # list_filter =