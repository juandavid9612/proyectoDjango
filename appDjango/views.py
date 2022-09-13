from django.shortcuts import render
from appDjango.models import Empleados
# Create your views here.
def inicio(request):
    
    contexto = {
        "Empleados":Empleados.objects.all()

        }
    return render(request, 'index.html')