from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.
def add(request):
    return HttpResponse('网址2，第一个页面')
def addTo(request):
    return HttpResponse('网址2，第二个页面')