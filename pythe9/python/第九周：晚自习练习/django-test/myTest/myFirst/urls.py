from django.conf.urls import url
from . import views
urlpatterns = [
    url('first/',views.first),
    url('second/',views.second)
]