from apps.delySantiago.models import Plato
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def home(request):
    return render(request, 'delySantiago/home.html')

def login(request):
    return render(request, 'delySantiago/login.html')

def registro(request):
    return render(request, 'delySantiago/registro.html')

def tienda(request):
    platos = Plato.objects.all()
    data = {
        'platos': platos
    }
    return render(request, 'delySantiago/tienda.html', data)

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            # login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data['form'] = formulario    
    return render(request, 'registration/registro.html', data)