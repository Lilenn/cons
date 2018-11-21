from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
class People(object):
    def __init__(self,name ,age):
        self.name = name
        self.age = age

def index(request):
    p = People('小明','99')
    # 获取当前时间
    newTime = datetime.datetime.now()
    content = {
        'name':'张三',
        'fond_list':['吃饭','睡觉','玩手机','看视频','扯淡'],
        'study_list':['C','HTML','JS','Python','Node','UI'],
        'friend': p ,
        'today': newTime,
        'girl_friend':{
            'name':'小美',
            'height':'160',
            'hasKuang':True
        }
    }
    # render 渲染html文件的时候 会 从项目当中的templates里面找
    # 所以无需设置templates路径 如果app的templates里面有和项目的templates里的文件重名的时候
    # 只需在app里面仙剑一个文件夹 然后将重名文件放进去
    # 渲染文件的时候跟上新建的文件夹路径即可
    # return render(request,'index.html',content)
    return render(request,'templ/index.html')