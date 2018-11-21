from django.urls import path,re_path
from django.conf.urls import url
from .views import SubjectList,AddView,DetailView,Delete,EditView

app_name = 'subject'
urlpatterns = [
    path('',SubjectList.as_view(),name='home'),
    path('add/',AddView.as_view(),name='add'),
    path('detail/',DetailView.as_view(),name='detail'),
    path('delete/',Delete.as_view(),name='delete'),
    path('edit/',EditView.as_view(),name='edit')

]