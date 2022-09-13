from django import forms  
from appDjango.models import Empleados, Experiencias, Estudios

#(Nombre, Apellido, Tipo de documento, numero de documento, correo, teléfono, tipo de sangre), 
class EmpleadoRegistro(forms.ModelForm):  
    class Meta:  
        model = Empleados
        fields = "__all__"  
#(Ano, Mes, Estudio, Institución, Titulo obtenido), 
class EmpleadoRegistro2(forms.ModelForm):  
    class Meta:  
        model = Estudios
        fields = "__all__" 
#(Ano, Mes, Empresa, Jefe inmediato, Cargo, Responsabilidades, Logros realizados)
class EmpleadoRegistro3(forms.ModelForm):  
    class Meta:  
        model = Experiencias
        fields = "__all__" 