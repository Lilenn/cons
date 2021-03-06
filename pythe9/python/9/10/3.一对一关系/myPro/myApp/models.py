from django.db import models

# Create your models here.
# 一对一关系 ：每个人都对应一个身份证， 一个身份证也只能对应一个人
# 注意：如果模型里面的代码发生更改，那么一定要诚信迁移
class One(models.Model):
    # tsub = models.OneToOneField(Two, on_delete=models.CASCADE, primary_key=True)
    oname = models.CharField(max_length=20,null=True)
    oage = models.CharField(max_length=20,null=True)
    # data 日期 日期格式的字段
    odata = models.DateField(null=True)

    class Meta:
        db_table = 'First'

class Two(models.Model):
    # 设置一对一关系 是通过将表中的字段设置为主键完成的
    # on_dalete = models.CASCADE 当父表中的某一条数据删除的时候
    # 相关字表中的数据也会被删除
    # 需要将tsub设置为主键
    tsub = models.OneToOneField(One,on_delete=models.CASCADE,primary_key=True)
    tfond = models.CharField(max_length=20,null=True)
    tdes = models.CharField(max_length=200,null=True)

    class Meta:
        db_table = 'Second'
