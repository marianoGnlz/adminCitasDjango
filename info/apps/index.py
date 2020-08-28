from django.http import HttpResponse
from django.shortcuts import render

def base(request):
    cosas = render(request,"base.html")
    return HttpResponse(cosas)

def baseCita(request):
    dictForm = {
        "mascota": request.GET["mascota"],
        "propietario": request.GET["propietario"],
        "fecha": request.GET["fecha"],
        "hora": request.GET["hora"],
        "sintomas": request.GET["sintomas"]
    }

    cosas = render(request,"cita.html", dictForm)
    return HttpResponse(cosas)