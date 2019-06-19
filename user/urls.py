from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

app_name = 'user'

urlpatterns = [
    #url('teste/', views.teste),
    url('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='sas/index.html'), name='logout'),
    url('novo_usuario/', views.novo_usuario, name='novo_usuario')
]
