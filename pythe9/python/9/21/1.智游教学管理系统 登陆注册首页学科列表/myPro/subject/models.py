from django.db import models
from django.contrib import admin
import datetime
# Create your models here.



class SubjectModel(models.Model):
    name = models.CharField(max_length=20,null=False)
    number = models.IntegerField(null=True)
    days = models.IntegerField(null=False)

    amount = models.CharField(null=False,max_length=100)
    assueance = models.CharField(max_length=100,null=False)
    remake = models.CharField(max_length=200,null=False)

    stauts = models.CharField(max_length=100,null=True)
    creater = models.CharField(max_length=100,null=True)
    create_time = models.DateTimeField(default=datetime.datetime.now())
    updater = models.CharField(max_length=100,null=True)
    update_time = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'subject'

@admin.register(SubjectModel)
class SubjectAdaminModel(admin.ModelAdmin):
    list_display = ('name','number')
