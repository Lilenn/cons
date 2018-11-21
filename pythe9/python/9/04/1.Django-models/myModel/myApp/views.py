from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
from .models import First
def home(request):
    # 获取所有的数据
    allData = First.objects.all()

    objectList = list()
    for data in allData:
        objectList.append('姓名:' + data.name + ',描述:'+ data.des)
    response_html = '<br>'.join(objectList)
    return HttpResponse(response_html)
