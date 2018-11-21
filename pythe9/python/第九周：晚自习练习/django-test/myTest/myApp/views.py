from django.shortcuts import render
from django.http import HttpResponse
from .models import First
# Create your views here.
def home(request):

    addData = First.objects.all()

    objectList = list()
    for data in addData:
        objectList.append('姓名:' + data.name + '，描述：' + data.des)
    response_html = '<br>'.join(objectList)

    return HttpResponse(response_html)