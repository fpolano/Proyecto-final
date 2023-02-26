from django.urls import path
from STFprivado import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('taller', views.paginaTaller, name="Taller"),

    # Autenticación #
    path('login', views.ingresar, name = 'Ingresar'),
    path('logout', LogoutView.as_view(template_name='STFprivado/Autenticar/logout.html'), name='Salir'),
    path('register', views.nuevoUsuario, name = 'Nuevo Usuario'),
    path("editUser", views.editarUsuario, name = "Editar Usuario"),

    # CRUD Clientes #
    path('clientes', views.clientesLista, name = "Clientes lista"),   
    path('clientes/detalle/<clienteId>', views.clientesDetalle, name="Clientes detalle"),
    path('clientes/alta', views.clientesAlta, name="Clientes alta"),
    path('clientes/modificacion/<repuestoId>', views.clientesModificacion, name="Clientes modificacion"),
    path('clientes/borrar/<repuestoId>', views.clientesBaja, name="Clientes borrar"),

    # CRUD Ordenes de reparación #
    path('reparaciones', views.ordenesLista, name = "Reparaciones lista"),
    path('reparaciones/detalle/<ordenId>', views.ordenesDetalle, name="Reparaciones detalle"),
    path('reparaciones/alta', views.ordenesAlta, name="Reparaciones alta"),
    path('reparaciones/modificacion/<ordenId>', views.ordenesModificacion, name="Reparaciones modificacion"),
    path('reparaciones/borrar/<ordenId>', views.ordenesBaja, name="Reparaciones borrar"),
]