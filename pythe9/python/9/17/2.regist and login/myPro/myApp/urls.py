from django.urls import path
from django.conf.urls import url
from . import views
from .views import RegisterView,LoginView,ActiveView
urlpatterns = [
    path(r'register/',RegisterView.as_view(),name = 'register'),
    path(r'login/',LoginView.as_view(),name = 'login'),
    # ?P抓取内容
    url(r'active/(?P<code>\w+)',ActiveView.as_view(),name='active')
]
