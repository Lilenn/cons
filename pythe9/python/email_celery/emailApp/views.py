from django.shortcuts import render
from django.http import HttpResponse

from emailApp.tasks import celery_send_email
# Create your views here.

def add_task_send_email(request):
    celery_send_email.delay('邮件的主题','这是一个测试邮件','hk846077763@163.com',['846077763@qq.com'])
    return HttpResponse('send email success')