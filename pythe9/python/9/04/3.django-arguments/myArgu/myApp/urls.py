from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # 注意url 和 path 的区别
# http://127.0.0.1:8000/index/justtest/?id=100&name=lisi
    url('justtest/',views.justTest),
# http://127.0.0.1:8000/index/second/100/hello
#     path(r'second/<mid><name>',views.second)
    url(r'second/(\d+)/(\w+)',views.second),
    # ?P<a>
# http://127.0.0.1:8000/index/third/2/3/lisi
    url(r'third/(?P<a>\d+)/(?P<b>\d+)/(?P<name>\w+)',views.third)
]