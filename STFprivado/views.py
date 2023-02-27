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
        miFormulario = UsuarioFormularioActualizar(request.POST) #el formulario es el del usuario
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data     #info en modo diccionario

            #actualizar la info del usuario activo
            usuario.first_name = informacion['nombre']
            usuario.last_name = informacion['apellido']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "STFprivado/taller.html")
    else:
        miFormulario= UsuarioFormulario(initial={'nombre':usuario.first_name, 'apellido':usuario.last_name, 'email':usuario.email})

    return render(request, "STFprivado/Autenticar/editarUsuario.html",{'miFormulario':miFormulario})

#################### CRUD Ordenes de reparación ####################
def ordenesLista(request):
    ordenes = Ordenes.objects.all()
    return render(request, "STFprivado/ordenes/ordenesLista.html",{'datos':ordenes})

def ordenesDetalle(request,ordenId):
    orden = Ordenes.objects.filter(id=ordenId)
    return render(request, "STFprivado/ordenes/ordenesDetalle.html",{'datos':orden})

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

            contexto = {'datos':Ordenes.objects.all()}
            return render(request, "STFprivado/ordenes/ordenesLista.html",contexto)
    else:
        miFormulario = OrdenesFormulario() # Esto es para que la primera vez se muestre el formulario vacio
 
    return render(request, "AppSTF/cargaFormularios.html", {"miFormulario": miFormulario}) # Envía el formulario a la plantilla

@login_required
def ordenesModificacion(request,ordenId):
    ordenEditar = Ordenes.objects.get(id=ordenId)

    if request.method == "POST":
 
        miFormulario = OrdenesFormulario(request.POST, request.FILES)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            ordenEditar.estado = informacion["estado"]
            ordenEditar.cliente = informacion["cliente"]
            ordenEditar.tipo = informacion["tipo"]
            ordenEditar.marca =informacion["marca"]
            ordenEditar.modelo = informacion["modelo"]
            ordenEditar.obs = informacion["obs"]
            ordenEditar.presupuesto = informacion["presupuesto"]
            
            ordenEditar.save()

            contexto = {'datos':Ordenes.objects.all()}
            return render(request, "STFprivado/ordenes/ordenesLista.html",contexto)
    else:
        miFormulario = OrdenesFormulario(initial={ "estado":ordenEditar.estado,
                                                    "cliente":ordenEditar.cliente,
                                                    "tipo":ordenEditar.tipo,
                                                   "marca":ordenEditar.marca,
                                                    "modelo":ordenEditar.modelo,
                                                    "obs":ordenEditar.obs,
                                                    "presupuesto":ordenEditar.presupuesto,})

    return render(request, "AppSTF/cargaFormularios.html", {"miFormulario": miFormulario,'titulo':"Editar Orden"})    

@login_required
def ordenesBaja(request,ordenId):
    ordenBorrar = Ordenes.objects.get(id=ordenId)
    if request.method == "POST":
        ordenBorrar.delete()

        contexto = {'datos':Ordenes.objects.all()}
        return render(request, "STFprivado/ordenes/ordenesLista.html",contexto)
    else:
        contexto = {'datos':ordenBorrar,'titulo':"Eliminar:"}

    return render(request, "STFprivado/ordenes/ordenesBorrar.html",contexto) 

#################### CRUD Base de datos de clientes ####################
def clientesLista(request):
    clientes = Clientes.objects.all()
    return render(request, "STFprivado/clientes/clientesLista.html",{'datos':clientes})

def clientesDetalle(request,clienteId):
    cliente = Clientes.objects.filter(id=clienteId)
    return render(request, "STFprivado/clientes/clientesDetalle.html",{'datos':cliente})

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

            contexto = {'datos':Clientes.objects.all()}
            return render(request, "STFprivado/clientes/clientesLista.html",contexto)
    else:
        miFormulario = ClientesFormulario()
 
    return render(request, "AppSTF/cargaFormularios.html", {"miFormulario": miFormulario})

@login_required
def clientesModificacion(request,clienteId):
    clienteEditar = Clientes.objects.get(id=clienteId)

    if request.method == "POST":
 
        miFormulario = ClientesFormulario(request.POST, request.FILES)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            clienteEditar.razonSocial= informacion["razonSocial"]
            clienteEditar.cuit = informacion["cuit"]
            clienteEditar.contacto = informacion["contacto"]
            clienteEditar.email =informacion["email"]
            clienteEditar.telefono = informacion["telefono"]
            clienteEditar.direccion= informacion["direccion"]
            
            clienteEditar.save()

            contexto = {'datos':Clientes.objects.all()}
            return render(request, "STFprivado/clientes/clientesLista.html",contexto)
    else:
        miFormulario = ClientesFormulario(initial={ "razonSocial":clienteEditar.razonSocial,
                                                    "cuit":clienteEditar.cuit,
                                                    "contacto":clienteEditar.contacto,
                                                    "email":clienteEditar.email,
                                                    "telefono":clienteEditar.telefono,
                                                    "direccion":clienteEditar.direccion,})
 
    return render(request, "AppSTF/cargaFormularios.html", {"miFormulario": miFormulario,'titulo':"Editar Máquina"})    

@login_required
def clientesBaja(request,clienteId):
    clienteBorrar = Clientes.objects.get(id=clienteId)
    if request.method == "POST":
        clienteBorrar.delete()
        contexto = {'datos':Clientes.objects.all()}
        return render(request, "STFprivado/clientes/clientesLista.html",contexto)
    else:
        contexto = {'datos':clienteBorrar,'titulo':"Eliminar:"}

    return render(request, "STFprivado/clientes/clientesBorrar.html",contexto) 