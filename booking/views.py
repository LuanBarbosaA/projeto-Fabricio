from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
import pdb
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
#from sas.decorators.decorators import required_to_be_admin


# Create your views here.
@login_required()
def novo_booking(request):
    user = request.user
    if request.method == "POST":
        #pdb.set_trace()
        #User.objects.get(id=user.id)
        '''form_booking = BookingForm(data={
            'responsible': request.POST.get('responsible'),
            'time': request.POST.get('time'),
            'place': request.POST.get('place'),
            'name': request.POST.get('name'),
            'start_date': request.POST.get('start_date'),
            'end_date': request.POST.get('end_date'),
            'engineering': request.POST.get('engineering'),
            'user': user,
        })'''
        form_booking = BookingForm(request.POST, request.user)
        #pdb.set_trace()
        if form_booking.is_valid():
            form_booking.save(request.user)
        return redirect('index/')
        #pdb.set_trace()
    else:
        contexto = {
            'form_booking': BookingForm()
        }
        return render(request, '../templates/booking/novo_booking.html', contexto)
