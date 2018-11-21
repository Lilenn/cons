from django.urls import path,re_path

from .views import StageView,DetailView,DeleteView,AddView,EditView
urlpatterns = [
    path('list/',StageView.as_view(),name='stage_list'),
    path('detail/',DetailView.as_view(),name='detail'),
    path('delete/',DeleteView.as_view(),name='delete'),
    path('add/',AddView.as_view(),name='add'),
    path('edit/',EditView.as_view(),name='edit')
]