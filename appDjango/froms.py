from django import forms  
from appDjango.models import Empleados

class EmpleadoRegistro(forms.ModelForm):  
    class Meta:  
        model = Empleados  
        fields = "__all__"  