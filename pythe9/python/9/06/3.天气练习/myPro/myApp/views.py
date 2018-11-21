from django.shortcuts import render
import requests

# Create your views here.
def myweather(request):
    url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E9%83%91%E5%B7%9E&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
    response = requests.get(url)
    response_dic = response.json()
    if response_dic['error'] == 0:
        weather_date = response_dic['results'][0]['weather_data']
        city = response_dic['results'][0]['currentCity']
        content = {
            'weather_date' : weather_date,
            'city' : city
        }

    return render(request,'index.html',content)