
from django.urls import path
from appDjango.views import inicio, administracion

urlpatterns = [
    path('', inicio),
    path('index.html', inicio),
    path('tables.html', administracion),  
]
