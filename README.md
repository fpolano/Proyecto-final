# Proyecto-final
Proyecto final Curso Python CoderHouse. Página web con Django

--------------------------------------------------------------------------------------------
Del readme de Tercera-pre-entrega
Repositorio del proyecto Django correspondiente a la tercera preentrega del curso de Python de CoderHouse

Proyecto en django cuyo objetivo final es generar una web que permita administrar las reparaciones, venta de máquinas y respuestos, manuales y base de datos de clientes de un taller de reparación de máquinas herramientas.
---------------------------------------------------------------------------------------------

## Versión 0.1:
--------------------------------------------------------------------------------------------
Del readme de Tercera-pre-entrega
Repositorio del proyecto Django correspondiente a la tercera preentrega del curso de Python de CoderHouse

Proyecto en django cuyo objetivo final es generar una web que permita administrar las reparaciones, venta de máquinas y respuestos, manuales y base de datos de clientes de un taller de reparación de máquinas herramientas.
---------------------------------------------------------------------------------------------
Se incorporó:
    - Tabla de clientes con formulario de carga
    - Tabla de ordenees de reparación con formulario de carga y consulta de reparaciones por nobre de cliente
    - Tabla de manuales con formulario de carga
    - Tabla de maquinas en venta con formulario de carga
    - Tabla de repuestos en venta con formulario de carga
    - Todas la base de datos es de acceso público para la carga de información. IMPORTANTE: No todas las clases poseen registros cargados pero se probaron los formularios de cada una. El html del formulario de carga es único cambiandose el form que levanta.

Mejoras deseadas pára proximas versiones:
    - Generar 2 niveles de acceso, uno público para mostrar el contenido de la base de datos y otro privado -para el CRUD de la misma
    - Agregar a las tablas productos y repuestos un campo imagen que muestr el elementoi físico.
    - Agregar a la tabla manuales un campo archivo para almacenar los mismos y permitir su descarga.

-------------------------------------------

## Versión 0.2:
Se incorporó:
    - Vistas de alta, baja, modificación y lista para la base de datos Maquinas
    - Copyright con datos del desarrollador (yo XD)

## Versión 0.3:
Se incorporó:
    - Funcionalidad completa de la vista detalle de máquinas incluido mostrar una imagen del producto
    - CRUD de usuarios
    - Pagina de inicio interna cuando se accede con usuario para la navegación de clientes y ordenes de trabajo

## Versión 0.4:
Se incoroporó:
    - Vistas de alta, baja, modificación, detalle y lista para todas las bases de datos (repuestos, ordenes de reparación, clientes y  manuales-descarga en lugar de detalle-)
    - Se cporrigió problema con vista de registro de nuecvo usuario

Mejoras futuras deseables:
    - Validación de datos de alta y modificación para todas las tablas
    - Roles de usuarios para controlar nivel de privilegios del CRUD. Validar creación por email.
    - Mejoras estéticas en css y html
