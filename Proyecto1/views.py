from datetime import datetime
from django.http import HttpResponse

def saludo(request): #primera vista

    return HttpResponse("Hola alumnos esta es nuestra primera pagina")

def despedida(request):

    return HttpResponse("Adios")

def dameFecha(request):
    
    fecha_actual = datetime.now()

    documento = """<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)