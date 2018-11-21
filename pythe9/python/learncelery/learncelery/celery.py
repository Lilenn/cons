import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE','learncelery.settings')
app = Celery('learncelery')

# CELERY 作为前缀，在settings中去配置
app.config_from_object('django.conf:settings',namespace='CELERY')

# 到django的各个app下，自动的发现taskss.py任务脚本
app.autodiscover_tasks()