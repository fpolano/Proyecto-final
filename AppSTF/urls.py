from django.urls import path
from AppSTF import views

urlpatterns = [
    # Páginas estáticas #
    path('', views.inicio, name="Inicio"), #página de inicio
    path('nosotros', views.sobre, name="Nosotros"),
    path('desarrollador', views.desarrollador, name="Desarrollador"),

    # CRUD Máquinas #
    path('maquinas', views.maquinasLista, name="Maquinas lista"),
    path('maquinas/detalle/<maquinaId>', views.maquinasDetalle, name="Maquinas detalle"),
    path('maquinas/alta', views.maquinasAlta, name="Maquinas alta"),
    path('maquinas/modificacion/<maquinaId>', views.maquinasModificacion, name="Maquinas modificacion"),
    path('maquinas/borrar/<maquinaId>', views.maquinasBaja, name="Maquinas borrar"),

    # CRUD Repuestos #
    path('repuestos', views.repuestosLista, name="Repuestos lista"),
    path('repuestos/detalle/<repuId>', views.repuestosDetalle, name="Repuestos detalle"),
    path('repuestos/alta', views.repuestosAlta, name="Repuestos alta"),
    path('repuestos/modificacion/<repuId>', views.repuestosModificacion, name="Repuestos modificacion"),
    path('repuestos/borrar/<repuId>', views.repuestosBaja, name="Repuestos borrar"),

    # CRUD manuales #
    path('manuales', views.manualesLista, name="Manuales lista"),
    path('manuales/descarga/<manualId>', views.manualesDescarga, name="Manuales descarga"),
    path('manuales/alta', views.manualesAlta, name="Manuales alta"),
    path('manuales/modificacion/<manualId>', views.manualesModificacion, name="Manuales modificacion"),
    path('manuales/borrar/<manualId>', views.manualesBaja, name="Manuales borrar"),

    # Consulta ordenes #
    path('buscar', views.buscarOrden, name="Buscar"),
    path('resultadorden/', views.resultadoOrden),
]