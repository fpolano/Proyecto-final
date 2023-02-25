from django.urls import path
from STFprivado import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('taller', views.paginaTaller, name="Taller"),

    # Autenticación #
    path('login', views.ingresar, name = 'Ingresar'),
    path('logout', LogoutView.as_view(template_name='STFprivado/Autenticar/logout.html'), name='Salir'),
    path('register', views.nuevoUsuario, name = 'Nuevo Usuario'),
    path("editUser", views.editarUsuario, name="Editar Usuario"),

    # CRUD Clientes #
    path('clientes', views.clientesAlta, name="Clientes alta"),

    # CRUD Ordenes de reparación #
    path('reparaciones', views.ordenesAlta, name="Reparaciones alta"),
]