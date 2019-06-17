from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'cliente'

urlpatterns = [
    #url('teste/', views.teste),
    url('login/', views.login, name='login'),
    url('novo_usuario/', views.novo_usuario, name='novo_usuario')
]
