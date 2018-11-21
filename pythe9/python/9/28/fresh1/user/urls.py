from django.urls import path

from .views import register,register_post,login,info,logout,all_order,upload
# 命名空间名字
app_name = 'user'
urlpatterns =  [
   path('register/',register, name='register'),
   path('register_post/',register_post,name='register_post'),
   path('login/',login,name='login'),
   path('info/',info,name='info'),
   path('logout/',logout,name='logout'),
   path('all_order/<int:page_num>',all_order,name='all_order'),
   path('upload/',upload,name='upload')
]