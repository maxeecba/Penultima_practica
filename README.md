# Penultima_practica

"""echo "# Penultima_practica" >> README.md""" #lo que hace esto es crear un archivo readme y el contenido es lo que está dentro de las comillas
--------------------------------------------------------------------------------------------
git init: Inicializa un repositorio (se crea una carpeta oculta que si la borramos se borra el seguimiento)
---------------------------------------------------------------------------------------------
git add README.md:(tambien se puede hacer clic en el + en control de codigo fuente) Este comando envía al stage area
------------------------------------------------------------------------------------
Hay 3 areas: el area de trabajo. Que es donde tenemos los archivos después hay 2 areas que son invisibles. que son:
1- El Stage Area (Area de preaparacion): Que es donde vamos agregando las cosas que van funcionando bien (la caracteristica)
2 - El area de repositorio: Es una fotografia de como está el codigo en ese momento. y despues lo subimos a la nube 
Solo podemos push (empujar) los commit (Fotografias), una vez que empujamos las fotografías quedan en al nube lo podemos tirar(Descargar). 
-------------------------------------------------------------------------------------------
git commit -m "first commit": Lo envía a la 3° seccion a la fotografía el -m significa que le vamos a dar un mensaje ej :"primer commit"

git status: Sirve para ver el estado de nuestro trabajo
git log: Sirve para ver todas las fotografías que tengo
---------------------------------------------------------------------------------------
git branch -M main: sirve para cambiar el nombre de mi rama a veces por defecto es "master" y la cambia a "main" o al nombre que le pongamos.
---------------------------------------------------------------------------------------
: Va agregar esta url ( que es mi repositorio que esta vacío), voy agregar una fuente osea el lugar de donde se emana el codigo.
----------------------------------------------------------------------------------------
git push -u origin main: "main" es el nombre de la rama la cual puede variar el nombre ya que se lo cambia
Tambien podemos hacer clic en el iconito que está en la parte inferior izquierda que es como un circulito con flechas y subirá los cambios a nuestro repositorio de github.
------------------------------------------------------------------------------------------
py -m venv .venv: nos sirve para crear un entorno vitual para poder instalar django y no tener problemas de versiones.
----
.\.venv\Scripts\activate: luego con este comando nos metemos en lalas carpetas .venv y scripts para ejecutar activate
------------------------------------------------------------------------------------------
cd project: nos metemos a la carpeta del proyecto
d
pip install django: instalamos django
-------------------------------------------------------------------------------------------
django-admin --version: nos muestra la version de django que tenemos instalada 
------------------------------------------------------------------------------------------
django-admin startproject config .: (el "." es para que me lo cree en la carpeta y no se creen 2 carpetas,cuando instalamos django me creo un script que se llama django-admin.exe que es un archivo binario) Nos crea en nuestra carpeta de trabajo una carpeta config. que es donde esta la configuracion de django.

archivo manage.py: es el primer script que ejecuta django 
-----------------
--------------------------------------------------------------------------
ls : vamos a visualizar a manage.py

python manage.py runserver: Ejecutamos por primera vez un proyecto de django. comenzamos el servidor de desarrollo en la url que nos brinda
podemos detenerlo con Crl + C
luego agregamos todos los cambios  con git add . 
y sacamos la foto 
-------------------------------------------------------------------------------------------
git merge dev: primero debemos pararnos en la rama principal para ejecutar este comando que lo que hace es fusionar los cambios de la rama dev con la rama principal 
--------------------------------------------------------------------------------------------
## CREANDO UNA APLICACION

django-admin startapp core: Es el primer comando que vamos a usar para crear una aplicacion, 

paso1:crear una carpeta templates dentro de la carpeta core
----------------------------------------------------------------------------------------
paso2: crear una carpeta que se llame igual que el proyecto en este caso "core"
paso3: dentro de la carpeta core crear un archivo .index.html !+tab (cambiamos lenguaje)
----------------------------------------------------------------------------------------
paso4: vamos a views.py que esta dentro de core, creamos una funcion 
def index(request):
    return render(request,"core/index.hml)#primero nombre de la plantilla(va buscar nuestro archivo dentro de la carpeta template, por lo tanto tenemos que poner nuestra subcarpeta core(nombre de la aplicacion) seguido del archivo index.html )
en esta funcion vamos a devolver una plantilla
----------------------------------------------------------------------------------------
paso5: Crear la urls.py dentro de core hacemos una copia de la urls de config.y dejamos solo
from django.urls import path
from .views import index (index es el nombre de nuestra funcion)

urlpatterns = [
    path('core/', index),
]
El tema es que django no sabe que existe esta aplicacion, para hacerle saber que exite, tenemos que registrarla en config/settings.py. Hay una variable que se llama INSTALLED_APP y dentro de esta agregamos nuestra aplicacion que se llama "core"
---------------
paso6: Y en las urls de config tenemos que indicarle que queremos incluir las urls de core. (las urls que estan en config son el archivo principal). por eso incluimos un path dentro de urlpatterns donde si no le ponemos por ejemplo  path('core/',include("core.urls")) no va hacer falta escribir en la barra del navegador http://127.0.0.1:8000/core y de esta forma accedemos a la pagina sin especificar la seccion
urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',include("core.urls")) #es el nombre de la aplicacion seguido del nombre del modulo
]
--------------
paso7: no olvidarse de agregar la funcion include dentro de la importacion: 
"from django.urls import path, include" (dentro de include necesito un argumento entre comillas que es el nombre de la aplicación que es core "." el nombre del modulo "core.urls"  )
--------------
paso8: si queremos quitar http://127.0.0.1:8000/core/core vamos a urls de core y a urls de config y le quitamos le borro core del path
-------------
## ¿ Como hago para pasarle una variable a HTML ?
## Las variables en django van entre 2 llaves {{}}
Nos vamos a core/views.py y aquí le enviamos un diccionario. por ejemplo:
def index(request):
    return render(request,"core/index.html", {"nombre": "ferreteria"})
Esta clave "nombre" la puedo reutilizar en index.hml dentro de 2 llaves. Por ejemplo de la siguiente forma 
<h1>Proyecto {{ nombre }}</h1>

## Ultimo
git clone LINK de github para descargar
lo descarga donde estemos parados. 
para que funcione tenemos que crear el entorno virtual con (py -m venv .venv) y activarlo con (.\.venv\Scripts\activate)
Y instalar django



