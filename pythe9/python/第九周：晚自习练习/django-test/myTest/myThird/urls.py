from django.conf.urls import url

from  . import views

urlpatterns= [
    url('just/',views.just),

    url('one/(\d+)/(\w+)',views.one),

    url('two/(?P<a>\d+)/(?P<b>\d+)/(?P<name>\w+)/',views.two)
]