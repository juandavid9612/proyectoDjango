from django.shortcuts import render, redirect  
from appDjango.models import Empleados

#from django.contrib.auth.forms import UserCreationForm  
#from django.contrib import messages  

from appDjango.froms import EmpleadoRegistro

# Create your views here.

def inicio(request):    
    contexto = {
        "Empleados":Empleados.objects.all()

        }
    return render(request, 'index.html',contexto)

def administracion(request):      
    if request.method == "POST":  
        form = EmpleadoRegistro(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                #return redirect('tables.html')  
            except:  
                pass  
    else:  
        form = EmpleadoRegistro()

    contexto = {
    "Empleados":Empleados.objects.all(),
    'form':form 
    }
    return render(request, 'tables.html',contexto)