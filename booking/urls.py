from django.conf.urls import url, include
from . import views

app_name = 'booking'

urlpatterns = [
    url('novo_booking/', views.novo_booking, name='novo_booking'),
    url('minhas_reservas/', views.minhas_reservas, name='minhas_reservas')
]
