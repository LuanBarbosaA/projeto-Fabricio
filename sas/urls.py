from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url('teste/', views.teste)
    url('user/', include('user.urls', namespace='user')),
    url('', views.index, name='index')
]
