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
----------
django-admin startproject config .: (el "." es para que me lo cree en la carpeta y no se creen 2 carpetas,cuando instalamos django me creo un script que se llama django-admin.exe que es un archivo binario) Nos crea en nuestra carpeta de trabajo una carpeta config. que es donde esta la configuracion de django.

archivo manage.py: es el primer script que ejecuta django 
-------------------------------------------------------------------------------------------
ls : vamos a visualizar a manage.py
python manage.py runserver: Ejecutamos por primera vez un proyecto de django. comenzamos el servidor de desarrollo en la url que nos brinda
podemos detenerlo con Crl + C
luego agregamos todos los cambios  con git add . 
y sacamos la foto 
-------------------------------------------------------------------------------------------


