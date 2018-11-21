from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):

    return HttpResponse('网页1，,一个页面')
def second(request):

    return HttpResponse('网页1，第二个页面')