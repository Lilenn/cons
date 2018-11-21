from django.db import models

# Create your models here.
class TouTiaoNews(models.Model):
    title = models.CharField(max_length=200 , null=True)
    link = models.CharField(max_length=600 , null=True)
    source = models.CharField(max_length=100,null=True)
    time = models.CharField(max_length=50 , null=True)