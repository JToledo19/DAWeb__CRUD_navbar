from django.urls import path
from ventas_app import views

urlpatterns = [
    path('Ventas',views.inicio_vistaVentas,name="Ventas"),
    path("registrarVentas/",views.registrarVentas,name="registrarVentas"),
    path("seleccionarVentas/<id_empleado>",views.seleccionarVentas,name="seleccionarVentas"),
    path("editarVentas/",views.editarVentas,name="editarVentas"),
    path("borrarVentas/<id_empleado>",views.borrarVentas,name="borrarVentas")
]