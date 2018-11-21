from django.urls import path

from goods.views import index


app_name = "goods"
urlpatterns = [
    path("index/", index, name="index")
]