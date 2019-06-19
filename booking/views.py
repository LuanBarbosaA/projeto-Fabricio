from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
import pdb
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
#from sas.decorators.decorators import required_to_be_admin


# Create your views here.
@login_required()
def novo_booking(request):
    if request.method == "POST":
        form_booking = BookingForm(request.POST, request.user)
        if form_booking.is_valid():
            form_booking.save(request.user)
        return redirect('index/')
    else:
        contexto = {
            'form_booking': BookingForm()
        }
        return render(request, '../templates/booking/novo_booking.html', contexto)


@login_required()
def minhas_reservas(request):
    if request.method == "GET":
        user = request.user
        reservas_list = Booking.objects.filter(user=user).all()
        #pdb.set_trace()
        contexto = {
            'reservas_list': reservas_list
        }
        return render(request, '../templates/booking/minhas_reservas.html', contexto)
    '''elif request.method == "POST":
        pdb.set_trace()'''
