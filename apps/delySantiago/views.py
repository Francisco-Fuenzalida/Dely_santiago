from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'delySantiago/home.html')

def login(request):
    return render(request, 'delySantiago/login.html')

def registro(request):
    return render(request, 'delySantiago/registro.html')