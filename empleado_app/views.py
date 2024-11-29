from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.

def inicio_vistaEmpleado(request):
    lasempleado=Empleado.objects.all()
    return render(request,'gestionarEmpleado.html',{'misempleado':lasempleado})

def registrarEmpleado(request):
    id_empleado=request.POST["numidempleado"]
    id_ventas=request.POST["numidventas"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["numtelefono"]
    sexo=request.POST["txtsexo"]
    correo=request.POST["txtcorreo"]
    turno=request.POST["txtturno"]

    guardarempleado=Empleado.objects.create(id_empleado=id_empleado,id_ventas=id_ventas,nombre=nombre,telefono=telefono,sexo=sexo,correo=correo,turno=turno)

    return redirect('Empleado')

def seleccionarEmpleado(request,id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    return render(request,"editarEmpleado.html",{"misempleado":empleado})

def editarEmpleado(request):
    id_empleado=request.POST["numidempleado"]
    id_ventas=request.POST["numidventas"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["numtelefono"]
    sexo=request.POST["txtsexo"]
    correo=request.POST["txtcorreo"]
    turno=request.POST["txtturno"]

    empleado=Empleado.objects.get(id_empleado=id_empleado)

    empleado.id_ventas=id_ventas
    empleado.nombre=nombre
    empleado.telefono=telefono
    empleado.sexo=sexo
    empleado.correo=correo
    empleado.turno=turno
    empleado.save()

    return redirect('Empleado')

def borrarEmpleado(request,id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()

    return redirect('Empleado')