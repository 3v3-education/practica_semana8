from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def inicio(request):
    return render(request, 'publicaciones/inicio.html')

def base (request):
    return render(request,'publicaciones/base.html')

def lista_publicaciones(request):
    publicaciones = [
        {"titulo": "mi primer publicacion", "autor":"Ana"},
        {"titulo": "Aprendiendo djangoo!", "autor":"Luis"},
        {"titulo": "Vistas y rutas", "autor":"Marta"}
    ]

    contexto = {"publicaciones": publicaciones}
    return render(request,"publicaciones/lista_publicaciones.html", contexto)

def lista_autores(request):
    autores = [
        {"nombre":"Camila","apellido":"Arena"},
        {"nombre":"Mayra","apellido":"Caporale"},
        {"nombre":"Ana Lucia","apellido":"Arias"}
    ]
    context = {"autores":autores}
    return render(request,'publicaciones/lista_autores.html',context)

def contacto(request):
    return render(request,'publicaciones/contacto.html')

def about(request):
    return render(request,'publicaciones/about.html')
