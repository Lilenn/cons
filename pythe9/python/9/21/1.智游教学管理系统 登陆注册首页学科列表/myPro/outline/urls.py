from django.urls import path,re_path

from .views import OutlineView,DetailView,AddView,EditView,DeleteView

app_name='outline'
urlpatterns = [
    path('list/',OutlineView.as_view(),name='outline_list'),
    path('detail/',DetailView.as_view(),name='detail'),
    path('add/',AddView.as_view(),name='add'),
    path('edit/',EditView.as_view(),name='edit'),
    path('delete/',DeleteView.as_view(),name='delete')
]