from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# view类 为自定义视图类
# 该类可以响应 get post 方法
from django.views.generic import View
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
        return JsonResponse({'json':data_json})
    url = 'http://api.map.baidu.com/telematics/v3/weather?location=%E9%83%91%E5%B7%9E&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
    data_json = requests.get(url).json()
    return render(request,'weather.html',{'json':data_json})

def movie(request):
    if request.is_ajax():
        city = request.POST.get('city')
        url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(city)
        data_json = requests.get(url).json()
        return JsonResponse({'json':data_json})
    url = 'http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location=%E9%83%91%E5%B7%9E&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'
    data_json = requests.get(url).json()
    return render(request,'movie.html',{'json':data_json})

# class MovieView(View):
#     # 该方法可以相应 所有的get请求
#     def get(sele,request):
#         pass
class WeatherView(View):
    def get(self,request):
        city = request.GET.get('city')
        if city:
            url = 'http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'.format(city)
        else:
            url = 'http://api.map.baidu.com/telematics/v3/weather?location=郑州&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
        json_data = requests.get(url).json()
        print(url)
        print(json_data)
        if city :
            return JsonResponse({'json':json_data})
        return render(request,'weather.html',{'json':json_data})

class topView(View):
    def get(self,request):
        page = request.GET.get('page')

        if page:
            url = 'https://www.apiopen.top/satinGodApi?type=1&page={}'.format(page)
        else:
            page = 1
            url = 'https://www.apiopen.top/satinGodApi?type=1&page=1'

        top_list = requests.get(url).json()['data']
        list = []
        for x in range(1,21):
            list.append(x)
        paginator = Paginator(top_list,len(top_list))

        return render(request,'top.html',{'page':page,'paginator':paginator,'list':list})
    def post(self,request):
        return render(request, 'top.html')


