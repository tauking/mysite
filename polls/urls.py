from django.urls import path

from . import views

app_name = 'polls'
urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('info', views.info, name='info'),
    ]
