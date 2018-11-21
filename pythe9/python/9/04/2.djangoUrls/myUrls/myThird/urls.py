from django.conf.urls import url
from . import views

urlpatterns = [
    url('one/',views.one),
    url('two/',views.two),
]
