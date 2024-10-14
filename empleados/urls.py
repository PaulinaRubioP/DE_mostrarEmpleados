from django.urls import path
from . import views

urlpatterns = [
    path("mostrarEmpleados/", views.mostrarEmpleados, name="mostrarEmpleados"),

]