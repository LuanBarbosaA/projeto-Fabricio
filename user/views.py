from django.shortcuts import render, redirect
from .forms import RegistrationForm, RegistrationUserForm
from django.contrib.auth import login
import pdb

# Create your views here.


def teste(request):
    return render(request, '../templates/user/teste.html')


def novo_usuario(request):
    if request.method == 'POST':
        form_registration = RegistrationForm(request.POST)
        form_user_profile = RegistrationUserForm(request.POST)
        #pdb.set_trace()
        if form_registration.is_valid():
            form_registration.save()
        if form_user_profile.is_valid():
            form_user_profile.save()
        return redirect('/index')
    else:
        form_registration = RegistrationForm()
        form_user_profile = RegistrationUserForm()
        contexto = {
            "form_registration": form_registration,
            "form_user_profile": form_user_profile
        }
        return render(request, '../templates/user/criar_novo_usuario.html', contexto)
