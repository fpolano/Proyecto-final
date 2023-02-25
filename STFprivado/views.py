from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from STFprivado.models import *
from STFprivado.forms import *
 
# Create your views here.
#################### Página principal taller #######################
@login_required()
def paginaTaller(request):
    return render(request,"STFprivado/taller.html")

#################### Autenticación y CRUD de usuarios ####################
def nuevoUsuario(request):
    if request.method == 'POST':    #cuando le haga click al botón
        form = UsuarioFormulario(request.POST)   #leer los datos   llenados en el formulario
        if form.is_valid():
            user=form.cleaned_data['username']
            form.save()          
            return render(request, "AppSTF/index.html")   
    else:
        form = UsuarioFormulario()   #formulario de django que nos permite crear usuarios        

    return render(request, "STFprivado/Autenticar/registrarUsuario.html", {'form':form})

def ingresar(request):
    if request.method == 'POST': #al presionar el botón "Iniciar Sesión"
        form = AuthenticationForm(request, data = request.POST) #leer la data del formulario de inicio de sesión
        if form.is_valid():         
            usuario=form.cleaned_data.get('username')   #leer el usuario ingresado
            contra=form.cleaned_data.get('password')    #leer la contraseña ingresada
            user=authenticate(username=usuario, password=contra)    #buscar al usuario con los datos ingresados
            if user:    #si ha encontrado un usuario con eso datos
                login(request, user)   #hacemos login
                #mostramos la página de inicio con un mensaje de bienvenida.
                return render(request, "STFprivado/taller.html")
        else:   #si el formulario no es valido (no encuentra usuario)
            #mostramos la página de inicio junto a un mensaje de error.    
            return render(request, "STFprivado/taller.html")
    else:           
        form = AuthenticationForm() #mostrar el formulario

    return render(request, "STFprivado/Autenticar/login.html", {'form':form})    #vincular la vista con la plantilla de html

@login_required
def editarUsuario(request):
    usuario = request.user #usuario activo (el que ha iniciado sesión)
    if request.method == "POST":    #al presionar el botón
        miFormulario = UsuarioFormulario(request.POST) #el formulario es el del usuario
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data     #info en modo diccionario

            #actualizar la info del usuario activo
            usuario.first_name = informacion['nombre']
            usaurio.last_name = informacion['apellido']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "STFprivado/taller.html")
    else:
        miFormulario= UsuarioFormulario(initial={'nombre':usuario.first_name, 'apellido':usuario.last_name, 'email':usuario.email})

    return render(request, "STFprivado/Autenticar/editarUsuario.html",{'miFormulario':miFormulario})

#################### CRUD Ordenes de reparación ####################
@login_required
def ordenesAlta(request):
    if request.method == "POST": #indica que se hizo click a enviar
 
        miFormulario = OrdenesFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            orden = Ordenes(estado = informacion["estado"],
                            cliente = informacion["cliente"],
                            tipo = informacion["tipo"],
                            marca =informacion["marca"],
                            modelo = informacion["modelo"],
                            obs = informacion["obs"],
                            presupuesto = informacion["presupuesto"],
                            )
            orden.save()
            return render(request, "AppSTF/index.html")
    else:
        miFormulario = OrdenesFormulario() # Esto es para que la primera vez se muestre el formulario vacio
 
    return render(request, "AppSTF/carga.html", {"miFormulario": miFormulario}) # Envía el formulario a la plantilla

#################### CRUD Base de datos de clientes ####################
@login_required
def clientesAlta(request):
    if request.method == "POST":
 
        miFormulario = ClientesFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cliente = Clientes(razonSocial= informacion["razonSocial"],
                                cuit = informacion["cuit"],
                                contacto = informacion["contacto"],
                                email =informacion["email"],
                                telefono = informacion["telefono"],
                                direccion= informacion["direccion"],
                                )
            cliente.save()
            return render(request, "AppSTF/index.html")
    else:
        miFormulario = ClientesFormulario()
 
    return render(request, "AppSTF/carga.html", {"miFormulario": miFormulario})