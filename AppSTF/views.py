from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from AppSTF.forms import *
from AppSTF.models import *
from STFprivado.models import Ordenes

# Create your views here.
# En los CRUD para alta y modificación se mantiene la programación funcional de las vistas

#################### Página de inicio ###################
def inicio(request):
    return render(request,"AppSTF/index.html")

#################### Página con la descripción de la empresa ################# 
def sobre(request):
    return render(request,"AppSTF/about.html")

#################### Página con la descripción de la empresa ################# 
def desarrollador(request):
    return render(request,"AppSTF/copyright.html")

#################### CRUD Máquinas a la venta ####################
def maquinasLista(request):
    maquinas = Maquinas.objects.all()
    return render(request, "AppSTF/Maquinas/maquinasLista.html",{'datos':maquinas})

def maquinasDetalle(request,maquinaId):
    maquina = Maquinas.objects.filter(id=maquinaId)
    print(maquina)
    return render(request, "AppSTF/Maquinas/maquinasDetalle.html",{'datos':maquina})

@login_required
def maquinasAlta(request):
    if request.method == "POST":
 
        miFormulario = MaquinasFormulario(request.POST, request.FILES)
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            maquina = Maquinas(nombre = informacion["nombre"],
                                tipo = informacion["tipo"],
                                marca = informacion["marca"],
                                modelo = informacion["modelo"],
                                desc = informacion["desc"],
                                precio = informacion["precio"],
                                stock = informacion["stock"],
                                foto = informacion["foto"],
                                )
                  #             
            maquina.save()

            contexto = {'datos':Maquinas.objects.all(),'titulo':"Nueva Máquina"}
            return render(request, "AppSTF/Maquinas/maquinasLista.html",contexto)
    else:
        miFormulario = MaquinasFormulario()
 
    return render(request, "AppSTF/cargaFormularios.html", {"miFormulario": miFormulario,'titulo':"Nueva Máquina"})

@login_required
def maquinasModificacion(request,maquinaId):
    maquinaEditar = Maquinas.objects.get(id=maquinaId)

    if request.method == "POST":
 
        miFormulario = MaquinasFormulario(request.POST, request.FILES)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            maquinaEditar.nombre = informacion["nombre"]
            maquinaEditar.tipo = informacion["tipo"]
            maquinaEditar.marca = informacion["marca"]
            maquinaEditar.modelo = informacion["modelo"]
            maquinaEditar.desc = informacion["desc"]
            maquinaEditar.precio = informacion["precio"]
            maquinaEditar.stock = informacion["stock"]
            maquinaEditar.foto = informacion["foto"]
            
            maquinaEditar.save()

            contexto = {'datos':Maquinas.objects.all(),'titulo':"Editar Máquina"}
            return render(request, "AppSTF/Maquinas/maquinasLista.html",contexto)
    else:
        miFormulario = MaquinasFormulario(initial={"nombre":maquinaEditar.nombre,
                                                    "tipo":maquinaEditar.tipo,
                                                    "marca":maquinaEditar.marca,
                                                    "modelo":maquinaEditar.modelo,
                                                    "desc":maquinaEditar.desc,
                                                    "precio":maquinaEditar.precio,
                                                    "stock":maquinaEditar.stock,
                                                    "foto":maquinaEditar.foto,})
 
    return render(request, "AppSTF/cargaFormularios.html", {"miFormulario": miFormulario,'titulo':"Editar Máquina"})    

@login_required
def maquinasBaja(request,maquinaId):
    maquinaBorrar = Maquinas.objects.get(id=maquinaId)
    if request.method == "POST":
        maquinaBorrar.delete()
        contexto = {'datos':Maquinas.objects.all()}
        return render(request, "AppSTF/Maquinas/maquinasLista.html",contexto)
    else:
        contexto = {'datos':maquinaBorrar,'titulo':"Eliminar:"}

    return render(request, "AppSTF/Maquinas/maquinasBorrar.html",contexto)    

#################### CRUD Repuestos a la venta ####################

@login_required
def repuestosAlta(request):
    if request.method == "POST":
 
        miFormulario = RepuestosFormulario(request.POST, request.FILES) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            repu = Repuestos(nombre = informacion["nombre"],
                            marca = informacion["marca"],
                            modelo =informacion["modelo"],
                            precio = informacion["precio"],
                            stock = informacion["stock"],
                            foto = informacion["foto"],
                            )
            repu.save()
            return render(request, "AppSTF/index.html")
    else:
        miFormulario = RepuestosFormulario()
 
    return render(request, "AppSTF/cargaFormularios.html", {"miFormulario": miFormulario,'titulo':"Nuevo Repuesto"})

#################### CRUD Biblioteca de Manuales ####################

@login_required
def manualesAlta(request):
    if request.method == "POST":
 
        miFormulario = ManualesFormulario(request.POST, request.FILES) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            manual = Manuales(tipo = informacion["tipo"],
                            marca = informacion["marca"],
                            modelo = informacion["modelo"],
                            archivo = informacion["archivo"],
                            )
            manual.save()
            return render(request, "AppSTF/index.html")
    else:
        miFormulario = ManualesFormulario()
 
    return render(request, "AppSTF/cargaFormularios.html", {"miFormulario": miFormulario,'titulo':"Nuevo Manual"})


################### Consulta reparaciones (accesible publicamente) #################
def buscarOrden(request):
    return render(request,"AppSTF/buscarOrden.html")

def resultadoOrden(request):
    if request.GET["cliente"]:
        cliente = request.GET["cliente"]
        reparaciones = Ordenes.objects.filter(cliente__icontains=cliente)
        return render(request,"AppSTF/buscarorden.html",{"ordCliente":reparaciones})
    elif request.GET["numero"]:
        numero = int(request.GET["numero"])
        reparaciones = Ordenes.objects.filter(id=numero)
        return render(request,"AppSTF/buscarorden.html",{"ordCliente":reparaciones})
    else:
        respuesta = "No se encontraron ordenes"
        return render(request,"AppSTF/buscarorden.html",{"respuesta":respuesta})
    