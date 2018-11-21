from django.db import models
from django.contrib import admin
from stage.models import StageModel
import datetime
# Create your models here.

class OutlineModel(models.Model):
    stages = StageModel.objects.all()
    stage_id_name = [(stage.id, stage.title) for stage in stages]

    stage_id = models.IntegerField(default=0, verbose_name='阶段id',choices=stage_id_name)
    number = models.IntegerField(default=0,verbose_name='序号',null=False)
    title = models.CharField(max_length=255,null=False,verbose_name='标题')
    days = models.IntegerField(default=0,null=False,verbose_name='学时')
    advancing = models.CharField(max_length=255,null=False,verbose_name='高级内容')
    remark = models.CharField(max_length=255,null=True,verbose_name='备注')
    status = models.IntegerField(default=0)
    creater = models.IntegerField(default=0,verbose_name='创建者')
    create_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间')
    updater = models.IntegerField(default=0,verbose_name='更新者')
    update_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='更新时间')

@admin.register(OutlineModel)
class OutlineAdminModel(admin.ModelAdmin):
    list_display = ('title','advancing')