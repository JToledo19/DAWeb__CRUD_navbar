from django.shortcuts import render, redirect
from .models import Ventas

# Create your views here.

def inicio_vistaVentas(request):
    lasventas=Ventas.objects.all()
    return render(request,'gestionarVentas.html',{'misventas':lasventas})

def registrarVentas(request):
    id_empleado=request.POST["numidempleado"]
    id_producto=request.POST["numidproducto"]
    id_cliente=request.POST["numidcliente"]
    cantidad_producto=request.POST["numcantidadproducto"]
    fecha=request.POST["txtfecha"]
    precio_total=request.POST["numpreciototal"]
    metodo_pago=request.POST["txtmetodopago"]

    guardarventas=Ventas.objects.create(id_empleado=id_empleado,id_producto=id_producto,id_cliente=id_cliente,cantidad_producto=cantidad_producto,fecha=fecha,precio_total=precio_total,metodo_pago=metodo_pago)

    return redirect('Ventas')

def seleccionarVentas(request,id_empleado):
    ventas=Ventas.objects.get(id_empleado=id_empleado)
    return render(request,"editarVentas.html",{"misventas":ventas})

def editarVentas(request):
    id_empleado=request.POST["numidempleado"]
    id_producto=request.POST["numidproducto"]
    id_cliente=request.POST["numidcliente"]
    cantidad_producto=request.POST["numcantidadproducto"]
    fecha=request.POST["txtfecha"]
    precio_total=request.POST["numpreciototal"]
    metodo_pago=request.POST["txtmetodopago"]


    ventas=Ventas.objects.get(id_empleado=id_empleado)

    ventas.id_producto=id_producto
    ventas.id_cliente=id_cliente
    ventas.cantidad_producto=cantidad_producto
    ventas.fecha=fecha
    ventas.precio_total=precio_total
    ventas.metodo_pago=metodo_pago
    ventas.save()

    return redirect('Ventas')

def borrarVentas(request,id_empleado):
    ventas=Ventas.objects.get(id_empleado=id_empleado)
    ventas.delete()

    return redirect('Ventas')