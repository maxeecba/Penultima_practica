from django.http import HttpResponse

def saludo(request):
    return HttpResponse("hola")

def saludo2(request):
    nombre = input("ingresa tu nombre")
    return HttpResponse(f"hola {nombre}")

def nombre (request, nombre):
    return HttpResponse(nombre)

def fecha_hora(request):
    from  datetime import datetime
    ahora = datetime.now().strftime(r"%d/%m/%Y %H:%M:%S")
    return HttpResponse(ahora)