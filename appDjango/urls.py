
from django.urls import path
from appDjango.views import inicio, administracion

urlpatterns = [
    path('', inicio),
    path('index.html', inicio),
    path('administracion', administracion),  
    path('tables.html', administracion),  
]
