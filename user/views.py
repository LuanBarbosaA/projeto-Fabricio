from django.shortcuts import render, redirect
from .forms import RegistrationForm


# Create your views here.


def teste(request):
    return render(request, '../templates/user/teste.html')


def login(request):
    return render(request, '../templates/user/login.html')


def novo_usuario(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = RegistrationForm()
        contexto = {
            "form": form
        }
    return render(request, '../templates/user/criar_novo_usuario.html', contexto)
