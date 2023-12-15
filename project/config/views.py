from django.http import HttpResponse

def saludo(request):
    return HttpResponse("hola")

def saludo2(request):
    nombre = input("ingresa tu nombre")
    return HttpResponse(f"hola {nombre}")

def nombre (request, nombre):
    return HttpResponse(nombre)