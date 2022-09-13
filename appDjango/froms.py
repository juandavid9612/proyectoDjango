from django import forms  
from appDjango.models import Empleados, Experiencias, Estudios

class EmpleadoRegistro(forms.ModelForm):  
    class Meta:  
        model = Empleados
        fields = "__all__"  