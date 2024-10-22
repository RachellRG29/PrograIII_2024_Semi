from django.shortcuts import render

# Create your views here.
def index_inicio(request):
    return render(request, 'index_inicio.html')
