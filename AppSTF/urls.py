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
    path('repuestos', views.repuestosAlta, name="Repuestos alta"),

    # CRUD manuales #
    path('manuales', views.manualesAlta, name="Manuales alta"),

    # Consulta ordenes #
    path('buscar', views.buscarOrden, name="Buscar"),
    path('resultadorden/', views.resultadoOrden),
]