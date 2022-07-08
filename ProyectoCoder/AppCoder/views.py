from django import http
from django.shortcuts import render
from AppCoder.models import Curso, Profesor
from django.http import HttpResponse
from AppCoder.forms import CursoForm, ProfeForm

# Create your views here.


def curso(self):
    
    curso=Curso(nombre="Django", comision=939393)
    curso.save()
    texto=f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render (request, "Appcoder/inicio.html") # DEVUELVE UN TEMPLATE

def cursos(request):
    return render (request, "Appcoder/cursos.html")

def profesores(request):
    return render (request, "Appcoder/profesores.html")

def estudiantes(request):
    return render (request, "Appcoder/estudiantes.html")


def entregables(request):
    return render (request, "Appcoder/entregables.html")

"""def cursoFormulario(request):
    if (request.method=="POST"):
        nombre= request.POST.get("curso")
        comision= request.POST.get("comision")
        curso= Curso(nombre=nombre, comision=comision)
        curso.save()
        return render (request, "Appcoder/inicio.html")



    
    return render(request, "AppCoder/cursoFormulario.html") FORMULARIO HTML
"""
def cursoFormulario(request):
    if (request.method=="POST"):
        form= CursoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre= info["nombre"]
            comision= info["comision"]
            curso= Curso(nombre=nombre, comision=comision)
            curso.save()
            return render (request, "Appcoder/inicio.html")
    else:
        form= CursoForm()
    return render(request, "AppCoder/cursoFormulario.html", {"formulario":form})

def profeFormulario(request):
    if (request.method=="POST"):
        form= ProfeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            profesion= info["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            return render (request, "Appcoder/inicio.html")
    else:
        form= ProfeForm()
    return render(request, "AppCoder/profeForm.html", {"formulario":form})

def busquedaComision(request):

    return render(request, "AppCoder/busquedaComision.html") 

def buscar(request):
    if request.GET["comision"]:
        comi=request.GET["comision"]
        cursos= Curso.objects.filter(comision=comi)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "AppCoder/busquedaComision.html", {"error":"No se ingreso ninguna comision"})