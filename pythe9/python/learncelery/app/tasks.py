from __future__ import absolute_import
from celery import shared_task
import time

@shared_task
def tasks_add(x,y):
    return x+y

@shared_task
def mul(x,y):
    return x*y
