from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def one(request):
    return HttpResponse('网页3，第一个页面')
def two(request):
    return HttpResponse('网页3，第二个页面')
