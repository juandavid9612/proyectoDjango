
from django.urls import path
from appDjango.views import inicio

urlpatterns = [
    path('', inicio),
    path('index.html', inicio),

]
