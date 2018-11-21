from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

class UserProfile(AbstractUser):
    unickname = models.CharField(max_length=20,verbose_name='昵称',null=True,blank=True)
    ubirthday = models.DateField(auto_now_add=True,verbose_name='生日',null=True,blank=True)
    uaddress = models.CharField(max_length=200,verbose_name='地址',null=True,blank=True)

class Subject(models.Model):
    id = models.CharField(primary_key=True,max_length=20)
    name = models.CharField(max_length=20,verbose_name='学科名称',null=False)
    amount = models.DecimalField(max_digits=10,decimal_places=0,verbose_name='学费',null=False)
    days = models.CharField(max_length=20,verbose_name='学时',null=False)
    assurance = models.CharField(max_length=255,verbose_name='承诺',null=False)
    remark = models.CharField(max_length=255,verbose_name='备注',null=True)

    stauts = models.CharField(max_length=100, null=True)
    creater = models.CharField(max_length=100, null=True)
    create_time = models.DateTimeField(default=datetime.datetime.now())
    updater = models.CharField(max_length=100, null=True)
    update_time = models.DateTimeField(default=datetime.datetime.now())
    number = models.IntegerField(null=True)

