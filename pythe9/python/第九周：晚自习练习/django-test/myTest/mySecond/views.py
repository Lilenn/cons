from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

def index(request):
    p = People('小明','20')

    newTime = datetime.datetime.now()

    content = {
        'name':'李明',
        'age':21,
        'friend':p,
        'teday':newTime,
        'fond_list':['吃饭','睡觉','玩游戏']
    }
    return render(request,'index.html',content)