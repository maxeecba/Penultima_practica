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
---------------------------------------------------------------------------------------
git log: Sirve para ver todas las fotografías que tengo
El HEAD: indica que está apuntando a EstoEsUnaRama, y que tambien esta apundando a "origin/EstoEsUnaRama(Esto es internet github)"
---------------------------------------------------------------------------------------
git branch -M main: sirve para cambiar el nombre de mi rama a veces por defecto es "master" y la cambia a "main" o al nombre que le pongamos.
---------------------------------------------------------------------------------------
: Va agregar esta url ( que es mi repositorio que esta vacío), voy agregar una fuente osea el lugar de donde se emana el codigo.
----------------------------------------------------------------------------------------
git push -u origin main: "main" es el nombre de la rama la cual puede variar el nombre ya que se lo cambia
Tambien podemos hacer clic en el iconito que está en la parte inferior izquierda que es como un circulito con flechas y subirá los cambios a nuestro repositorio de github.
------------------------------------------------------------------------------------------
Buenas Practicas: La rama principal hay que dejarla en main.. y la rama para solucionar otras cuestiones como bugs, o de desarrollo (dev) una vez que funciona algo lo unimos a la rama principal(main), cuando lo integramos a dev hacemos un marge lo integramos, lo fucionamos.
Git permite tener un control de versiones.
Lo principal que vamos hacer ahora es crear una rama
para hacer esto seguimos con los siguientes comandos:
----------------------------------------------------------------------------------------
git branch: Vemos todas las ramas que tenemos.
git branch dev(nombre de la rama): sirve para crear una rama Esto hace una copia de la rama principal
a medida que vaya trabajando sobre la rama copia cuando está terminado se fusiona
----------------------------------------------------------------------------------------
git checkout dev: cambia a la rama que creamos para trabajar en ella.
o podemos hacer clic en la parte inferior izquierda 
----------------------------------------------------------------------------------------
