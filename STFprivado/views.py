from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from STFprivado.models import *
from STFprivado.forms import *

# Create your views here.
#################### Autenticación de usuarios ####################


#################### CRUD Ordenes de reparación ####################
def ordenesFormulario(request):
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
def clientesFormulario(request):
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