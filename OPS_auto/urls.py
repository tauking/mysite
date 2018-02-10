from django.urls import path

from . import views

app_name = 'OPS_auto'
urlpatterns=[
    path('', views.index, name='index'),
    ]