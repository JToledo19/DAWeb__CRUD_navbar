from django.shortcuts import render, redirect
from .models import Pedido

# Create your views here.

def inicio_vistaPedido(request):
    lospedidos=Pedido.objects.all()
    return render(request,'gestionarPedido.html',{'mispedidos':lospedidos})

def registrarPedido(request):
    id_pedido=request.POST["numidpedido"]
    id_cliente=request.POST["numidcliente"]
    fecha_pedido=request.POST["txtfechapedido"]
    total_pedido=request.POST["txttotalpedido"]
    estado_pedido=request.POST["txtestadopedido"]
    metodo_pago=request.POST["txtmetodopago"]
    direccion_envio=request.POST["txtdireccionenvio"]

    guardarpedido=Pedido.objects.create(id_pedido=id_pedido,id_cliente=id_cliente,fecha_pedido=fecha_pedido,total_pedido=total_pedido,estado_pedido=estado_pedido,metodo_pago=metodo_pago,direccion_envio=direccion_envio)

    return redirect('Pedido')

def seleccionarPedido(request,id_pedido):
    Pedido_=Pedido.objects.get(id_pedido=id_pedido)
    return render(request,"editarPedido.html",{"misPedido":Pedido_})

def editarPedido(request):
    id_pedido=request.POST["idpedido"]
    id_cliente=request.POST["numidcliente"]
    fecha_pedido=request.POST["txtfechapedido"]
    total_pedido=request.POST["txttotalpedido"]
    estado_pedido=request.POST["numestadopedido"]
    metodo_pago=request.POST["txtmetodopago"]
    direccion_envio=request.POST["txtdireccionenvio"]

    Pedido_=Pedido.objects.get(id_pedido=id_pedido)

    Pedido_.id_cliente=id_cliente
    Pedido_.fecha_pedido=fecha_pedido
    Pedido_.total_pedido=total_pedido
    Pedido_.estado_pedido=estado_pedido
    Pedido_.metodo_pago=metodo_pago
    Pedido_.direccion_envio=direccion_envio
    Pedido_.save()

    return redirect('Pedido')

def borrarPedido(request,id_pedido):
    Pedido_=Pedido.objects.get(id_pedido=id_pedido)
    Pedido_.delete()

    return redirect('Pedido')