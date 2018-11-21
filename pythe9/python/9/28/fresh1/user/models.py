from django.db import models
from django.contrib import admin
# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=50,null=False,verbose_name='用户名')
    password = models.CharField(max_length=256,null=False,verbose_name='密码')
    phone = models.CharField(max_length=11,null=False,verbose_name='电话号码')
    address = models.CharField(max_length=200,null=True,verbose_name='地址',blank=True)
    email = models.EmailField(verbose_name='电子邮箱',null=True)

    class Meta:
        # 修改admin后台显示的名字
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

@admin.register(UserModel)
class UserAdminModel(admin.ModelAdmin):
    list_display = ('username','phone','address')

class CollectGoodsModel(models.Model):
    # 属于谁的收货信息
    # 用户对于收货信息为一对多的关系
    user = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    # 收件人
    person_name = models.CharField(max_length=30,null=True,verbose_name='收货人')
    # 收件地址
    detail_address = models.CharField(max_length=200,null=False,verbose_name='详细地址')
    # 邮政编码
    postcode = models.IntegerField(default=000000,null=True,verbose_name='邮政编码')
    # 联系方式
    tel = models.CharField(max_length=20,verbose_name='联系方式',null=False)
    # 现在是否正在使用
    is_used = models.BooleanField(verbose_name='是否正在使用')

    class Meta:
        verbose_name = '收货信息管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.person_name

@admin.register(CollectGoodsModel)
class CollectGoodsAdminModel(admin.ModelAdmin):
    # 把收货信息注册到管理后台
    list_display = ('person_name','detail_address','tel','is_used')
