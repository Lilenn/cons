from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
# Create your views here.
def index(request):
    url = 'https://api.map.baidu.com/location/ip?ak=KHkVjtmfrM6NuzqxEALj0p8i1cUQot6Z&qq-pf-to=pcqq.group'
    data_json = requests.get(url).json()
    return render(request,'index.html',{'json':data_json})
def weather(request):
    if request.is_ajax():
        city = (request.GET.get('city'))
        url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'.format(city)
        data_json = requests.get(url).json()
        print(data_json)
        return JsonResponse({'json':data_json})
    url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E9%83%91%E5%B7%9E&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
    data_json = requests.get(url).json()
    return render(request,'weather.html',{'json':data_json})