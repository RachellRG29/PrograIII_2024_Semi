from django.shortcuts import render

# Create your views here.
def index_inicio(request):
    return render(request, 'index_inicio.html')

def index_login(request):
    return render(request, 'index_login.html')

def index_register(request):
    return render(request, 'index_register.html')

def index_pant_prin(request):
    return render(request, 'index_pant_prin.html')
