from django.urls import path
from .views import ProgramView,AddView,EditView,DetailView,DeleteView

app_name='program'
urlpatterns = [
    path('list/',ProgramView.as_view(),name='program_list'),
    path('add/',AddView.as_view(),name='add'),
    path('edit/',EditView.as_view(),name='edit'),
    path('detail/',DetailView.as_view(),name='detail'),
    path('delete/',DeleteView.as_view(),name='delete')
]