from django.urls import path

from . views import RegisterView,LoginView,LogOutView ,test_json

urlpatterns = [
    path(r'register/',RegisterView.as_view(),name='register'),
    path(r'login/',LoginView.as_view(),name='login'),
    # 注销
    path('logout/',LogOutView.as_view(),name='logout'),
    path('json_test/',test_json)
]