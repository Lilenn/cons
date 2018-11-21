from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def just(request):
    name = request.GET.get('name','zhangsan')
    myID = request.GET.get('id','0')

    return HttpResponse('name=%s,id=%s' % (name,myID))
def one(request,mid ,name):
    return HttpResponse('id=%s, name=%s' % (mid,name))

def two(request,a ,b ,name):

    return HttpResponse('sum=%s,name=%s'%(a+b , name))