from django.db import models
import datetime
from django.contrib import admin
from subject.models import SubjectModel
# Create your models here.
class StageModel(models.Model):
    subjects = SubjectModel.objects.all()
    subject_id_name = [(subject.id,subject.name) for subject in subjects]

    subject_id = models.IntegerField(default=0,verbose_name='学科id',choices=subject_id_name)
    title = models.CharField(max_length=50, null=False, verbose_name='阶段标题')
    number = models.IntegerField(default=0,verbose_name='排序')
    days = models.IntegerField(default=True,null=False,verbose_name='学时')
    project = models.CharField(max_length=255,verbose_name='项目',null=False)
    teaching = models.CharField(max_length=255,verbose_name='教学方法',null=False)
    learning = models.CharField(max_length=255,verbose_name='学习方法')
    sharing = models.CharField(max_length=255,verbose_name='学生分享')
    remark = models.CharField(max_length=255,verbose_name='备注')
    status = models.IntegerField(default=0,verbose_name='状态')
    creater = models.IntegerField(default=0,verbose_name='创建者')
    create_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='创建时间')
    updater = models.DateTimeField(default=datetime.datetime.now(),verbose_name='更新者')
    update_time = models.DateTimeField(default=datetime.datetime.now(),verbose_name='更新时间')

@admin.register(StageModel)
class StageAdminModel(admin.ModelAdmin):
    list_display = ('title','project')
