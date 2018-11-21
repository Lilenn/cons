from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.
class UserProfile(AbstractUser):
    unickname = models.CharField(max_length=20,verbose_name='昵称',null=True,blank=True)
    ubirthday = models.DateField(auto_now_add=True,verbose_name='生日',null=True,blank=True)
    uaddress = models.CharField(max_length=100,verbose_name='地址',null=True,blank=True)

class EmailRecode(models.Model):
    code = models.CharField(max_length=20)
    send_date = models.DateField(default=datetime.datetime.now())
    email = models.EmailField(error_messages={'invalid':'邮件格式不正确'})