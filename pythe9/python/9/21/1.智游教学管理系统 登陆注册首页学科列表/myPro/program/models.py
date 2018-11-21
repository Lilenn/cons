from django.db import models
from django.contrib import admin
import datetime
from outline.models import OutlineModel
from stage.models import StageModel
# Create your models here.
class ProgramModel(models.Model):
    stages = StageModel.objects.all()
    outlines = OutlineModel.objects.all()

    stage_id_name = [(stage.id, stage.title) for stage in stages]
    outline_id_name = [(outline.id,outline.title) for outline in outlines]

    stage_id = models.IntegerField(default=0, verbose_name='阶段id',choices=stage_id_name)
    outline_id = models.IntegerField(default=0,verbose_name='一级大纲id',choices=outline_id_name)
    number = models.IntegerField(default=0,null=False,verbose_name='排序')
    sign = models.CharField(max_length=255,null=False,verbose_name='标志性内容')
    digest = models.CharField(max_length=255,verbose_name='内容摘要',null=False)
    propare = models.CharField(max_length=255,verbose_name='准备工作',null=False)
    process = models.CharField(max_length=255,verbose_name='讲课流程',null=False)
    attention = models.CharField(max_length=255,verbose_name='准备工作',null=False)
    exercise = models.CharField(max_length=255,verbose_name='课后作业',null=False)
    share = models.CharField(max_length=255,verbose_name='学生分享',null=False)
    management = models.CharField(max_length=255,verbose_name='管理事项',null=False)
    remark = models.CharField(max_length=255,verbose_name='备注',null=True)
    status = models.IntegerField(default=0,null=True)
    creater = models.IntegerField(default=0,verbose_name='创建者',null=True)
    create_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间')
    updater = models.IntegerField(default=0,verbose_name='更新者')
    update_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='更新时间')

@admin.register(ProgramModel)
class ProgramAdminModel(admin.ModelAdmin):
    list_display = ('number','sign')




