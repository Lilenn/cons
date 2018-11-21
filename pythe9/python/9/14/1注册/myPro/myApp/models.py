from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 在django里面 有一些内置表，内置表会包含一些基本数据字段
# 其中有一个叫做auth——user类 里面包含了用户信息 ，比如账号密码等
# 因为这个类不能修改， 所以可以创建一个模型继承自这个类， 使用这个模型
# 进行用户的储存 autha-user 类中使用的 基础类为AbstractUser

class CustomUser(AbstractUser):
    # AbstractUser 里面有默认字段 可以全部使用默认字段 也可以添加额外的字段
    # 一下字段 是添加的字段 这些字段只做演示用 在其他代码用不到
    birthday =models.DateField(default='2015-07-30')
    nick = models.CharField(default='honey',max_length=20)
    class Meta:
        db_table = 'Honey'

# setting注册
# HINT: Add or change a related_name argument to the definition for 'CustomUser.user_permissions' or 'User.user_permissions'.
