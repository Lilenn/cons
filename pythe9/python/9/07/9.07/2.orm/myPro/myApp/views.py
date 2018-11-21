from django.shortcuts import render

from .models import Person
# Create your views here.
from django.http import HttpResponse
def index(requset):
    # 方法1
    # first  = Person(uname='张三',uage=17,usex=True)
    # first.save()

    # 方法2
    # first =  Person.objects.create(uname='lisi',uage=16,usex=False)

    # 方法3
    # first = Person()
    # first.uname= '小美'
    # first.uage = 21
    # first.usex = True
    # first.save()

    # 如果不存在则创建 如果存在 则获取
    # Person.objects.get_or_create(uname='王五',uage=22,usex=True)

    all  = Person.objects.all()

    # 找到的结果是一个容器  里面可能有多个值
    # 也可能没有值
    # 如果没有值 程序也不会报错
    # 查询
    first = Person.objects.filter(uname='小美')[0]
    # 修改值
    first.uname = '太美'
    # 删除
    Person.objects.filter(uname='lisi')[0].delete()

    return render(requset,'index.html',{'all':all,'find':first})


