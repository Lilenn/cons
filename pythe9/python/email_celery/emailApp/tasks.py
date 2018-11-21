from __future__ import absolute_import

from celery import shared_task
from django.core.mail import send_mail
import logging

loger = logging.getLogger(__name__)



@shared_task
def celery_send_email(subject,message,from_email,recipient_list, **kwargs):
    try:
        loger.info('开始发送邮件')
        send_mail(subject,message,from_email,recipient_list,**kwargs)
        loger.info('发送邮件成功')
        return 'email send success!'
    except Exception as e:
        loger.info('email send error',e)
