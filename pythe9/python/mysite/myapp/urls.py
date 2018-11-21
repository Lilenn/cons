from django.urls import path
from .views import handle_wx,create_menu,get_menu_info,add_material

urlpatterns = [
    path('',handle_wx),
    path('create_menu/',create_menu),
    path("get_menu_info/", get_menu_info),
    path("add_material/", add_material)
]