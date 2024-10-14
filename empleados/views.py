from django.shortcuts import render

def mostrarEmpleados(request):
   empleados = ["Martín González",
    "Sofía Rodríguez",
    "Matías Pérez",
    "Camila Muñoz",
    "Joaquín Rojas",
    "Antonia Díaz",
    "Sebastián Contreras",
    "Isidora Silva",
    "Vicente Espinoza",
    "Francisca Fernández"]
   context = {'empleados': empleados}
   return render(request, 'empleados/mostrarEmpleados.html ', context)