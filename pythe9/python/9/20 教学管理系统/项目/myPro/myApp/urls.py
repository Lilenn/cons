from django.conf.urls import url
from django.urls import path
from . import views
from .views import AddView,ChangeView,DetailView

urlpatterns = [
    path(r'add/',AddView.as_view(),name='add'),
    url(r'detail/(?P<code>\d+)/',DetailView.as_view(),name='detail'),
    path(r'change/',ChangeView.as_view(),name='change')
]